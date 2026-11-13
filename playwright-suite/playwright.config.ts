import { defineConfig, devices } from '@playwright/test';

/**
 * Configuración de la Suite de Automatización QA Playwright
 * Generada automáticamente por el Agente QA Playwright.
 */
export default defineConfig({
  testDir: './tests',
  /* Ejecutar tests en archivos en paralelo */
  fullyParallel: true,
  /* Fallar la compilación en CI si accidentalmente dejamos test.only en el código fuente */
  forbidOnly: !!process.env.CI,
  /* Reintentar en CI solamente */
  retries: process.env.CI ? 2 : 0,
  /* Optar por no tener trabajadores paralelos en CI si los recursos son limitados */
  workers: process.env.CI ? 1 : undefined,
  /* Reportería rica: HTML local y salida visual en terminal */
  reporter: [
    ['html', { outputFolder: 'playwright-report', open: 'never' }],
    ['list']
  ],
  use: {
    /* URL base de la aplicación bajo prueba */
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    /* Captura de trazas y capturas de pantalla en fallos */
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },

  /* Proyectos para navegadores principales */
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],

  /* Servidor web local mock opcional para pruebas inmediatas */
  webServer: {
    command: 'python -m http.server 3000 --directory ./mock-app',
    port: 3000,
    reuseExistingServer: true,
  },
});
