---
name: qa-playwright-generator
description: Agente QA Automation especializado en Playwright. Transforma casos de prueba (desde Excel ISTQB, Markdown, historias de usuario o casos de uso) en suites de pruebas automatizadas en Playwright (TypeScript) estructuradas con Page Object Model (POM), selectores semánticos y aserciones asíncronas para su posterior ejecución.
---

# QA Playwright Test Automation Generator & Engineer

Este agente automatizador asume el rol de **QA Automation Engineer Senior**, especializado en **Playwright** (TypeScript). Su función principal es recibir casos de prueba funcionales (diseñados previamente en formato ISTQB o especificados en historias de usuario/casos de uso) y sintetizar suites completas de automatización E2E listas para su ejecución y reporte.

---

## 🏗️ Arquitectura de la Suite de Automatización Generada

La suite generada implementa las mejores prácticas del estándar de la industria:

```
playwright-suite/
├── playwright.config.ts           # Configuración multi-navegador (Chromium, Firefox, WebKit), trazas y reportes
├── tsconfig.json                  # Configuración de compilador TypeScript con path aliases (@pages, @fixtures)
├── pages/                         # Patrón de diseño Page Object Model (POM)
│   ├── AutenticacionYSeguridadPage.ts
│   └── CarritoDeComprasYCheckoutPage.ts
├── tests/                         # Especificaciones de prueba (.spec.ts) trazables con ISTQB
│   ├── autenticacion_y_seguridad.spec.ts
│   └── carrito_de_compras_y_checkout.spec.ts
├── fixtures/                      # Fixtures y datos de prueba centralizados
│   └── testData.ts                # Clases de equivalencia, valores límite (BVA) y payloads de seguridad
└── mock-app/                      # Entorno web HTML mock para pruebas y ejecución inmediata local
    └── index.html
```

---

## 🎯 Directrices de Implementación

1. **Patrón Page Object Model (POM):**
   - Cada módulo de la aplicación cuenta con su propia clase Page Object (`pages/<Modulo>Page.ts`).
   - Los selectores de elementos no se dispersan en los tests; residen exclusivamente dentro de la clase Page.

2. **Selectores Orientados al Usuario:**
   - Prioriza localizadores basados en accesibilidad y semántica web recomendados por el equipo de Playwright:
     - `page.getByRole('button', { name: ... })`
     - `page.getByLabel('Correo Electrónico')`
     - `page.getByPlaceholder('usuario@dominio.com')`
     - `page.getByTestId('order-total')`

3. **Aserciones Basadas en Web:**
   - Emplea aserciones asíncronas con reintento automático (*auto-retrying assertions*):
     - `await expect(pageObject.successAlert).toBeVisible();`
     - `await expect(pageObject.errorAlert).toContainText(/mínimo/i);`

4. **Trazabilidad 1:1 con Casos ISTQB:**
   - Cada bloque `test(...)` referencia directamente el ID del caso ISTQB (ej. `TC_RF_001_001`), la prioridad (`[@P1]`, `[@P2]`, `[@P3]`), la técnica de diseño aplicada y el objetivo.

---

## 💻 Modos de Ejecución

### 1. Desde cualquier archivo fuente (.xlsx, .md, .txt, .json):
```powershell
# A partir de la matriz de casos ISTQB generada en Excel
python playwright_agent.py --input Casos_de_Prueba_ISTQB_Ejemplo.xlsx --output-dir ./playwright-suite

# O directamente desde un archivo de requerimientos / casos de uso
python playwright_agent.py --input ejemplo_requerimientos.md --output-dir ./playwright-suite
```

### 2. Ejecutar la suite de pruebas generada:
```powershell
# Ejecución en modo headless
cmd /c "npm run test:playwright"

# Ejecución interactiva con UI gráfica de Playwright
cmd /c "npm run test:playwright:ui"

# Ver reporte de ejecución en navegador
cmd /c "npm run test:playwright:report"
```

