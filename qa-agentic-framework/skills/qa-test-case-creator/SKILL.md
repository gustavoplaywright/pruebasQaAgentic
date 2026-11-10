---
name: qa-test-case-creator
description: Analiza historias de usuario, requerimientos funcionales o criterios de aceptación para generar matrices de casos de prueba exhaustivas (manuales y funcionales).
---

# QA Test Case Creator

## Propósito
Transformar especificaciones funcionales y criterios de aceptación en un conjunto estructurado, exhaustivo y determinista de casos de prueba.

## Entradas Requeridas
- Historia de Usuario (US) o Requerimiento Funcional.
- Criterios de Aceptación (formato Gherkin o texto plano).
- Reglas de Negocio específicas (si aplican).

## Estrategia de Cobertura
Al procesar la entrada, generar casuística dividida en:
1. **Flujo Principal (Happy Path):** Escenarios de éxito y operación estándar.
2. **Flujos Alternativos / Negativos:** Validaciones de campos, datos inválidos, errores de sistema.
3. **Casos de Borde (Edge Cases):** Valores límite, caracteres especiales, campos vacíos/nulos.
4. **Seguridad y Roles (si aplica):** Accesos no autorizados y permisos.

## Formato de Salida

| ID | Título | Tipo | Precondiciones | Pasos de Ejecución | Datos de Prueba | Resultado Esperado | Prioridad |
|---|---|---|---|---|---|---|---|
| TC-[MOD]-001 | [Título descriptivo] | Happy Path / Negativo / Edge | [Precondición] | 1. Paso 1<br>2. Paso 2 | [Parámetros] | [Resultado esperado] | Alta / Media / Baja |

## Reglas de Ejecución
- Mantener pasos atómicos y deterministas.
- Utilizar una nomenclatura clara para los IDs (ej. `TC-AUTH-001`).
- Asegurar que no existan ambigüedades en las precondiciones ni en los resultados esperados.