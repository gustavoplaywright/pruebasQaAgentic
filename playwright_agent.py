#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
AGENTE QA PLAYWRIGHT - Generador Automatizado de Suites de Prueba E2E
=============================================================================
Este agente toma documentos de requerimientos, casos de uso o casos de prueba
(en Excel .xlsx formato ISTQB, Markdown .md o JSON) y genera automáticamente
una suite completa y modular de pruebas automatizadas en Playwright (TypeScript)
con arquitectura Page Object Model (POM), selectores semánticos y aserciones.
=============================================================================
"""

import os
import sys
import re
import json
import argparse
import unicodedata
from typing import List, Dict, Any, Optional

# UTF-8 para Windows consola
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    import openpyxl
except ImportError:
    openpyxl = None


# =============================================================================
# MODELO INTERNO DE CASO DE AUTOMATIZACIÓN
# =============================================================================

class AutoTestCase:
    def __init__(
        self,
        tc_id: str,
        module: str,
        req_ref: str,
        title: str,
        description: str,
        technique: str,
        priority: str,
        preconditions: str,
        steps: str,
        test_data: str,
        expected_result: str,
    ):
        self.tc_id = tc_id
        self.module = module
        self.req_ref = req_ref
        self.title = title
        self.description = description
        self.technique = technique
        self.priority = priority
        self.preconditions = preconditions
        self.steps = steps
        self.test_data = test_data
        self.expected_result = expected_result


# =============================================================================
# EXTRACTOR DE CASOS (Excel ISTQB, Markdown, JSON)
# =============================================================================

class TestCaseExtractor:
    @staticmethod
    def extract(source_path: str) -> List[AutoTestCase]:
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"No existe el archivo especificado: {source_path}")

        ext = os.path.splitext(source_path)[1].lower()
        if ext == ".xlsx":
            return TestCaseExtractor._extract_from_excel(source_path)
        elif ext == ".json":
            return TestCaseExtractor._extract_from_json(source_path)
        else:
            return TestCaseExtractor._extract_from_markdown_or_text(source_path)

    @staticmethod
    def _extract_from_excel(excel_path: str) -> List[AutoTestCase]:
        if openpyxl is None:
            raise ImportError("Se requiere 'openpyxl' para leer archivos Excel. Ejecute: pip install openpyxl")

        wb = openpyxl.load_workbook(excel_path, data_only=True)
        # Buscar hoja de casos de prueba
        sheet_name = None
        for name in wb.sheetnames:
            if "caso" in name.lower() or "test" in name.lower():
                sheet_name = name
                break
        
        if not sheet_name:
            sheet_name = wb.sheetnames[0]

        ws = wb[sheet_name]
        headers = [str(cell.value or '').strip() for cell in ws[1]]
        
        def find_col(possible_names):
            for idx, h in enumerate(headers):
                for p in possible_names:
                    if p.lower() in h.lower():
                        return idx + 1
            return None

        c_id = find_col(["id caso", "tc_id", "id"]) or 1
        c_mod = find_col(["módulo", "modulo", "feature", "module"]) or 2
        c_req = find_col(["ref. requisito", "requisito", "req_ref", "hu"]) or 3
        c_title = find_col(["título", "titulo", "title", "nombre"]) or 4
        c_desc = find_col(["descripción", "descripcion", "description", "objetivo"]) or 5
        c_tech = find_col(["técnica", "tecnica", "technique"]) or 7
        c_prio = find_col(["prioridad", "priority"]) or 9
        c_pre = find_col(["precondiciones", "precondition"]) or 10
        c_steps = find_col(["pasos", "steps"]) or 11
        c_data = find_col(["datos", "data", "test data"]) or 12
        c_expected = find_col(["resultado esperado", "expected"]) or 13

        cases: List[AutoTestCase] = []
        for row in range(2, ws.max_row + 1):
            val_id = str(ws.cell(row, c_id).value or '').strip()
            if not val_id or val_id.lower().startswith("id"):
                continue

            cases.append(AutoTestCase(
                tc_id=val_id,
                module=str(ws.cell(row, c_mod).value or 'General').strip(),
                req_ref=str(ws.cell(row, c_req).value or '').strip(),
                title=str(ws.cell(row, c_title).value or f"Test {val_id}").strip(),
                description=str(ws.cell(row, c_desc).value or '').strip(),
                technique=str(ws.cell(row, c_tech).value or 'General').strip(),
                priority=str(ws.cell(row, c_prio).value or 'Media').strip(),
                preconditions=str(ws.cell(row, c_pre).value or '').strip(),
                steps=str(ws.cell(row, c_steps).value or '').strip(),
                test_data=str(ws.cell(row, c_data).value or '').strip(),
                expected_result=str(ws.cell(row, c_expected).value or '').strip(),
            ))

        return cases

    @staticmethod
    def _extract_from_json(json_path: str) -> List[AutoTestCase]:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get("test_cases", [data])
        cases = []
        for idx, item in enumerate(items, 1):
            cases.append(AutoTestCase(
                tc_id=item.get("id", f"TC_AUTO_{idx:03d}"),
                module=item.get("module", "General"),
                req_ref=item.get("req_ref", f"REQ-{idx:03d}"),
                title=item.get("title", f"Test Case {idx}"),
                description=item.get("description", ""),
                technique=item.get("technique", "Funcional"),
                priority=item.get("priority", "Media (P2)"),
                preconditions=item.get("preconditions", ""),
                steps=item.get("steps", ""),
                test_data=item.get("test_data", ""),
                expected_result=item.get("expected_result", ""),
            ))
        return cases

    @staticmethod
    def _extract_from_markdown_or_text(md_path: str) -> List[AutoTestCase]:
        # Si es un archivo de requerimientos, reutilizar o invocar el parser QA
        # para generar la estructura
        from qa_agent import RequirementParser, ISTQBTestGenerator
        reqs = RequirementParser.parse_file(md_path)
        raw_cases = ISTQBTestGenerator.generate_test_cases(reqs)
        return [
            AutoTestCase(
                tc_id=c.tc_id,
                module=c.module,
                req_ref=c.req_ref,
                title=c.title,
                description=c.description,
                technique=c.technique,
                priority=c.priority,
                preconditions=c.preconditions,
                steps=c.steps,
                test_data=c.test_data,
                expected_result=c.expected_result,
            )
            for c in raw_cases
        ]


# =============================================================================
# GENERADOR DE SUITE PLAYWRIGHT (TypeScript + Page Object Model)
# =============================================================================

class PlaywrightSuiteGenerator:
    """
    Construye una suite completa de Playwright:
    - playwright.config.ts
    - tsconfig.json
    - pages/<Module>Page.ts (Page Object Models)
    - tests/<module>.spec.ts (Tests automáticos)
    - fixtures/testData.ts
    """

    def __init__(self, output_dir: str, base_url: str = "http://localhost:3000"):
        self.output_dir = output_dir
        self.base_url = base_url
        self.pages_dir = os.path.join(output_dir, "pages")
        self.tests_dir = os.path.join(output_dir, "tests")
        self.fixtures_dir = os.path.join(output_dir, "fixtures")

    def generate(self, cases: List[AutoTestCase]):
        os.makedirs(self.pages_dir, exist_ok=True)
        os.makedirs(self.tests_dir, exist_ok=True)
        os.makedirs(self.fixtures_dir, exist_ok=True)

        # 1. Configuración de Playwright y TypeScript
        self._write_playwright_config()
        self._write_tsconfig()
        self._write_test_data_fixture()

        # 2. Agrupar casos por módulo
        modules: Dict[str, List[AutoTestCase]] = {}
        for c in cases:
            norm_mod = self._normalize_name(c.module)
            modules.setdefault(norm_mod, []).append(c)

        # 3. Generar Page Objects y Specs por módulo
        generated_specs = []
        for mod_key, mod_cases in modules.items():
            pom_filename = self._generate_page_object(mod_key, mod_cases)
            spec_filename = self._generate_spec_file(mod_key, mod_cases)
            generated_specs.append((mod_key, spec_filename, len(mod_cases)))

        # 4. Crear suite demo mock para que ejecute localmente sin servidor externo
        self._write_mock_server_and_html()

        print(f"\n[+] Suite Playwright generada exitosamente en: {os.path.abspath(self.output_dir)}")
        print(f"    - Configuraciones: playwright.config.ts, tsconfig.json")
        print(f"    - Page Objects en: {self.pages_dir}")
        print(f"    - Especificaciones de Prueba en: {self.tests_dir}")
        print(f"    - Fixtures de Datos en: {self.fixtures_dir}")
        for mod_k, spec_f, count in generated_specs:
            print(f"      * {spec_f} ({count} tests)")

    def _strip_accents(self, text: str) -> str:
        return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

    def _normalize_name(self, name: str) -> str:
        s = self._strip_accents(name)
        s = re.sub(r'[^\w\s]', '', s)
        s = re.sub(r'\s+', '_', s.strip().lower())
        return s or "general"

    def _to_pascal_case(self, name: str) -> str:
        s = self._strip_accents(name)
        words = re.findall(r'[A-Za-z0-9]+', s)
        return "".join(w.capitalize() for w in words) or "General"

    def _write_playwright_config(self):
        config_content = f"""import {{ defineConfig, devices }} from '@playwright/test';

/**
 * Configuración de la Suite de Automatización QA Playwright
 * Generada automáticamente por el Agente QA Playwright.
 */
export default defineConfig({{
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
    ['html', {{ outputFolder: 'playwright-report', open: 'never' }}],
    ['list']
  ],
  use: {{
    /* URL base de la aplicación bajo prueba */
    baseURL: process.env.BASE_URL || '{self.base_url}',
    /* Captura de trazas y capturas de pantalla en fallos */
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  }},

  /* Proyectos para navegadores principales */
  projects: [
    {{
      name: 'chromium',
      use: {{ ...devices['Desktop Chrome'] }},
    }},
    {{
      name: 'firefox',
      use: {{ ...devices['Desktop Firefox'] }},
    }},
    {{
      name: 'webkit',
      use: {{ ...devices['Desktop Safari'] }},
    }},
  ],

  /* Servidor web local mock opcional para pruebas inmediatas */
  webServer: {{
    command: 'npx http-server ./mock-app -p 3000',
    port: 3000,
    reuseExistingServer: !process.env.CI,
  }},
}});
"""
        with open(os.path.join(self.output_dir, "playwright.config.ts"), "w", encoding="utf-8") as f:
            f.write(config_content)

    def _write_tsconfig(self):
        ts_config = """{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "baseUrl": ".",
    "paths": {
      "@pages/*": ["pages/*"],
      "@fixtures/*": ["fixtures/*"]
    }
  },
  "include": ["**/*.ts"]
}
"""
        with open(os.path.join(self.output_dir, "tsconfig.json"), "w", encoding="utf-8") as f:
            f.write(ts_config)

    def _write_test_data_fixture(self):
        data_content = """/**
 * Fixtures y datos de prueba centralizados
 * Incluye particiones de equivalencia válidas/inválidas y valores límite (BVA).
 */
export const testData = {
  // Datos de autenticación y registro
  auth: {
    validUser: {
      email: 'qa.automation@empresa.com',
      password: 'ValidPassword123!',
      fullName: 'QA Automation Lead',
    },
    invalidUser: {
      emptyEmail: '',
      badFormatEmail: 'usuario-sin-arroba.com',
      alreadyRegisteredEmail: 'existente@empresa.com',
      shortPassword: 'Pass1!',       // 6 caracteres (Límite inferior inválido Min-1)
      boundaryMinPassword: 'Pass123!', // 8 caracteres (Límite exacto Min)
      boundaryMaxPassword: 'A1!'.padEnd(20, 'a'), // 20 caracteres (Límite exacto Max)
      longPassword: 'A1!'.padEnd(21, 'a'),        // 21 caracteres (Límite superior inválido Max+1)
      noSpecialCharPassword: 'Password1234',
    },
    lockoutThreshold: 3, // Intentos fallidos para disparo de bloqueo
  },

  // Datos para pruebas de cupones y checkout
  checkout: {
    coupons: {
      validPercent: 'DESCUENTO10',
      validFixed: 'SUPER50',
      expiredCoupon: 'EXPIRED2024',
      invalidCoupon: 'CUPON_NO_EXISTE_999',
    },
    amounts: {
      underMin: 35.0,     // Menor al mínimo de $50
      exactMin: 50.0,     // Exacto mínimo para DESCUENTO10
      qualifiesSuper: 250.0, // Califica para SUPER50
      exceedsMax: 10500.0,   // Excede límite de $10,000
    }
  },

  // Datos de perfiles y carga de archivos
  profile: {
    validAvatarJpg: 'fixtures/sample_avatar.jpg',
    validAvatarPng: 'fixtures/sample_avatar.png',
    invalidFormatPdf: 'fixtures/document.pdf',
    oversizedAvatar: 'fixtures/large_image_3mb.jpg',
  },

  // Inyecciones de seguridad para Error Guessing
  securityPayloads: {
    xss: "<script>alert('XSS_QA')</script>",
    sqli: "' OR '1'='1' --",
    utf8Special: "ñÑáéíóú Ç!#$%&/()=? 🚀🔥",
  }
};
"""
        with open(os.path.join(self.fixtures_dir, "testData.ts"), "w", encoding="utf-8") as f:
            f.write(data_content)

    def _generate_page_object(self, mod_key: str, cases: List[AutoTestCase]) -> str:
        class_name = f"{self._to_pascal_case(mod_key)}Page"
        filename = f"{class_name}.ts"
        file_path = os.path.join(self.pages_dir, filename)

        # Detectar el tipo de módulo para personalizar métodos del POM
        is_auth = any(k in mod_key.lower() for k in ["autentic", "login", "registro", "seguridad"])
        is_checkout = any(k in mod_key.lower() for k in ["pago", "checkout", "cupon", "carrito"])
        is_profile = any(k in mod_key.lower() for k in ["perfil", "usuario", "avatar"])

        pom_code = f"""import {{ Page, Locator, expect }} from '@playwright/test';

/**
 * Page Object Model para el Módulo: {mod_key.replace('_', ' ').title()}
 * Encapsula la interacción con la interfaz y selectores orientados al usuario.
 */
export class {class_name} {{
  readonly page: Page;
  readonly path: string;

  // Localizadores principales del componente
  readonly mainHeading: Locator;
  readonly submitButton: Locator;
  readonly successAlert: Locator;
  readonly errorAlert: Locator;
  readonly validationMessage: Locator;

"""

        if is_auth:
            pom_code += """  // Elementos específicos de Autenticación
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly confirmPasswordInput: Locator;
  readonly rememberMeCheckbox: Locator;
  readonly lockoutBanner: Locator;

  constructor(page: Page) {
    this.page = page;
    this.path = '/login';
    this.mainHeading = page.getByRole('heading', { level: 1 });
    this.emailInput = page.getByLabel('Correo Electrónico').or(page.getByPlaceholder('usuario@dominio.com'));
    this.passwordInput = page.getByLabel('Contraseña').or(page.getByPlaceholder('Ingresa tu contraseña'));
    this.confirmPasswordInput = page.getByLabel('Confirmar Contraseña');
    this.submitButton = page.getByRole('button', { name: /Iniciar Sesión|Registrarse|Enviar/i });
    this.successAlert = page.getByRole('alert').filter({ hasText: /éxito|bienvenido|confirmación/i });
    this.errorAlert = page.getByRole('alert').filter({ hasText: /error|inválid|bloquead|requerid/i });
    this.validationMessage = page.locator('.field-validation-error, .invalid-feedback');
    this.lockoutBanner = page.getByRole('alert').filter({ hasText: /bloqueada temporalmente/i });
  }

  async goto() {
    await this.page.goto(this.path);
    await expect(this.mainHeading).toBeVisible();
  }

  async fillCredentials(email: string, pass: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(pass);
  }

  async submit() {
    await this.submitButton.click();
  }

  async login(email: string, pass: string) {
    await this.fillCredentials(email, pass);
    await this.submit();
  }

  async register(email: string, pass: string, confirmPass?: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(pass);
    if (confirmPass && await this.confirmPasswordInput.isVisible()) {
      await this.confirmPasswordInput.fill(confirmPass);
    }
    await this.submit();
  }
"""
        elif is_checkout:
            pom_code += """  // Elementos específicos de Checkout y Cupones
  readonly couponInput: Locator;
  readonly applyCouponButton: Locator;
  readonly totalOrderAmount: Locator;
  readonly discountAmount: Locator;
  readonly checkoutButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.path = '/checkout';
    this.mainHeading = page.getByRole('heading', { name: /checkout|carrito|orden/i });
    this.couponInput = page.getByPlaceholder(/código de cupón|cupón/i).or(page.getByLabel('Cupón'));
    this.applyCouponButton = page.getByRole('button', { name: /aplicar|canjear/i });
    this.totalOrderAmount = page.locator('[data-testid="order-total"], .total-price');
    this.discountAmount = page.locator('[data-testid="discount-amount"], .discount-row');
    this.submitButton = page.getByRole('button', { name: /pagar|finalizar compra/i });
    this.successAlert = page.getByRole('alert').filter({ hasText: /descuento aplicado|cupón válido/i });
    this.errorAlert = page.getByRole('alert').filter({ hasText: /inválido|expirado|insuficiente|máximo/i });
    this.validationMessage = page.locator('.coupon-feedback, .error-message');
  }

  async goto() {
    await this.page.goto(this.path);
  }

  async applyCoupon(code: string) {
    await this.couponInput.fill(code);
    await this.applyCouponButton.click();
  }
"""
        else:
            pom_code += """  // Elementos genéricos y de carga de archivos
  readonly genericInput: Locator;
  readonly fileUploadInput: Locator;
  readonly previewAvatar: Locator;

  constructor(page: Page) {
    this.page = page;
    this.path = '/';
    this.mainHeading = page.getByRole('heading').first();
    this.genericInput = page.locator('input').first();
    this.fileUploadInput = page.locator('input[type="file"]');
    this.previewAvatar = page.locator('[data-testid="avatar-preview"], img.avatar');
    this.submitButton = page.getByRole('button', { name: /guardar|actualizar|enviar/i });
    this.successAlert = page.getByRole('alert').filter({ hasText: /éxito|guardado|actualizado/i });
    this.errorAlert = page.getByRole('alert').filter({ hasText: /error|no permitido|supera/i });
    this.validationMessage = page.locator('.field-error');
  }

  async goto() {
    await this.page.goto(this.path);
  }

  async uploadFile(filePath: string) {
    await this.fileUploadInput.setInputFiles(filePath);
    await this.submitButton.click();
  }
"""

        pom_code += """
  async expectSuccess() {
    await expect(this.successAlert).toBeVisible();
  }

  async expectError(messagePattern?: RegExp | string) {
    await expect(this.errorAlert).toBeVisible();
    if (messagePattern) {
      await expect(this.errorAlert).toContainText(messagePattern);
    }
  }
}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(pom_code)

        return filename

    def _generate_spec_file(self, mod_key: str, cases: List[AutoTestCase]) -> str:
        class_name = f"{self._to_pascal_case(mod_key)}Page"
        spec_filename = f"{mod_key}.spec.ts"
        spec_path = os.path.join(self.tests_dir, spec_filename)

        lines = [
            f"import {{ test, expect }} from '@playwright/test';",
            f"import {{ {class_name} }} from '../pages/{class_name}';",
            f"import {{ testData }} from '../fixtures/testData';",
            "",
            f"/**",
            f" * Suite Automatizada para el Módulo: {mod_key.replace('_', ' ').title()}",
            f" * Generada automáticamente bajo trazabilidad ISTQB",
            f" */",
            f"test.describe('Módulo: {mod_key.replace('_', ' ').title()}', () => {{",
            f"  let pageObject: {class_name};",
            "",
            f"  test.beforeEach(async ({{ page }}) => {{",
            f"    pageObject = new {class_name}(page);",
            f"    await pageObject.goto();",
            f"  }});",
            ""
        ]

        for tc in cases:
            # Limpiar comillas para descripción del test
            clean_title = tc.title.replace("'", "\\'")
            prio_tag = "@P1" if "alta" in tc.priority.lower() else ("@P2" if "media" in tc.priority.lower() else "@P3")
            
            lines.append(f"  /**")
            lines.append(f"   * Caso ISTQB: {tc.tc_id} | Técnica: {tc.technique}")
            lines.append(f"   * Requisito: {tc.req_ref} | Prioridad: {tc.priority}")
            lines.append(f"   * Objetivo: {tc.description}")
            lines.append(f"   */")
            lines.append(f"  test('{tc.tc_id}: [{prio_tag}] {clean_title}', async ({{ page }}) => {{")

            # Generar cuerpo del test según técnica y título
            lines.extend(self._generate_test_body(tc, mod_key))

            lines.append(f"  }});")
            lines.append("")

        lines.append("});")

        with open(spec_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return spec_filename

    def _generate_test_body(self, tc: AutoTestCase, mod_key: str) -> List[str]:
        body = []
        lower_title = tc.title.lower()
        lower_tech = tc.technique.lower()

        # Comentario de precondiciones
        body.append(f"    // Precondición: {tc.preconditions}")

        is_invalid_class = "inválid" in lower_tech or "invalid" in lower_tech or "vacío" in lower_title or "vacio" in lower_title or "requerido" in lower_title or "rechazo" in lower_title
        is_valid_class = not is_invalid_class and ("exitoso" in lower_title or "válida" in lower_tech or "valida" in lower_tech or "happy" in lower_title)
        is_bva = "límite" in lower_title or "limite" in lower_title or "bva" in lower_tech
        is_lockout = "bloqueo" in lower_title or "estado" in lower_title or "transición" in lower_tech or "transicion" in lower_tech
        is_security = "resistencia" in lower_title or "inyecci" in lower_title or "error guessing" in lower_tech or "caracteres especiales" in lower_title
        is_decision = "regla" in lower_title or "tabla" in lower_tech or "decisión" in lower_tech or "decision" in lower_tech

        # 1. Campos obligatorios vacíos o clase inválida
        if is_invalid_class:
            if "autentic" in mod_key or "login" in mod_key or "registro" in mod_key:
                body.append("    // 1. Intentar enviar formulario con campos vacíos o datos requeridos omitidos")
                body.append("    await pageObject.submit();")
                body.append("    // 2. Aserción: Bloqueo de envío y mensaje de validación visible")
                body.append("    await pageObject.expectError(/requerido|obligatorio|ingrese|inválid/i);")
            elif "checkout" in mod_key or "pago" in mod_key:
                body.append("    await pageObject.applyCoupon('');")
                body.append("    await pageObject.expectError(/ingrese|requerido|inválido/i);")
            else:
                body.append("    await pageObject.submitButton.click();")
                body.append("    await pageObject.expectError();")

        # 2. Análisis de Valores Límite (BVA)
        elif is_bva:
            if "inferior" in lower_title or "mínimo" in lower_title or "min" in lower_title:
                body.append("    // 1. Probar valor frontera Min - 1 (Inválido)")
                body.append("    await pageObject.fillCredentials(testData.auth.validUser.email, testData.auth.invalidUser.shortPassword);")
                body.append("    await pageObject.submit();")
                body.append("    await pageObject.expectError(/mínimo|longitud insuficiente|longitud/i);")
                body.append("    // 2. Probar valor frontera Min exacto (Válido)")
                body.append("    await pageObject.fillCredentials(testData.auth.validUser.email, testData.auth.invalidUser.boundaryMinPassword);")
                body.append("    await pageObject.submit();")
            else:
                body.append("    // 1. Probar valor frontera Max exacto (Válido)")
                body.append("    await pageObject.fillCredentials(testData.auth.validUser.email, testData.auth.invalidUser.boundaryMaxPassword);")
                body.append("    await pageObject.submit();")
                body.append("    // 2. Probar valor frontera Max + 1 (Inválido)")
                body.append("    await pageObject.fillCredentials(testData.auth.validUser.email, testData.auth.invalidUser.longPassword);")
                body.append("    await pageObject.submit();")
                body.append("    await pageObject.expectError(/máximo excedido|longitud|supera/i);")

        # 3. Transición de estados / Bloqueo
        elif is_lockout:
            body.append("    // Simulación de 3 intentos fallidos consecutivos")
            body.append("    for (let intento = 1; intento <= testData.auth.lockoutThreshold; intento++) {")
            body.append("      await pageObject.login('test.lockout@empresa.com', 'WrongPass123!');")
            body.append("      if (intento < testData.auth.lockoutThreshold) {")
            body.append("        await pageObject.expectError(/inválid/i);")
            body.append("      }")
            body.append("    }")
            body.append("    // Aserción: Cuenta bloqueada temporalmente")
            body.append("    await expect(pageObject.lockoutBanner).toBeVisible();")

        # 4. Seguridad y Adivinación de Errores (Error Guessing / XSS / SQLi)
        elif is_security:
            body.append("    // Prueba de robustez frente a XSS y SQL Injection")
            body.append("    await pageObject.fillCredentials(testData.securityPayloads.xss, testData.securityPayloads.sqli);")
            body.append("    await pageObject.submit();")
            body.append("    // Aserción: La aplicación no ejecuta scripts y maneja el rechazo limpiamente")
            body.append("    await pageObject.expectError();")
            body.append("    await expect(page.locator('text=Internal Server Error')).toHaveCount(0);")

        # 5. Reglas de negocio / Tablas de decisión
        elif is_decision:
            if "checkout" in mod_key or "pago" in mod_key:
                body.append("    // Prueba de combinatoria de cupón frente a monto mínimo")
                body.append("    await pageObject.applyCoupon(testData.checkout.coupons.validFixed);")
                body.append("    // Verificación de regla de negocio")
                body.append("    await pageObject.expectSuccess();")
            else:
                body.append("    await pageObject.submit();")
                body.append("    await pageObject.expectSuccess();")

        # 6. Camino feliz / Válido
        elif is_valid_class:
            if "autentic" in mod_key or "login" in mod_key or "registro" in mod_key:
                body.append("    // 1. Ingresar credenciales válidas")
                body.append("    await pageObject.login(testData.auth.validUser.email, testData.auth.validUser.password);")
                body.append("    // 2. Aserción: Verificar mensaje de confirmación o redirección")
                body.append("    await pageObject.expectSuccess();")
            elif "checkout" in mod_key or "pago" in mod_key:
                body.append("    // 1. Aplicar cupón válido")
                body.append("    await pageObject.applyCoupon(testData.checkout.coupons.validPercent);")
                body.append("    // 2. Aserción: Descuento reflejado exitosamente")
                body.append("    await pageObject.expectSuccess();")
            else:
                body.append("    await pageObject.submitButton.click();")
                body.append("    await pageObject.expectSuccess();")

        # Fallback genérico
        else:
            body.append("    // Ejecución de flujo del caso de prueba")
            body.append("    await pageObject.submit();")
            body.append("    // Verificar resultado esperado")
            body.append("    // Resultado esperado: " + tc.expected_result.replace("\n", " "))
            body.append("    await expect(page).not.toHaveTitle('');")

        return body

    def _write_mock_server_and_html(self):
        """Crea una mini app HTML mock para que la suite de Playwright sea inmediatamente ejecutable"""
        mock_dir = os.path.join(self.output_dir, "mock-app")
        os.makedirs(mock_dir, exist_ok=True)

        html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>App Demo QA - Entorno de Pruebas</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 40px; background: #f8fafc; }
    .card { background: white; padding: 24px; border-radius: 8px; max-width: 500px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); margin-bottom: 20px; }
    h1 { color: #1e293b; font-size: 20px; margin-bottom: 16px; }
    label { display: block; margin-top: 12px; font-weight: 500; font-size: 14px; }
    input[type="text"], input[type="password"], input[type="file"] { width: 100%; padding: 8px 12px; margin-top: 4px; box-sizing: border-box; border: 1px solid #cbd5e1; border-radius: 4px; }
    button { margin-top: 16px; background: #2563eb; color: white; padding: 10px 18px; border: none; border-radius: 4px; cursor: pointer; font-weight: 600; }
    button:hover { background: #1d4ed8; }
    .alert { padding: 12px; border-radius: 4px; margin-top: 16px; display: none; font-size: 14px; }
    .alert-success { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
    .alert-danger { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Iniciar Sesión / Registro</h1>
    <form id="authForm">
      <label for="email">Correo Electrónico</label>
      <input type="text" id="email" placeholder="usuario@dominio.com">
      
      <label for="password">Contraseña</label>
      <input type="password" id="password" placeholder="Ingresa tu contraseña">

      <button type="button" id="btnLogin" onclick="handleAuth()">Iniciar Sesión</button>
    </form>

    <div id="authAlert" role="alert" class="alert"></div>
  </div>

  <div class="card">
    <h1>Checkout y Cupones</h1>
    <label for="coupon">Cupón de Descuento</label>
    <input type="text" id="coupon" placeholder="Código de cupón">
    <button type="button" onclick="handleCoupon()">Aplicar</button>
    <div id="couponAlert" role="alert" class="alert"></div>
  </div>

  <script>
    let failedAttempts = 0;

    function handleAuth() {
      const email = document.getElementById('email').value.trim();
      const pass = document.getElementById('password').value;
      const alertBox = document.getElementById('authAlert');
      alertBox.style.display = 'block';

      if (!email || !pass) {
        alertBox.className = 'alert alert-danger';
        alertBox.innerText = 'Error: Todos los campos son obligatorios y requeridos.';
        return;
      }

      if (email.includes('<script>') || pass.includes("' OR")) {
        alertBox.className = 'alert alert-danger';
        alertBox.innerText = 'Error: Entrada no permitida por seguridad.';
        return;
      }

      if (pass.length < 8) {
        alertBox.className = 'alert alert-danger';
        alertBox.innerText = 'Error: La contraseña no cumple con la longitud mínima requerida.';
        return;
      }

      if (pass.length > 20) {
        alertBox.className = 'alert alert-danger';
        alertBox.innerText = 'Error: Longitud máxima excedida.';
        return;
      }

      if (email === 'test.lockout@empresa.com' && pass === 'WrongPass123!') {
        failedAttempts++;
        if (failedAttempts >= 3) {
          alertBox.className = 'alert alert-danger';
          alertBox.innerText = 'Alerta: Cuenta bloqueada temporalmente por 15 minutos debido a intentos fallidos.';
        } else {
          alertBox.className = 'alert alert-danger';
          alertBox.innerText = 'Error: Credenciales inválidas. Intento ' + failedAttempts + ' de 3.';
        }
        return;
      }

      alertBox.className = 'alert alert-success';
      alertBox.innerText = '¡Éxito! Bienvenido al sistema.';
    }

    function handleCoupon() {
      const code = document.getElementById('coupon').value.trim().toUpperCase();
      const alertBox = document.getElementById('couponAlert');
      alertBox.style.display = 'block';

      if (!code) {
        alertBox.className = 'alert alert-danger';
        alertBox.innerText = 'Error: Ingrese un cupón válido.';
        return;
      }

      if (code === 'DESCUENTO10' || code === 'SUPER50') {
        alertBox.className = 'alert alert-success';
        alertBox.innerText = '¡Éxito! Descuento aplicado satisfactoriamente.';
      } else {
        alertBox.className = 'alert alert-danger';
        alertBox.innerText = 'Error: El cupón ingresado no es válido o ha expirado.';
      }
    }
  </script>
</body>
</html>
"""
        with open(os.path.join(mock_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Agente QA Playwright: Genera suites automatizadas en Playwright (TypeScript/POM) a partir de casos ISTQB, requerimientos o use cases."
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Archivo fuente: Excel de casos ISTQB (.xlsx), requerimientos (.md / .txt) o JSON."
    )
    parser.add_argument(
        "-o", "--output-dir",
        default="playwright-suite",
        help="Directorio de destino para la suite de Playwright (default: playwright-suite)"
    )
    parser.add_argument(
        "--base-url",
        default="http://localhost:3000",
        help="URL base de la aplicación bajo prueba (default: http://localhost:3000)"
    )

    args = parser.parse_args()

    print("=" * 70)
    print("AGENTE QA PLAYWRIGHT - AUTOMATIZACIÓN DE PRUEBAS E2E")
    print("=" * 70)
    print(f"[*] Extrayendo casos de prueba desde: {args.input}")
    cases = TestCaseExtractor.extract(args.input)
    print(f"[+] Total de Casos extraídos para automatización: {len(cases)}")

    print(f"[*] Diseñando suite de Playwright en: {args.output_dir}")
    generator = PlaywrightSuiteGenerator(output_dir=args.output_dir, base_url=args.base_url)
    generator.generate(cases)

    print("=" * 70)
    print("SUITE LISTA PARA EJECUCIÓN")
    print(f"Comando para ejecutar las pruebas:")
    print(f"  npx playwright test")
    print("=" * 70)


if __name__ == "__main__":
    main()
