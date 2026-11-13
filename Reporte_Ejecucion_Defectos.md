# Informe Ejecutivo de Ejecución de Pruebas y Gestión de Defectos

**Fecha y Hora de Ejecución:** 2026-11-02 20:30:52  
**Motor de Pruebas:** Playwright E2E Runner (TypeScript)  
**Agente Responsable:** Agente QA Test Runner & Defect Analyst  

---

## 📊 Métricas Globales de Calidad (KPIs)

| Métrica | Valor | Indicador |
|---|---|---|
| **Total de Pruebas Ejecutadas** | `29` | 🏁 |
| **Pruebas Exitosas (Passed)** | `3` | 🟢 |
| **Pruebas Fallidas (Failed)** | `26` | 🔴 |
| **Tasa de Aprobación (Pass Rate)** | **`10.3%`** | ⚠️ |
| **Tiempo Total de Ejecución** | `46.95 s` | ⏱️ |
| **Defectos Registrados (Bugs)** | `26` | 🐞 |

---

## 🔍 Resumen por Módulo y Estado de Ejecución

| ID Caso ISTQB | Título de la Prueba | Estado | Duración | Causa Raíz / Observación |
|---|---|---|---|---|
| `TC_RF_001_001` | TC_RF_001_001: [@P1] Verificar flujo exitoso principal para  | **🔴 Falló** | `3754 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_001_002` | TC_RF_001_002: [@P1] Validar rechazo al enviar formulario co | **🔴 Falló** | `3797 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_001_003` | TC_RF_001_003: [@P2] Validar límites inferiores (Mínimo - 1  | **🔴 Falló** | `2921 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_001_004` | TC_RF_001_004: [@P2] Validar límites superiores (Máximo exac | **🔴 Falló** | `2929 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_001_005` | TC_RF_001_005: [@P1] Validar combinatoria de reglas de negoc | **🔴 Falló** | `1668 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_001_006` | TC_RF_001_006: [@P1] Verificar resistencia a inyecciones, ca | **🔴 Falló** | `1380 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_001_007` | TC_RF_001_007: [@P2] Verificar criterio: El usuario debe ing | **🔴 Falló** | `876 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_001_008` | TC_RF_001_008: [@P2] Verificar criterio: Al registrarse corr | **🔴 Falló** | `899 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_002_009` | TC_RF_002_009: [@P1] Verificar flujo exitoso principal para  | **🔴 Falló** | `753 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_002_010` | TC_RF_002_010: [@P1] Validar rechazo al enviar formulario co | **🔴 Falló** | `1328 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_002_011` | TC_RF_002_011: [@P2] Validar límites inferiores (Mínimo - 1  | **🔴 Falló** | `955 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_002_012` | TC_RF_002_012: [@P2] Validar límites superiores (Máximo exac | **🔴 Falló** | `997 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_002_013` | TC_RF_002_013: [@P1] Validar combinatoria de reglas de negoc | **🔴 Falló** | `811 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_002_014` | TC_RF_002_014: [@P2] Validar ciclo de vida y transición de e | **🔴 Falló** | `1202 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_002_015` | TC_RF_002_015: [@P1] Verificar resistencia a inyecciones, ca | **🔴 Falló** | `941 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_002_016` | TC_RF_002_016: [@P2] Verificar criterio: El usuario ingresa  | **🔴 Falló** | `1371 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_003_017` | TC_RF_003_017: [@P1] Verificar flujo exitoso principal para  | **🟢 Pasó** | `1855 ms` | OK (1855 ms) |
| `TC_RF_003_018` | TC_RF_003_018: [@P1] Validar rechazo al enviar formulario co | **🔴 Falló** | `6107 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_003_019` | TC_RF_003_019: [@P2] Validar límites inferiores (Mínimo - 1  | **🔴 Falló** | `941 ms` | ERROR GENÉRICO / DESCONOCIDO |
| `TC_RF_003_020` | TC_RF_003_020: [@P2] Validar límites superiores (Máximo exac | **🔴 Falló** | `1215 ms` | ERROR GENÉRICO / DESCONOCIDO |
| `TC_RF_003_021` | TC_RF_003_021: [@P1] Validar combinatoria de reglas de negoc | **🟢 Pasó** | `552 ms` | OK (552 ms) |
| `TC_RF_003_022` | TC_RF_003_022: [@P1] Verificar resistencia a inyecciones, ca | **🔴 Falló** | `456 ms` | ERROR GENÉRICO / DESCONOCIDO |
| `TC_RF_003_023` | TC_RF_003_023: [@P2] Verificar criterio: Si el cupón ha expi | **🔴 Falló** | `482 ms` | FALLO FUNCIONAL / ASERCIÓN |
| `TC_RF_004_024` | TC_RF_004_024: [@P1] Verificar flujo exitoso principal para  | **🟢 Pasó** | `614 ms` | OK (614 ms) |
| `TC_RF_004_025` | TC_RF_004_025: [@P1] Validar rechazo al enviar formulario co | **🔴 Falló** | `6168 ms` | TIMEOUT / RENDIMIENTO |
| `TC_RF_004_026` | TC_RF_004_026: [@P2] Validar límites inferiores (Mínimo - 1  | **🔴 Falló** | `547 ms` | ERROR GENÉRICO / DESCONOCIDO |
| `TC_RF_004_027` | TC_RF_004_027: [@P2] Validar límites superiores (Máximo exac | **🔴 Falló** | `459 ms` | ERROR GENÉRICO / DESCONOCIDO |
| `TC_RF_004_028` | TC_RF_004_028: [@P1] Verificar resistencia a inyecciones, ca | **🔴 Falló** | `472 ms` | ERROR GENÉRICO / DESCONOCIDO |
| `TC_RF_004_029` | TC_RF_004_029: [@P2] Verificar criterio: Al cargar un archiv | **🔴 Falló** | `496 ms` | ERROR GENÉRICO / DESCONOCIDO |

---

## 🐞 Registro Oficial de Defectos (Jira / GitHub Issues Ready)

### Ticket: [BUG-001] [TIMEOUT / RENDIMIENTO] Fallo en Verificar flujo exitoso principal para Registro de Nuevos Usuarios
- **ID Caso ISTQB Asociado:** `TC_RF_001_001`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Verificar flujo exitoso principal para Registro de Nuevos Usuarios.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-002] [TIMEOUT / RENDIMIENTO] Fallo en Validar rechazo al enviar formulario con campos requeridos vacíos en Registro de
- **ID Caso ISTQB Asociado:** `TC_RF_001_002`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar rechazo al enviar formulario con campos requeridos vacíos en Registro de Nuevos Usuarios.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-003] [TIMEOUT / RENDIMIENTO] Fallo en Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en Registro de Nuevos
- **ID Caso ISTQB Asociado:** `TC_RF_001_003`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en Registro de Nuevos Usuarios.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-004] [TIMEOUT / RENDIMIENTO] Fallo en Validar límites superiores (Máximo exacto y Máximo + 1) en Registro de Nuevos Us
- **ID Caso ISTQB Asociado:** `TC_RF_001_004`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar límites superiores (Máximo exacto y Máximo + 1) en Registro de Nuevos Usuarios.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-005] [TIMEOUT / RENDIMIENTO] Fallo en Validar combinatoria de reglas de negocio en Registro de Nuevos Usuarios
- **ID Caso ISTQB Asociado:** `TC_RF_001_005`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar combinatoria de reglas de negocio en Registro de Nuevos Usuarios.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-006] [TIMEOUT / RENDIMIENTO] Fallo en Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas e
- **ID Caso ISTQB Asociado:** `TC_RF_001_006`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas en Registro de Nuevos Usuarios.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-007] [TIMEOUT / RENDIMIENTO] Fallo en Verificar criterio: El usuario debe ingresar un correo electrónico con formato v
- **ID Caso ISTQB Asociado:** `TC_RF_001_007`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Verificar criterio: El usuario debe ingresar un correo electrónico con formato v... en Registro de Nuevos Usuarios.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-008] [TIMEOUT / RENDIMIENTO] Fallo en Verificar criterio: Al registrarse correctamente, el sistema debe enviar un corr
- **ID Caso ISTQB Asociado:** `TC_RF_001_008`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Verificar criterio: Al registrarse correctamente, el sistema debe enviar un corr... en Registro de Nuevos Usuarios.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-009] [TIMEOUT / RENDIMIENTO] Fallo en Verificar flujo exitoso principal para Inicio de Sesión y Bloqueo de Cuenta por 
- **ID Caso ISTQB Asociado:** `TC_RF_002_009`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Verificar flujo exitoso principal para Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-010] [TIMEOUT / RENDIMIENTO] Fallo en Validar rechazo al enviar formulario con campos requeridos vacíos en Inicio de S
- **ID Caso ISTQB Asociado:** `TC_RF_002_010`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar rechazo al enviar formulario con campos requeridos vacíos en Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-011] [TIMEOUT / RENDIMIENTO] Fallo en Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en Inicio de Sesión y
- **ID Caso ISTQB Asociado:** `TC_RF_002_011`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-012] [TIMEOUT / RENDIMIENTO] Fallo en Validar límites superiores (Máximo exacto y Máximo + 1) en Inicio de Sesión y Bl
- **ID Caso ISTQB Asociado:** `TC_RF_002_012`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar límites superiores (Máximo exacto y Máximo + 1) en Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-013] [TIMEOUT / RENDIMIENTO] Fallo en Validar combinatoria de reglas de negocio en Inicio de Sesión y Bloqueo de Cuent
- **ID Caso ISTQB Asociado:** `TC_RF_002_013`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar combinatoria de reglas de negocio en Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-014] [TIMEOUT / RENDIMIENTO] Fallo en Validar ciclo de vida y transición de estados en Inicio de Sesión y Bloqueo de C
- **ID Caso ISTQB Asociado:** `TC_RF_002_014`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Validar ciclo de vida y transición de estados en Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-015] [TIMEOUT / RENDIMIENTO] Fallo en Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas e
- **ID Caso ISTQB Asociado:** `TC_RF_002_015`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas en Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-016] [TIMEOUT / RENDIMIENTO] Fallo en Verificar criterio: El usuario ingresa correo y contraseña válidos y accede exit
- **ID Caso ISTQB Asociado:** `TC_RF_002_016`
- **Módulo:** Autenticación y Seguridad
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Autenticación y Seguridad).
2. Ejecutar la acción automatizada correspondiente a: Verificar criterio: El usuario ingresa correo y contraseña válidos y accede exit... en Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('headin

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('heading', { level: 1 })
Expected: visible
Error: strict mode violation: getByRole('heading', { level: 1 }) resolved to 2 elements:
    1) <h1>Iniciar Sesión / Registro</h1> aka getByRole('heading', { name: 'Iniciar Sesión / Registro' })
    2) <h1>Checkout y Cupones</h1> aka getByRole('heading', { name: 'Checkout y Cupones' })

Call log:
[2m  - Expect "toBeVisible" getByRole('heading',
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Autenticación y Seguridad. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-017] [TIMEOUT / RENDIMIENTO] Fallo en Validar rechazo al enviar formulario con campos requeridos vacíos en Aplicación 
- **ID Caso ISTQB Asociado:** `TC_RF_003_018`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Validar rechazo al enviar formulario con campos requeridos vacíos en Aplicación de Cupones de Descuento en Checkout.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i })
Expected: visible
T

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i })
Expected: visible
Timeout: 5000ms
Error: element(s) not found

Call log:
[2m  - Expect "toBeVisible" getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i }) with timeout 5000ms[22m
[2m  - waiting for getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i })[22m

    
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-018] [ERROR GENÉRICO / DESCONOCIDO] Fallo en Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en Aplicación de Cupo
- **ID Caso ISTQB Asociado:** `TC_RF_003_019`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `ERROR GENÉRICO / DESCONOCIDO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en Aplicación de Cupones de Descuento en Checkout.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [ERROR GENÉRICO / DESCONOCIDO]: TypeError: pageObject.fillCredentials is not a function

  47 |     // Precondición: Pantalla de captura de datos habilitada para Aplicación de Cupones de Descuento en Checkout.
  48 |     // 1. Proba

**Evidencia Técnica (Traceback):**
```text
TypeError: pageObject.fillCredentials is not a function
    at D:\workspace\agentic\playwright-suite\tests\carrito_de_compras_y_checkout.spec.ts:49:22
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: Excepción durante la ejecución de los pasos del test.

---
### Ticket: [BUG-019] [ERROR GENÉRICO / DESCONOCIDO] Fallo en Validar límites superiores (Máximo exacto y Máximo + 1) en Aplicación de Cupones
- **ID Caso ISTQB Asociado:** `TC_RF_003_020`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `ERROR GENÉRICO / DESCONOCIDO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Validar límites superiores (Máximo exacto y Máximo + 1) en Aplicación de Cupones de Descuento en Checkout.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [ERROR GENÉRICO / DESCONOCIDO]: TypeError: pageObject.fillCredentials is not a function

  63 |     // Precondición: Pantalla de captura de datos habilitada para Aplicación de Cupones de Descuento en Checkout.
  64 |     // 1. Proba

**Evidencia Técnica (Traceback):**
```text
TypeError: pageObject.fillCredentials is not a function
    at D:\workspace\agentic\playwright-suite\tests\carrito_de_compras_y_checkout.spec.ts:65:22
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: Excepción durante la ejecución de los pasos del test.

---
### Ticket: [BUG-020] [ERROR GENÉRICO / DESCONOCIDO] Fallo en Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas e
- **ID Caso ISTQB Asociado:** `TC_RF_003_022`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `ERROR GENÉRICO / DESCONOCIDO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas en Aplicación de Cupones de Descuento en Checkout.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [ERROR GENÉRICO / DESCONOCIDO]: TypeError: pageObject.fillCredentials is not a function

  92 |     // Precondición: Módulo expuesto y accesible para recepción de datos.
  93 |     // Prueba de robustez frente a XSS y SQL Injection


**Evidencia Técnica (Traceback):**
```text
TypeError: pageObject.fillCredentials is not a function
    at D:\workspace\agentic\playwright-suite\tests\carrito_de_compras_y_checkout.spec.ts:94:22
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: Excepción durante la ejecución de los pasos del test.

---
### Ticket: [BUG-021] [FALLO FUNCIONAL / ASERCIÓN] Fallo en Verificar criterio: Si el cupón ha expirado o no existe, se muestra el mensaje: 
- **ID Caso ISTQB Asociado:** `TC_RF_003_023`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `FALLO FUNCIONAL / ASERCIÓN`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Verificar criterio: Si el cupón ha expirado o no existe, se muestra el mensaje: ... en Aplicación de Cupones de Descuento en Checkout.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [FALLO FUNCIONAL / ASERCIÓN]: TypeError: pageObject.submit is not a function

  107 |     // Precondición: Entorno con servicios de notificación y mensajería habilitados.
  108 |     // Ejecución de flujo del caso de prueba
> 109 

**Evidencia Técnica (Traceback):**
```text
TypeError: pageObject.submit is not a function
    at D:\workspace\agentic\playwright-suite\tests\carrito_de_compras_y_checkout.spec.ts:109:22
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: Discrepancia entre el valor esperado por la regla de negocio y el valor real recibido en la interfaz. Indica un defecto funcional directo en la aplicación bajo prueba.

---
### Ticket: [BUG-022] [TIMEOUT / RENDIMIENTO] Fallo en Validar rechazo al enviar formulario con campos requeridos vacíos en Carga de Im
- **ID Caso ISTQB Asociado:** `TC_RF_004_025`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `TIMEOUT / RENDIMIENTO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Validar rechazo al enviar formulario con campos requeridos vacíos en Carga de Imagen de Perfil de Usuario.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [TIMEOUT / RENDIMIENTO]: Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i })
Expected: visible
T

**Evidencia Técnica (Traceback):**
```text
Error: [2mexpect([22m[31mlocator[39m[2m).[22mtoBeVisible[2m([22m[2m)[22m failed

Locator: getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i })
Expected: visible
Timeout: 5000ms
Error: element(s) not found

Call log:
[2m  - Expect "toBeVisible" getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i }) with timeout 5000ms[22m
[2m  - waiting for getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i })[22m

    
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: El tiempo límite de espera (timeout) de la acción o aserción fue excedido. Posible lentitud de respuesta en backend, red lenta o elemento que nunca llegó al estado interactivo.

---
### Ticket: [BUG-023] [ERROR GENÉRICO / DESCONOCIDO] Fallo en Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en Carga de Imagen de
- **ID Caso ISTQB Asociado:** `TC_RF_004_026`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `ERROR GENÉRICO / DESCONOCIDO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Validar límites inferiores (Mínimo - 1 e Inmediato Válido) en Carga de Imagen de Perfil de Usuario.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [ERROR GENÉRICO / DESCONOCIDO]: TypeError: pageObject.fillCredentials is not a function

  145 |     // Precondición: Pantalla de captura de datos habilitada para Carga de Imagen de Perfil de Usuario.
  146 |     // 1. Probar valor 

**Evidencia Técnica (Traceback):**
```text
TypeError: pageObject.fillCredentials is not a function
    at D:\workspace\agentic\playwright-suite\tests\carrito_de_compras_y_checkout.spec.ts:147:22
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: Excepción durante la ejecución de los pasos del test.

---
### Ticket: [BUG-024] [ERROR GENÉRICO / DESCONOCIDO] Fallo en Validar límites superiores (Máximo exacto y Máximo + 1) en Carga de Imagen de Pe
- **ID Caso ISTQB Asociado:** `TC_RF_004_027`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `ERROR GENÉRICO / DESCONOCIDO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Validar límites superiores (Máximo exacto y Máximo + 1) en Carga de Imagen de Perfil de Usuario.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [ERROR GENÉRICO / DESCONOCIDO]: TypeError: pageObject.fillCredentials is not a function

  161 |     // Precondición: Pantalla de captura de datos habilitada para Carga de Imagen de Perfil de Usuario.
  162 |     // 1. Probar valor 

**Evidencia Técnica (Traceback):**
```text
TypeError: pageObject.fillCredentials is not a function
    at D:\workspace\agentic\playwright-suite\tests\carrito_de_compras_y_checkout.spec.ts:163:22
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: Excepción durante la ejecución de los pasos del test.

---
### Ticket: [BUG-025] [ERROR GENÉRICO / DESCONOCIDO] Fallo en Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas e
- **ID Caso ISTQB Asociado:** `TC_RF_004_028`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Crítica (Critical / Blocker)` | **Prioridad:** `Alta`
- **Categoría de Causa Raíz:** `ERROR GENÉRICO / DESCONOCIDO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Verificar resistencia a inyecciones, caracteres especiales y entradas anómalas en Carga de Imagen de Perfil de Usuario.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [ERROR GENÉRICO / DESCONOCIDO]: TypeError: pageObject.fillCredentials is not a function

  177 |     // Precondición: Módulo expuesto y accesible para recepción de datos.
  178 |     // Prueba de robustez frente a XSS y SQL Injectio

**Evidencia Técnica (Traceback):**
```text
TypeError: pageObject.fillCredentials is not a function
    at D:\workspace\agentic\playwright-suite\tests\carrito_de_compras_y_checkout.spec.ts:179:22
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: Excepción durante la ejecución de los pasos del test.

---
### Ticket: [BUG-026] [ERROR GENÉRICO / DESCONOCIDO] Fallo en Verificar criterio: Al cargar un archivo que no sea imagen o supere el límite de
- **ID Caso ISTQB Asociado:** `TC_RF_004_029`
- **Módulo:** Carrito de Compras y Checkout
- **Severidad:** `Alta (Major)` | **Prioridad:** `Media`
- **Categoría de Causa Raíz:** `ERROR GENÉRICO / DESCONOCIDO`

#### Pasos para Reproducir:
1. Acceder al módulo bajo prueba (Carrito de Compras y Checkout).
2. Ejecutar la acción automatizada correspondiente a: Verificar criterio: Al cargar un archivo que no sea imagen o supere el límite de... en Carga de Imagen de Perfil de Usuario.
3. Inspeccionar el comportamiento en pantalla y las respuestas de red.

**Comportamiento Esperado:**  
El sistema debe procesar la solicitud según la especificación de negocio y mostrar confirmación/validación adecuada sin errores de ejecución.

**Comportamiento Obtenido:**  
Ocurrió un error tipo [ERROR GENÉRICO / DESCONOCIDO]: TypeError: pageObject.fillCredentials is not a function

  192 |     // Precondición: Entorno con servicios de notificación y mensajería habilitados.
  193 |     // 1. Probar valor frontera Max exacto

**Evidencia Técnica (Traceback):**
```text
TypeError: pageObject.fillCredentials is not a function
    at D:\workspace\agentic\playwright-suite\tests\carrito_de_compras_y_checkout.spec.ts:194:22
```

💡 **Recomendación de Remediación:**  
Revisar la lógica en la vista o endpoint del módulo Carrito de Compras y Checkout. Causa raíz detectada: Excepción durante la ejecución de los pasos del test.

---