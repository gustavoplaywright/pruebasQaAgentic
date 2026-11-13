#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
AGENTE QA ISTQB - Generador Profesional de Casos de Prueba
=============================================================================
Este agente procesa archivos de especificación de requerimientos (historias
de usuario, requerimientos funcionales, reglas de negocio), aplica técnicas
formales de diseño de pruebas ISTQB (Partición de Equivalencia, Análisis de
Valores Límite, Tablas de Decisión, Transición de Estados, Adivinación de Errores)
y genera un libro de cálculo Excel (.xlsx) corporativo con trazabilidad completa.
=============================================================================
"""

import os
import sys
import re
import json
import argparse
from datetime import datetime
from typing import List, Dict, Any, Optional

# Asegurar codificación UTF-8 en consola para Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:
    print("Error: openpyxl no está instalado. Ejecute: pip install openpyxl")
    sys.exit(1)


# =============================================================================
# MODELO DE DATOS ISTQB
# =============================================================================

class TestCase:
    def __init__(
        self,
        tc_id: str,
        module: str,
        req_ref: str,
        title: str,
        description: str,
        test_type: str,
        technique: str,
        level: str,
        priority: str,
        preconditions: str,
        steps: str,
        test_data: str,
        expected_result: str,
        postconditions: str,
        status: str = "No Ejecutado",
        executed_by: str = "",
        execution_date: str = "",
        defect_notes: str = ""
    ):
        self.tc_id = tc_id
        self.module = module
        self.req_ref = req_ref
        self.title = title
        self.description = description
        self.test_type = test_type
        self.technique = technique
        self.level = level
        self.priority = priority
        self.preconditions = preconditions
        self.steps = steps
        self.test_data = test_data
        self.expected_result = expected_result
        self.postconditions = postconditions
        self.status = status
        self.executed_by = executed_by
        self.execution_date = execution_date
        self.defect_notes = defect_notes

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ID Caso": self.tc_id,
            "Módulo": self.module,
            "Ref. Requerimiento": self.req_ref,
            "Título": self.title,
            "Descripción / Objetivo": self.description,
            "Tipo de Prueba": self.test_type,
            "Técnica ISTQB": self.technique,
            "Nivel de Prueba": self.level,
            "Prioridad": self.priority,
            "Precondiciones": self.preconditions,
            "Pasos de Prueba": self.steps,
            "Datos de Prueba": self.test_data,
            "Resultado Esperado": self.expected_result,
            "Postcondiciones": self.postconditions,
            "Estado": self.status,
            "Ejecutado Por": self.executed_by,
            "Fecha Ejecución": self.execution_date,
            "Defectos / Observaciones": self.defect_notes,
        }


class Requirement:
    def __init__(
        self,
        req_id: str,
        title: str,
        module: str,
        description: str,
        acceptance_criteria: List[str] = None,
        business_rules: List[str] = None,
        inputs: List[Dict[str, Any]] = None
    ):
        self.req_id = req_id
        self.title = title
        self.module = module
        self.description = description
        self.acceptance_criteria = acceptance_criteria or []
        self.business_rules = business_rules or []
        self.inputs = inputs or []


# =============================================================================
# ANALIZADOR DE REQUERIMIENTOS
# =============================================================================

class RequirementParser:
    """
    Analiza archivos de requerimientos en Markdown, Texto plano o JSON
    identificando módulos, IDs, criterios de aceptación, entradas y reglas.
    """

    @staticmethod
    def parse_file(file_path: str) -> List[Requirement]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo especificado no existe: {file_path}")

        ext = os.path.splitext(file_path)[1].lower()
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        if ext == ".json":
            return RequirementParser._parse_json(content)
        else:
            return RequirementParser._parse_text_or_markdown(content)

    @staticmethod
    def _parse_json(content: str) -> List[Requirement]:
        data = json.loads(content)
        reqs = []
        items = data if isinstance(data, list) else data.get("requirements", [data])
        for idx, item in enumerate(items, 1):
            req = Requirement(
                req_id=item.get("id", f"REQ-{idx:03d}"),
                title=item.get("title", f"Requerimiento {idx}"),
                module=item.get("module", "General"),
                description=item.get("description", ""),
                acceptance_criteria=item.get("acceptance_criteria", []),
                business_rules=item.get("business_rules", []),
                inputs=item.get("inputs", [])
            )
            reqs.append(req)
        return reqs

    @staticmethod
    def _parse_text_or_markdown(content: str) -> List[Requirement]:
        requirements: List[Requirement] = []
        
        # Detectar módulos o secciones principales y requerimientos individuales
        # Patrón para identificar encabezados de Requerimientos vs Módulos
        lines = content.splitlines()
        current_module = "General"
        
        req_blocks = []
        current_block = []
        current_req_module = "General"

        for line in lines:
            line_stripped = line.strip()
            # Detectar encabezado de Módulo
            mod_match = re.match(r'^(?:#{1,2}\s*(?:Módulo|Funcionalidad|Feature|Module):\s*([^\n\r]+)|(?:Módulo|Funcionalidad|Feature):\s*([^\n\r]+))', line_stripped, re.IGNORECASE)
            if mod_match:
                current_module = (mod_match.group(1) or mod_match.group(2)).strip()
                continue

            # Detectar inicio de Requerimiento (### RF-xxx, ## RF-xxx, RF-xxx:, etc.)
            req_match = re.match(r'^(?:#{1,4}\s*)?(?:(?:RF|HU|REQ|US)-[0-9A-Za-z_-]+|Requisito\s*\d+|Historia\s*\d+)[:\s-]', line_stripped, re.IGNORECASE)
            if req_match:
                if current_block:
                    req_blocks.append((current_req_module, "\n".join(current_block)))
                    current_block = []
                current_req_module = current_module
                current_block.append(line)
            else:
                if current_block:
                    current_block.append(line)
                elif line_stripped and not line_stripped.startswith("#"):
                    # Si aún no hemos iniciado un bloque formal pero hay contenido
                    pass

        if current_block:
            req_blocks.append((current_req_module, "\n".join(current_block)))

        # Si no se detectaron bloques formales con el patrón, procesar por párrafos
        if not req_blocks:
            req_blocks = [(current_module, content)]

        for idx, (mod, block_text) in enumerate(req_blocks, 1):
            block_lines = [l.strip() for l in block_text.splitlines() if l.strip()]
            if not block_lines:
                continue

            first_line = block_lines[0]
            # Extraer ID
            id_match = re.search(r'(?:RF|HU|REQ|US)-?[0-9A-Za-z_-]+', first_line, re.IGNORECASE)
            req_id = id_match.group(0).upper() if id_match else f"RF-{idx:03d}"

            # Extraer Título limpio
            title_clean = re.sub(r'^[#\s*\-:]+|(?:RF|HU|REQ|US)-?[0-9A-Za-z_-]+[:\s-]*', '', first_line).strip()
            title = title_clean if title_clean else f"Requerimiento {req_id}"

            desc_lines = []
            criterios = []
            reglas = []
            inputs = []
            
            mode = "desc"
            for line in block_lines[1:]:
                lower_line = line.lower()
                if any(k in lower_line for k in ["criterios de aceptaci", "acceptance criteria", "criterios:"]):
                    mode = "crit"
                    continue
                elif any(k in lower_line for k in ["reglas de negocio", "business rules", "reglas:"]):
                    mode = "rules"
                    continue
                elif any(k in lower_line for k in ["campos", "parámetros", "parametros", "inputs:"]):
                    mode = "inputs"
                    continue
                
                clean_line = re.sub(r'^[\*\-\d\.\s#]+', '', line).strip()
                if not clean_line:
                    continue

                if clean_line.lower().startswith("descripción:") or clean_line.lower().startswith("descripcion:"):
                    clean_line = re.sub(r'^(?:descripción|descripcion):\s*', '', clean_line, flags=re.IGNORECASE).strip()
                    desc_lines.append(clean_line)
                    continue

                if mode == "crit":
                    criterios.append(clean_line)
                elif mode == "rules":
                    reglas.append(clean_line)
                elif mode == "inputs":
                    inputs.append({"name": clean_line})
                else:
                    desc_lines.append(clean_line)

            description = " ".join(desc_lines) if desc_lines else title

            # Detectar criterios inline tipo Gherkin (Dado, Cuando, Entonces)
            gherkin_matches = re.findall(r'(?:Dado|Cuando|Entonces|Given|When|Then)[^\n\r]+', block_text, re.IGNORECASE)
            if gherkin_matches and not criterios:
                criterios.extend(gherkin_matches)

            if not criterios and not reglas:
                criterios.append(f"El sistema debe procesar exitosamente la solicitud de {title}.")
                criterios.append(f"El sistema debe validar los datos ingresados y rechazar entradas inválidas.")

            requirements.append(Requirement(
                req_id=req_id,
                title=title,
                module=mod,
                description=description,
                acceptance_criteria=criterios,
                business_rules=reglas,
                inputs=inputs
            ))

        return requirements


# =============================================================================
# MOTOR DE DISEÑO DE PRUEBAS ISTQB
# =============================================================================

class ISTQBTestGenerator:
    """
    Aplica técnicas de caja negra ISTQB a cada requerimiento:
    1. Partición de Equivalencia (Clases Válidas e Inválidas)
    2. Análisis de Valores Límite (BVA)
    3. Pruebas de Tablas de Decisión
    4. Pruebas de Transición de Estados
    5. Adivinación de Errores y Casos Negativos de Seguridad
    """

    @staticmethod
    def generate_test_cases(requirements: List[Requirement]) -> List[TestCase]:
        test_cases: List[TestCase] = []
        tc_counter = 1

        for req in requirements:
            req_tc_list = ISTQBTestGenerator._generate_for_single_req(req, tc_counter)
            test_cases.extend(req_tc_list)
            tc_counter += len(req_tc_list)

        return test_cases

    @staticmethod
    def _generate_for_single_req(req: Requirement, start_counter: int) -> List[TestCase]:
        cases: List[TestCase] = []
        counter = start_counter
        full_text = f"{req.title} {req.description} {' '.join(req.acceptance_criteria)} {' '.join(req.business_rules)}".lower()

        # ---------------------------------------------------------------------
        # 1. CASO FELIZ / CAMINO PRINCIPAL (Partición de Equivalencia - Válida)
        # ---------------------------------------------------------------------
        tc_id = f"TC_{req.req_id.replace('-', '_')}_{counter:03d}"
        counter += 1
        cases.append(TestCase(
            tc_id=tc_id,
            module=req.module,
            req_ref=req.req_id,
            title=f"Verificar flujo exitoso principal para {req.title}",
            description=f"Validar que el usuario o sistema completa el flujo con datos válidos según especificación ({req.title}).",
            test_type="Funcional",
            technique="Partición de Equivalencia (Clase Válida)",
            level="Sistema / UAT",
            priority="Alta (P1)",
            preconditions=f"El sistema se encuentra operativo y el usuario dispone de credenciales/permisos válidos para el módulo {req.module}.",
            steps=(
                f"1. Acceder a la interfaz o endpoint de {req.title}.\n"
                f"2. Ingresar todos los campos obligatorios con valores válidos y dentro de especificación.\n"
                f"3. Confirmar la acción presionando el botón de envío o confirmación.\n"
                f"4. Verificar la respuesta del sistema y la persistencia de datos."
            ),
            test_data="Conjunto de datos válidos estándar según modelo de negocio.",
            expected_result=(
                f"La operación se completa satisfactoriamente. El sistema muestra mensaje de éxito "
                f"o confirmación y actualiza el estado correspondiente sin errores."
            ),
            postconditions="Los datos quedan correctamente registrados en la base de datos y la sesión se mantiene estable.",
            status="No Ejecutado"
        ))

        # ---------------------------------------------------------------------
        # 2. VALIDACIÓN DE CAMPOS OBLIGATORIOS (Partición de Equivalencia - Inválida)
        # ---------------------------------------------------------------------
        tc_id = f"TC_{req.req_id.replace('-', '_')}_{counter:03d}"
        counter += 1
        cases.append(TestCase(
            tc_id=tc_id,
            module=req.module,
            req_ref=req.req_id,
            title=f"Validar rechazo al enviar formulario con campos requeridos vacíos en {req.title}",
            description=f"Comprobar que el sistema previene el envío cuando faltan datos obligatorios y muestra los mensajes de error adecuados.",
            test_type="Funcional / Validación",
            technique="Partición de Equivalencia (Clase Inválida)",
            level="Sistema",
            priority="Alta (P1)",
            preconditions=f"El usuario se encuentra en el formulario o punto de entrada de {req.title}.",
            steps=(
                f"1. Dejar vacíos o en blanco los campos obligatorios.\n"
                f"2. Intentar someter el formulario o enviar la petición.\n"
                f"3. Inspeccionar el comportamiento de la interfaz y las alertas visuales."
            ),
            test_data="Campos requeridos: [NULL], [\"\"], espacios en blanco.",
            expected_result=(
                f"El sistema no procesa la solicitud. Se resaltan los campos obligatorios en color de advertencia "
                f"y se despliega un mensaje claro indicando que los campos son mandatorios."
            ),
            postconditions="No se almacena ningún registro incompleto ni se altera el estado del sistema.",
            status="No Ejecutado"
        ))

        # ---------------------------------------------------------------------
        # 3. ANÁLISIS DE VALORES LÍMITE (BVA - Boundary Value Analysis)
        # Detectar patrones numéricos, de longitud o fechas
        # ---------------------------------------------------------------------
        # Buscar límites explícitos tipo "mínimo X", "máximo Y", "entre X y Y", "longitud de X caracteres"
        bounds = re.findall(r'(?:m[ií]nimo|min)\s*(\d+)|(?:m[aá]ximo|max)\s*(\d+)|(?:entre|rango de)\s*(\d+)\s*(?:y|a)\s*(\d+)|(\d+)\s*(?:caracteres|carácteres|dígitos|letras|intentos|pesos|dólares|usd)', full_text)
        
        has_boundaries = bool(bounds) or any(k in full_text for k in ["longitud", "límite", "limite", "rango", "máximo", "mínimo", "caracteres"])

        if has_boundaries:
            # Caso Límite Mínimo
            tc_id = f"TC_{req.req_id.replace('-', '_')}_{counter:03d}"
            counter += 1
            cases.append(TestCase(
                tc_id=tc_id,
                module=req.module,
                req_ref=req.req_id,
                title=f"Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en {req.title}",
                description=f"Evaluar el comportamiento en los valores frontera inferiores según la técnica ISTQB BVA.",
                test_type="Funcional / Valores Límite",
                technique="Análisis de Valores Límite (BVA - Límite Inferior)",
                level="Sistema",
                priority="Media (P2)",
                preconditions=f"Pantalla de captura de datos habilitada para {req.title}.",
                steps=(
                    f"1. Ingresar un valor inmediatamente inferior al límite mínimo permitido (Min - 1).\n"
                    f"2. Intentar guardar y verificar mensaje de rechazo.\n"
                    f"3. Ingresar el valor exacto del límite mínimo permitido (Min).\n"
                    f"4. Guardar y verificar aceptación."
                ),
                test_data="Valor (Min - 1): Invalido | Valor (Min exacto): Válido",
                expected_result=(
                    f"El valor (Min - 1) es rechazado con mensaje específico de longitud/rango insuficiente. "
                    f"El valor (Min exacto) es aceptado correctamente."
                ),
                postconditions="Solo los datos dentro del umbral formal quedan registrados.",
                status="No Ejecutado"
            ))

            # Caso Límite Máximo
            tc_id = f"TC_{req.req_id.replace('-', '_')}_{counter:03d}"
            counter += 1
            cases.append(TestCase(
                tc_id=tc_id,
                module=req.module,
                req_ref=req.req_id,
                title=f"Validar límites superiores (Máximo exacto y Máximo + 1) en {req.title}",
                description=f"Evaluar el comportamiento en los valores frontera superiores según la técnica ISTQB BVA.",
                test_type="Funcional / Valores Límite",
                technique="Análisis de Valores Límite (BVA - Límite Superior)",
                level="Sistema",
                priority="Media (P2)",
                preconditions=f"Pantalla de captura de datos habilitada para {req.title}.",
                steps=(
                    f"1. Ingresar el valor exacto del límite superior permitido (Max).\n"
                    f"2. Guardar y verificar aceptación.\n"
                    f"3. Ingresar un valor inmediatamente superior al límite máximo permitido (Max + 1).\n"
                    f"4. Intentar guardar y verificar rechazo."
                ),
                test_data="Valor (Max exacto): Válido | Valor (Max + 1): Inválido / Excedido",
                expected_result=(
                    f"El valor exacto en el máximo es procesado con éxito. "
                    f"El valor que excede el máximo (Max + 1) es bloqueado con advertencia de límite superado."
                ),
                postconditions="El sistema trunca o rechaza el ingreso excesivo protegiendo la integridad de la base de datos.",
                status="No Ejecutado"
            ))

        # ---------------------------------------------------------------------
        # 4. TABLA DE DECISIÓN / COMBINATORIA DE REGLAS DE NEGOCIO
        # ---------------------------------------------------------------------
        if req.business_rules or "si " in full_text or "cuando " in full_text or "descuento" in full_text or "rol" in full_text or "condici" in full_text:
            tc_id = f"TC_{req.req_id.replace('-', '_')}_{counter:03d}"
            counter += 1
            rule_summary = req.business_rules[0] if req.business_rules else "Combinación de condiciones de negocio"
            cases.append(TestCase(
                tc_id=tc_id,
                module=req.module,
                req_ref=req.req_id,
                title=f"Validar combinatoria de reglas de negocio en {req.title}",
                description=f"Verificar que las decisiones lógicas y bifurcaciones del negocio se cumplan fielmente ({rule_summary}).",
                test_type="Reglas de Negocio / Lógica",
                technique="Pruebas de Tabla de Decisión (Decision Table)",
                level="Sistema / Integración",
                priority="Alta (P1)",
                preconditions="Configuración de parámetros y tablas maestras de negocio en estado inicial.",
                steps=(
                    f"1. Configurar Caso A: Condición 1 = Verdadero, Condición 2 = Falso -> Ejecutar acción.\n"
                    f"2. Configurar Caso B: Condición 1 = Falso, Condición 2 = Verdadero -> Ejecutar acción.\n"
                    f"3. Configurar Caso C: Ambas Condiciones = Verdadero -> Ejecutar acción.\n"
                    f"4. Contrastar cada resultado obtenido contra la matriz de decisiones."
                ),
                test_data="Matriz combinatoria de estados booleanos de entrada según reglas de negocio.",
                expected_result=(
                    f"Cada combinación produce exactamente el resultado previsto en la regla de negocio, "
                    f"sin inconsistencias ni aprobaciones no autorizadas."
                ),
                postconditions="Los registros de auditoría reflejan las decisiones de negocio aplicadas.",
                status="No Ejecutado"
            ))

        # ---------------------------------------------------------------------
        # 5. TRANSICIÓN DE ESTADOS (State Transition)
        # ---------------------------------------------------------------------
        state_keywords = ["estado", "status", "activo", "inactivo", "bloqueado", "cancelado", "aprobado", "pendiente", "intentos", "login"]
        if any(k in full_text for k in state_keywords):
            tc_id = f"TC_{req.req_id.replace('-', '_')}_{counter:03d}"
            counter += 1
            cases.append(TestCase(
                tc_id=tc_id,
                module=req.module,
                req_ref=req.req_id,
                title=f"Validar ciclo de vida y transición de estados en {req.title}",
                description=f"Comprobar las transiciones válidas e inválidas entre los estados del registro o entidad.",
                test_type="Funcional / Ciclo de Vida",
                technique="Pruebas de Transición de Estados (State Transition)",
                level="Sistema",
                priority="Media (P2)",
                preconditions="Entidad creada en su estado inicial (ej. Pendiente / Activo / Borrador).",
                steps=(
                    f"1. Provocar el evento de transición válida (ej. Aprobar / Bloquear / Procesar).\n"
                    f"2. Verificar que el estado cambie al nuevo estado esperado.\n"
                    f"3. Intentar forzar una transición inválida (ej. de Cancelado a Activo sin reactivación).\n"
                    f"4. Observar que el sistema bloquee la transición prohibida."
                ),
                test_data="Secuencia de eventos y transiciones del ciclo de vida.",
                expected_result=(
                    f"Las transiciones legítimas se efectúan registrando hora y usuario responsable. "
                    f"Las transiciones ilegítimas son rechazadas por la máquina de estados."
                ),
                postconditions="El estado final de la entidad coincide estrictamente con el diagrama de estados.",
                status="No Ejecutado"
            ))

        # ---------------------------------------------------------------------
        # 6. ADIVINACIÓN DE ERRORES / SEGURIDAD / ROBUSTEZ (Error Guessing)
        # ---------------------------------------------------------------------
        tc_id = f"TC_{req.req_id.replace('-', '_')}_{counter:03d}"
        counter += 1
        cases.append(TestCase(
            tc_id=tc_id,
            module=req.module,
            req_ref=req.req_id,
            title=f"Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas en {req.title}",
            description=f"Evaluar la robustez del módulo frente a datos malformados, caracteres no ASCII o scripts maliciosos (XSS/SQLi).",
            test_type="Seguridad / Robustez",
            technique="Adivinación de Errores (Error Guessing)",
            level="Sistema / Seguridad",
            priority="Alta (P1)",
            preconditions="Módulo expuesto y accesible para recepción de datos.",
            steps=(
                f"1. Ingresar en campos de texto payloads tipo: `<script>alert('QA')</script>` o `' OR '1'='1`.\n"
                f"2. Enviar cadenas con emojis, tildes, caracteres UTF-8 complejos y saltos de línea inesperados.\n"
                f"3. Realizar doble clic rápido o envíos concurrentes sobre el botón de acción.\n"
                f"4. Verificar manejo de excepciones y ausencia de pantallas de error tipo stack trace (HTTP 500)."
            ),
            test_data="Strings: <script>alert(1)</script>, \"; DROP TABLE users; --, ñÑáéíóú, 🚀🔥",
            expected_result=(
                f"El sistema sanitiza las entradas o las rechaza limpiamente con mensajes controlados. "
                f"No se produce ejecución de script en el cliente, ni fallos en consultas SQL, ni caída 500 del servidor."
            ),
            postconditions="La base de datos permanece íntegra sin inyecciones ni registros corruptos.",
            status="No Ejecutado"
        ))

        # ---------------------------------------------------------------------
        # 7. CASOS ESPECÍFICOS SEGÚN CRITERIOS DE ACEPTACIÓN ADICIONALES
        # ---------------------------------------------------------------------
        for crit_idx, crit in enumerate(req.acceptance_criteria):
            if len(cases) >= 8:
                break  # Evitar sobrecarga si ya hay suficientes casos por requisito
            if any(k in crit.lower() for k in ["mensaje", "notificaci", "correo", "email", "alerta", "tiempo"]):
                tc_id = f"TC_{req.req_id.replace('-', '_')}_{counter:03d}"
                counter += 1
                cases.append(TestCase(
                    tc_id=tc_id,
                    module=req.module,
                    req_ref=req.req_id,
                    title=f"Verificar criterio: {crit[:60]}... en {req.title}",
                    description=f"Comprobar el cumplimiento del criterio de aceptación: {crit}",
                    test_type="Funcional / Criterio de Aceptación",
                    technique="Pruebas Basadas en Casos de Uso (Use Case Testing)",
                    level="Sistema / UAT",
                    priority="Media (P2)",
                    preconditions="Entorno con servicios de notificación y mensajería habilitados.",
                    steps=(
                        f"1. Ejecutar el flujo del usuario que dispara la condición: '{crit}'.\n"
                        f"2. Monitorear la salida visual, correo o mensaje generado.\n"
                        f"3. Validar contenido, redacción y tiempo de respuesta."
                    ),
                    test_data="Parámetros asociados al criterio de aceptación específico.",
                    expected_result=f"El sistema satisface íntegramente el criterio: {crit}",
                    postconditions="Registro de eventos/notificaciones creado exitosamente.",
                    status="No Ejecutado"
                ))

        return cases


# =============================================================================
# GENERADOR PROFESIONAL DE EXCEL ISTQB
# =============================================================================

class ExcelISTQBExporter:
    """
    Construye un libro de cálculo profesional (.xlsx) con:
    1. Portada / Resumen Ejecutivo con KPIs y Métricas ISTQB
    2. Hoja de Casos de Prueba ISTQB detallada con formato corporativo y validaciones
    3. Matriz de Trazabilidad de Requisitos (RTM)
    """

    # Paleta de Colores Corporativa
    COLOR_PRIMARY = "1B365D"       # Azul Marino Profundo (Headers)
    COLOR_SECONDARY = "2E5B88"     # Azul Medio (Subheaders)
    COLOR_ACCENT = "00A88F"        # Teal / Verde corporativo
    COLOR_BG_LIGHT = "F8FAFC"      # Gris ultra claro para filas alternas
    COLOR_BORDER = "CBD5E1"        # Borde suave
    COLOR_WHITE = "FFFFFF"

    # Colores de Prioridad
    COLOR_PRIO_HIGH_BG = "FEE2E2"
    COLOR_PRIO_HIGH_FG = "991B1B"
    COLOR_PRIO_MED_BG = "FEF3C7"
    COLOR_PRIO_MED_FG = "92400E"
    COLOR_PRIO_LOW_BG = "DCFCE7"
    COLOR_PRIO_LOW_FG = "166534"

    @classmethod
    def export(cls, requirements: List[Requirement], test_cases: List[TestCase], output_path: str):
        wb = openpyxl.Workbook()
        
        # Eliminar hoja default
        wb.remove(wb.active)

        # 1. Crear Hoja de Resumen / Dashboard
        cls._build_dashboard_sheet(wb, requirements, test_cases)

        # 2. Crear Hoja de Casos de Prueba
        cls._build_test_cases_sheet(wb, test_cases)

        # 3. Crear Hoja de Matriz de Trazabilidad (RTM)
        cls._build_rtm_sheet(wb, requirements, test_cases)

        # Guardar libro
        wb.save(output_path)
        print(f"[OK] Archivo Excel generado con éxito en: {output_path}")

    @classmethod
    def _build_dashboard_sheet(cls, wb: openpyxl.Workbook, reqs: List[Requirement], cases: List[TestCase]):
        ws = wb.create_sheet(title="Resumen Ejecutivo ISTQB")
        ws.views.sheetView[0].showGridLines = True

        # Header Banner
        ws.merge_cells("B2:J3")
        banner = ws["B2"]
        banner.value = "INFORME EJECUTIVO DE DISEÑO DE PRUEBAS - METODOLOGÍA ISTQB"
        banner.font = Font(name="Calibri", size=16, bold=True, color=cls.COLOR_WHITE)
        banner.fill = PatternFill(start_color=cls.COLOR_PRIMARY, end_color=cls.COLOR_PRIMARY, fill_type="solid")
        banner.alignment = Alignment(horizontal="center", vertical="center")

        # Subtítulo / Metadata
        ws["B4"] = "Estándar de Pruebas:"
        ws["C4"] = "ISTQB CTFL v4.0 / ISO/IEC/IEEE 29119"
        ws["B5"] = "Fecha de Generación:"
        ws["C5"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ws["B6"] = "Rol Responsable:"
        ws["C6"] = "Agente QA Senior / Test Design Architect"
        ws["B7"] = "Estado del Plan:"
        ws["C7"] = "Casos Listos para Ejecución (Baseline)"

        for row in range(4, 8):
            ws[f"B{row}"].font = Font(name="Calibri", size=10, bold=True, color="334155")
            ws[f"C{row}"].font = Font(name="Calibri", size=10, color="0F172A")

        # KPI Cards (Cajas de resumen)
        total_cases = len(cases)
        total_reqs = len(reqs)
        prio_high = sum(1 for c in cases if "Alta" in c.priority)
        prio_med = sum(1 for c in cases if "Media" in c.priority)
        prio_low = sum(1 for c in cases if "Baja" in c.priority)

        kpis = [
            ("TOTAL CASOS", total_cases, "B9:C10", cls.COLOR_PRIMARY),
            ("REQUERIMIENTOS", total_reqs, "D9:E10", cls.COLOR_SECONDARY),
            ("PRIORIDAD ALTA", prio_high, "F9:G10", "B91C1C"),
            ("PRIORIDAD MEDIA", prio_med, "H9:I10", "D97706"),
            ("PRIORIDAD BAJA", prio_low, "J9:K10", "059669"),
        ]

        for title, value, rng, color in kpis:
            start_cell = rng.split(":")[0]
            ws.merge_cells(rng)
            c = ws[start_cell]
            c.value = f"{title}\n{value}"
            c.font = Font(name="Calibri", size=12, bold=True, color=cls.COLOR_WHITE)
            c.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

        # Tabla 1: Desglose por Técnica ISTQB
        techniques = {}
        for c in cases:
            techniques[c.technique] = techniques.get(c.technique, 0) + 1

        ws["B12"] = "Desglose por Técnica de Diseño ISTQB"
        ws["B12"].font = Font(name="Calibri", size=12, bold=True, color=cls.COLOR_PRIMARY)
        
        ws["B13"] = "Técnica de Prueba ISTQB"
        ws["C13"] = "Cantidad"
        ws["D13"] = "% Cobertura"
        for col in ["B13", "C13", "D13"]:
            ws[col].font = Font(name="Calibri", size=10, bold=True, color=cls.COLOR_WHITE)
            ws[col].fill = PatternFill(start_color=cls.COLOR_SECONDARY, end_color=cls.COLOR_SECONDARY, fill_type="solid")
            ws[col].alignment = Alignment(horizontal="center", vertical="center")

        curr_row = 14
        thin_border = Border(
            left=Side(style='thin', color=cls.COLOR_BORDER),
            right=Side(style='thin', color=cls.COLOR_BORDER),
            top=Side(style='thin', color=cls.COLOR_BORDER),
            bottom=Side(style='thin', color=cls.COLOR_BORDER)
        )

        for tech, count in techniques.items():
            pct = (count / total_cases) * 100 if total_cases > 0 else 0
            ws[f"B{curr_row}"] = tech
            ws[f"C{curr_row}"] = count
            ws[f"D{curr_row}"] = f"{pct:.1f}%"

            ws[f"B{curr_row}"].font = Font(name="Calibri", size=10)
            ws[f"C{curr_row}"].font = Font(name="Calibri", size=10)
            ws[f"D{curr_row}"].font = Font(name="Calibri", size=10)

            ws[f"C{curr_row}"].alignment = Alignment(horizontal="center")
            ws[f"D{curr_row}"].alignment = Alignment(horizontal="center")

            for col_letter in ["B", "C", "D"]:
                ws[f"{col_letter}{curr_row}"].border = thin_border
            curr_row += 1

        # Tabla 2: Desglose por Tipo de Prueba
        types_count = {}
        for c in cases:
            types_count[c.test_type] = types_count.get(c.test_type, 0) + 1

        ws["F12"] = "Desglose por Tipo de Prueba"
        ws["F12"].font = Font(name="Calibri", size=12, bold=True, color=cls.COLOR_PRIMARY)

        ws["F13"] = "Tipo de Prueba"
        ws["G13"] = "Cantidad"
        ws["H13"] = "% Total"
        for col in ["F13", "G13", "H13"]:
            ws[col].font = Font(name="Calibri", size=10, bold=True, color=cls.COLOR_WHITE)
            ws[col].fill = PatternFill(start_color=cls.COLOR_SECONDARY, end_color=cls.COLOR_SECONDARY, fill_type="solid")
            ws[col].alignment = Alignment(horizontal="center", vertical="center")

        curr_row_type = 14
        for t_name, count in types_count.items():
            pct = (count / total_cases) * 100 if total_cases > 0 else 0
            ws[f"F{curr_row_type}"] = t_name
            ws[f"G{curr_row_type}"] = count
            ws[f"H{curr_row_type}"] = f"{pct:.1f}%"

            ws[f"F{curr_row_type}"].font = Font(name="Calibri", size=10)
            ws[f"G{curr_row_type}"].font = Font(name="Calibri", size=10)
            ws[f"H{curr_row_type}"].font = Font(name="Calibri", size=10)

            ws[f"G{curr_row_type}"].alignment = Alignment(horizontal="center")
            ws[f"H{curr_row_type}"].alignment = Alignment(horizontal="center")

            for col_letter in ["F", "G", "H"]:
                ws[f"{col_letter}{curr_row_type}"].border = thin_border
            curr_row_type += 1

        # Ajuste de ancho de columnas
        ws.column_dimensions["A"].width = 4
        ws.column_dimensions["B"].width = 38
        ws.column_dimensions["C"].width = 15
        ws.column_dimensions["D"].width = 15
        ws.column_dimensions["E"].width = 4
        ws.column_dimensions["F"].width = 32
        ws.column_dimensions["G"].width = 14
        ws.column_dimensions["H"].width = 14
        ws.column_dimensions["I"].width = 14
        ws.column_dimensions["J"].width = 14
        ws.column_dimensions["K"].width = 14

    @classmethod
    def _build_test_cases_sheet(cls, wb: openpyxl.Workbook, cases: List[TestCase]):
        ws = wb.create_sheet(title="Casos de Prueba ISTQB")
        ws.views.sheetView[0].showGridLines = True

        headers = [
            ("ID Caso", 14),
            ("Módulo", 22),
            ("Ref. Requisito", 16),
            ("Título del Caso de Prueba", 36),
            ("Objetivo / Descripción", 34),
            ("Tipo de Prueba", 18),
            ("Técnica ISTQB", 28),
            ("Nivel", 15),
            ("Prioridad", 14),
            ("Precondiciones", 30),
            ("Pasos de Prueba (Paso a Paso)", 45),
            ("Datos de Prueba", 28),
            ("Resultado Esperado", 40),
            ("Postcondiciones", 26),
            ("Estado", 16),
            ("Ejecutado Por", 18),
            ("Fecha Ejecución", 16),
            ("ID Defecto / Observaciones", 28)
        ]

        header_font = Font(name="Calibri", size=11, bold=True, color=cls.COLOR_WHITE)
        header_fill = PatternFill(start_color=cls.COLOR_PRIMARY, end_color=cls.COLOR_PRIMARY, fill_type="solid")
        header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

        border_side = Side(style='thin', color=cls.COLOR_BORDER)
        cell_border = Border(left=border_side, right=border_side, top=border_side, bottom=border_side)

        # Escribir Cabecera
        for col_idx, (header_text, width) in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col_idx, value=header_text)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_align
            cell.border = cell_border
            col_letter = get_column_letter(col_idx)
            ws.column_dimensions[col_letter].width = width

        ws.row_dimensions[1].height = 32

        # Data Validation para Estado
        dv_status = DataValidation(
            type="list",
            formula1='"No Ejecutado,Pasó,Falló,Bloqueado,Omitido"',
            allow_blank=True,
            errorTitle="Estado Inválido",
            error="Seleccione un estado de la lista: No Ejecutado, Pasó, Falló, Bloqueado, Omitido."
        )
        ws.add_data_validation(dv_status)

        # Escribir Filas de Datos
        for row_idx, tc in enumerate(cases, 2):
            is_even = (row_idx % 2 == 0)
            row_fill = PatternFill(
                start_color=cls.COLOR_WHITE if is_even else cls.COLOR_BG_LIGHT,
                end_color=cls.COLOR_WHITE if is_even else cls.COLOR_BG_LIGHT,
                fill_type="solid"
            )

            data_row = [
                tc.tc_id,
                tc.module,
                tc.req_ref,
                tc.title,
                tc.description,
                tc.test_type,
                tc.technique,
                tc.level,
                tc.priority,
                tc.preconditions,
                tc.steps,
                tc.test_data,
                tc.expected_result,
                tc.postconditions,
                tc.status,
                tc.executed_by,
                tc.execution_date,
                tc.defect_notes
            ]

            for col_idx, val in enumerate(data_row, 1):
                cell = ws.cell(row=row_idx, column=col_idx, value=val)
                cell.font = Font(name="Calibri", size=10)
                cell.border = cell_border
                cell.fill = row_fill

                # Alineación según columna
                if col_idx in [1, 3, 6, 8, 9, 15, 17]:
                    cell.alignment = Alignment(horizontal="center", vertical="top")
                else:
                    cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

                # Resaltado de Prioridad
                if col_idx == 9:  # Prioridad
                    if "Alta" in str(val):
                        cell.fill = PatternFill(start_color=cls.COLOR_PRIO_HIGH_BG, end_color=cls.COLOR_PRIO_HIGH_BG, fill_type="solid")
                        cell.font = Font(name="Calibri", size=10, bold=True, color=cls.COLOR_PRIO_HIGH_FG)
                    elif "Media" in str(val):
                        cell.fill = PatternFill(start_color=cls.COLOR_PRIO_MED_BG, end_color=cls.COLOR_PRIO_MED_BG, fill_type="solid")
                        cell.font = Font(name="Calibri", size=10, bold=True, color=cls.COLOR_PRIO_MED_FG)
                    elif "Baja" in str(val):
                        cell.fill = PatternFill(start_color=cls.COLOR_PRIO_LOW_BG, end_color=cls.COLOR_PRIO_LOW_BG, fill_type="solid")
                        cell.font = Font(name="Calibri", size=10, bold=True, color=cls.COLOR_PRIO_LOW_FG)

                # Formato en Estado
                if col_idx == 15:  # Estado
                    dv_status.add(cell)

            ws.row_dimensions[row_idx].height = 42

        # Auto-filter
        max_col_letter = get_column_letter(len(headers))
        ws.auto_filter.ref = f"A1:{max_col_letter}{len(cases) + 1}"

    @classmethod
    def _build_rtm_sheet(cls, wb: openpyxl.Workbook, reqs: List[Requirement], cases: List[TestCase]):
        ws = wb.create_sheet(title="Matriz de Trazabilidad (RTM)")
        ws.views.sheetView[0].showGridLines = True

        headers = [
            ("ID Requisito", 16),
            ("Módulo", 22),
            ("Nombre / Título del Requerimiento", 35),
            ("Casos de Prueba Asociados (IDs)", 38),
            ("Cantidad de Casos", 18),
            ("Técnicas ISTQB Cubiertas", 35),
            ("Estado Cobertura", 18)
        ]

        header_font = Font(name="Calibri", size=11, bold=True, color=cls.COLOR_WHITE)
        header_fill = PatternFill(start_color=cls.COLOR_PRIMARY, end_color=cls.COLOR_PRIMARY, fill_type="solid")
        header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

        border_side = Side(style='thin', color=cls.COLOR_BORDER)
        cell_border = Border(left=border_side, right=border_side, top=border_side, bottom=border_side)

        for col_idx, (header_text, width) in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col_idx, value=header_text)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_align
            cell.border = cell_border
            col_letter = get_column_letter(col_idx)
            ws.column_dimensions[col_letter].width = width

        ws.row_dimensions[1].height = 30

        # Mapeo de casos por requerimiento
        req_cases_map: Dict[str, List[TestCase]] = {}
        for c in cases:
            req_cases_map.setdefault(c.req_ref, []).append(c)

        for row_idx, req in enumerate(reqs, 2):
            matched_cases = req_cases_map.get(req.req_id, [])
            tc_ids_str = ", ".join([c.tc_id for c in matched_cases]) if matched_cases else "SIN COBERTURA"
            count = len(matched_cases)
            techs = ", ".join(list(set([c.technique.split('(')[0].strip() for c in matched_cases])))
            status_cov = "Cubierto (100%)" if count >= 3 else ("Parcial" if count > 0 else "No Cubierto")

            is_even = (row_idx % 2 == 0)
            row_fill = PatternFill(
                start_color=cls.COLOR_WHITE if is_even else cls.COLOR_BG_LIGHT,
                end_color=cls.COLOR_WHITE if is_even else cls.COLOR_BG_LIGHT,
                fill_type="solid"
            )

            row_data = [
                req.req_id,
                req.module,
                req.title,
                tc_ids_str,
                count,
                techs,
                status_cov
            ]

            for col_idx, val in enumerate(row_data, 1):
                cell = ws.cell(row=row_idx, column=col_idx, value=val)
                cell.font = Font(name="Calibri", size=10)
                cell.border = cell_border
                cell.fill = row_fill

                if col_idx in [1, 5, 7]:
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                else:
                    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

                if col_idx == 7:
                    if "Cubierto" in status_cov:
                        cell.fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
                        cell.font = Font(name="Calibri", size=10, bold=True, color="166534")
                    else:
                        cell.fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
                        cell.font = Font(name="Calibri", size=10, bold=True, color="991B1B")

            ws.row_dimensions[row_idx].height = 26

        max_col_letter = get_column_letter(len(headers))
        ws.auto_filter.ref = f"A1:{max_col_letter}{len(reqs) + 1}"


# =============================================================================
# CLI Y PUNTO DE ENTRADA DEL AGENTE
# =============================================================================

def run_qa_agent(input_file: str, output_file: str):
    print("=" * 70)
    print("AGENTE QA ISTQB - ANÁLISIS DE REQUERIMIENTOS Y DISEÑO DE PRUEBAS")
    print("=" * 70)
    print(f"[*] Leyendo archivo de requerimientos: {input_file}")
    
    requirements = RequirementParser.parse_file(input_file)
    print(f"[+] Requerimientos detectados e interpretados: {len(requirements)}")
    for r in requirements:
        print(f"    - [{r.req_id}] ({r.module}): {r.title}")

    print("\n[*] Aplicando técnicas formales de diseño ISTQB...")
    print("    * Partición de Equivalencia (Clases Válidas e Inválidas)")
    print("    * Análisis de Valores Límite (BVA)")
    print("    * Tablas de Decisión / Reglas de Negocio")
    print("    * Transición de Estados")
    print("    * Adivinación de Errores y Robustez")

    test_cases = ISTQBTestGenerator.generate_test_cases(requirements)
    print(f"[+] Total de Casos de Prueba generados: {len(test_cases)}")

    print(f"\n[*] Exportando a formato Excel corporativo ISTQB: {output_file}")
    ExcelISTQBExporter.export(requirements, test_cases, output_file)

    print("\n" + "=" * 70)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print(f"Archivo Excel disponible en: {os.path.abspath(output_file)}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Agente QA ISTQB: Analiza requerimientos y genera casos de prueba en Excel (.xlsx)"
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Ruta al archivo de requerimientos (.md, .txt, .json)"
    )
    parser.add_argument(
        "-o", "--output",
        default="Casos_de_Prueba_ISTQB.xlsx",
        help="Ruta del archivo Excel de salida (default: Casos_de_Prueba_ISTQB.xlsx)"
    )

    args = parser.parse_args()
    run_qa_agent(args.input, args.output)


if __name__ == "__main__":
    main()
