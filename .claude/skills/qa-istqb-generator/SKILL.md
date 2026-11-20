---
name: qa-istqb-generator
description: Agente y skill QA especializado en análisis de especificaciones de requerimientos (funcionales, historias de usuario, reglas de negocio), diseño exhaustivo de casos de prueba bajo el estándar ISTQB (International Software Testing Qualifications Board) y exportación directa a un libro de cálculo Excel (.xlsx) estructurado profesionalmente.
---

# QA ISTQB Test Case Generator & Analyst

Este agente está diseñado para actuar como un QA Lead / Test Analyst certificado por ISTQB (CTFL v4.0 / ISO/IEC/IEEE 29119). Su función es transformar especificaciones de requerimientos en suites completas de casos de prueba listos para ejecución y seguimiento en Microsoft Excel.

## Capacidades y Técnicas Aplicadas

El agente aplica sistemáticamente las técnicas de caja negra definidas por ISTQB:
1. **Partición de Equivalencia (Equivalence Partitioning):**
   - Cobertura de clases de equivalencia válidas (caminos felices / happy paths).
   - Cobertura de clases de equivalencia inválidas (campos obligatorios vacíos, formatos erróneos, longitudes inadecuadas).
2. **Análisis de Valores Límite (Boundary Value Analysis - BVA):**
   - Valores en frontera mínima (Mínimo, Mínimo - 1).
   - Valores en frontera máxima (Máximo, Máximo + 1).
3. **Pruebas de Tablas de Decisión (Decision Table Testing):**
   - Combinatoria de condiciones booleanas, reglas de negocio cruzadas y promociones/descuentos.
4. **Pruebas de Transición de Estados (State Transition Testing):**
   - Eventos de activación, bloqueo de cuentas, cancelación, cambios de ciclo de vida.
5. **Adivinación de Errores y Seguridad (Error Guessing):**
   - Inyección de caracteres especiales, scripts maliciosos (XSS, SQLi), clics repetidos, timeout y concurrencia.

---

## Estructura del Libro de Cálculo Excel Generado

El documento Excel resultante cuenta con 3 hojas de trabajo corporativas:

### 1. Resumen Ejecutivo ISTQB (Dashboard)
- Banner corporativo con metadatos (fecha, autor, estándar, estado).
- Tarjetas de KPIs (Total de Casos, Total Requerimientos, Casos por Prioridad: Alta P1, Media P2, Baja P3).
- Tablas de distribución por Técnica ISTQB y por Tipo de Prueba con cálculo de porcentajes.

### 2. Casos de Prueba ISTQB
Contiene 18 columnas estandarizadas:
- `ID Caso` (ej. `TC_RF_001_001`)
- `Módulo`
- `Ref. Requisito` (Trazabilidad)
- `Título del Caso de Prueba`
- `Objetivo / Descripción`
- `Tipo de Prueba`
- `Técnica ISTQB`
- `Nivel` (Componente, Integración, Sistema, UAT)
- `Prioridad` (Formato condicional: P1 Rojo, P2 Amarillo, P3 Verde)
- `Precondiciones`
- `Pasos de Prueba (Paso a Paso)` (Secuencia numerada con saltos de línea legibles)
- `Datos de Prueba`
- `Resultado Esperado`
- `Postcondiciones`
- `Estado` (Dropdown interactivo: `No Ejecutado`, `Pasó`, `Falló`, `Bloqueado`, `Omitido`)
- `Ejecutado Por`
- `Fecha Ejecución`
- `ID Defecto / Observaciones`

### 3. Matriz de Trazabilidad de Requisitos (RTM)
- Mapeo bidireccional entre Requisitos / HU y Casos de Prueba asociados.
- Indicador visual de porcentaje de cobertura (100% Cubierto).

---

## Modo de Uso desde CLI

```powershell
# Analizar requerimientos y generar archivo Excel
python qa_agent.py --input <archivo_requerimientos.md|txt|json> --output <archivo_salida.xlsx>
```

