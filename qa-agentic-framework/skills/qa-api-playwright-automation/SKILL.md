---
name: qa-api-playwright-automation
description: Analiza especificaciones de API (Swagger, OpenAPI, colecciones Postman o cURL), selecciona esquemas, endpoints y verbos HTTP, y genera scripts de prueba automatizados de integración/API con Playwright usando APIRequestContext en TypeScript.
---

# QA API Playwright Automation

## Propósito
Transformar especificaciones de servicios web en suites de pruebas de API automatizadas, robustas y tipadas utilizando el cliente de API nativo de Playwright (`request`).

## Entradas Requeridas
- Endpoint, método HTTP (GET, POST, PUT, DELETE, PATCH).
- Headers obligatorios (Authorization, Content-Type, etc.).
- Body / Payload (JSON/XML) y parámetros de consulta (Query Params).
- Contrato o Schema esperado (validación JSON Schema).
- Respuestas esperadas (Status code, body response).

## Estrategia de Validación de APIs
El agente debe incorporar las siguientes aserciones para cada endpoint:
1. **Status Code:** Validar códigos exactos (ej. `200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`).
2. **Estructura y Contrato (JSON Schema):** Verificar tipos de datos (strings, numbers, booleans) y campos requeridos.
3. **Encabezados (Headers):** Validar `content-type` (ej. `application/json; charset=utf-8`).
4. **Respuesta de Negocio:** Validar valores clave dentro del JSON de respuesta (IDs, tokens, mensajes).
5. **Tiempos de Respuesta (SLA):** Asegurar que la respuesta ocurra dentro de un umbral aceptable (ej. `< 2000ms`).

## Estructura de Código Playwright API

Organizar la automatización de API mediante servicios reutilizables:

1. **Service Class (`services/*.service.ts`):** Métodos que encapsulan los llamados HTTP.
2. **Spec / Test (`tests/api/*.spec.ts`):** Casos de prueba con fixtures de `request` y aserciones.

## Reglas de Código TypeScript & Playwright API
- Usar destructuring y tipos de TypeScript definidos mediante `interface` o `type` para los payloads.
- Utilizar `await request.fetch()` o los métodos shorthand (`await request.post()`, `await request.get()`).
- Manejar tokens o variables de entorno mediante `process.env`.