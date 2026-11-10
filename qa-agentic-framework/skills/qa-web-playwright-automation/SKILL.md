---
name: qa-web-playwright-automation
description: Analiza la estructura del DOM (HTML/JSX), selecciona los mejores localizadores según las buenas prácticas de Playwright y genera scripts de prueba E2E automatizados en TypeScript utilizando el patrón Page Object Model (POM).
---

# QA Web Playwright Automation

## Propósito
Convertir casos de prueba funcionales y fragmentos o capturas del DOM/HTML en scripts automatizados robustos, mantenibles y limpios utilizando Playwright con TypeScript.

## Entradas Requeridas
- Caso de prueba a automatizar (proveniente de `qa-test-case-creator`).
- Snippet HTML, inspect del DOM o selectores de los elementos de la página.

## Estrategia de Selección de Localizadores (Prioridad de Playwright)
El agente debe priorizar la selección de localizadores respetando el siguiente orden estricto:
1. `page.getByTestId('...')` (Si existe el atributo `data-testid` o `data-cy`).
2. `page.getByRole('...', { name: '...' })` (Accesibilidad y semántica HTML).
3. `page.getByLabel('...')` (Formularios e inputs).
4. `page.getByPlaceholder('...')` (Inputs con placeholder).
5. `page.getByText('...')` (Texto visible).
6. **CSS / XPath (Última opción):** Solo utilizar si no existen las alternativas anteriores y siempre asegurando resiliencia a cambios.

## Patron de Arquitectura: Page Object Model (POM)
Generar la solución dividida en dos capas:
1. **Page Object (`*.page.ts`):** Definición de locators y métodos de acción.
2. **Spec / Test (`*.spec.ts`):** Flujo de prueba con aserciones declarativas (`expect`).

## Reglas de Código TypeScript & Playwright
- Usar `async / await` en todas las interacciones del objeto `page`.
- Evitar timeouts hardcodeados (`page.waitForTimeout`); usar esperas implícitas o `waitForURL` / `waitForSelector`.
- Utilizar aserciones web explícitas (`await expect(locator).toBeVisible()`, `await expect(page).toHaveURL()`).
- Implementar tipos estrictos de TypeScript sin usar `any`.