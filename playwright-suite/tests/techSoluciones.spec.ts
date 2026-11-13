import { expect, test } from '@playwright/test';
import { TechSolucionesPage } from '../pages/TechSolucionesPage';

test.describe('Tech Soluciones - portada', () => {
  let pageObject: TechSolucionesPage;

  test.beforeEach(async ({ page }) => {
    pageObject = new TechSolucionesPage(page);
    await pageObject.goto();
  });

  test('TC_DOM_001 [@P1] Partición de Equivalencia: carga y landmarks principales', async ({ page }) => {
    await expect(page).toHaveTitle('TECH SOLUCIONES');
    await expect(pageObject.banner).toBeVisible();
    await expect(pageObject.navigation).toBeVisible();
    await expect(pageObject.main).toBeVisible();
    await expect(pageObject.footer).toBeVisible();
  });

  test('TC_DOM_002 [@P2] Partición de Equivalencia: identidad y contenido de categorías', async ({ page }) => {
    await expect(pageObject.brandLink).toBeVisible();
    await expect(pageObject.main.getByRole('heading', { name: 'Inicio', level: 2 })).toBeVisible();
    await expect(pageObject.main.getByRole('heading', {
      name: 'Exploración de Categorías y Productos',
      level: 3,
    })).toBeVisible();
    await expect(pageObject.main).toContainText('Componentes y Actualizaciones:');
    await expect(pageObject.main).toContainText('Notebooks de Última Generación:');
    await expect(pageObject.main).toContainText('Insumos y Accesorios:');
  });

  test('TC_DOM_003 [@P2] Partición de Equivalencia: bloque promocional visible', async ({ page }) => {
    await expect(pageObject.main.getByRole('heading', {
      name: 'Promociones Exclusivas y Experiencia de Compra Única',
    })).toBeVisible();
    await expect(pageObject.main).toContainText('Ofertas de la Semana');
    await expect(pageObject.main).toContainText('envíos rápidos y seguros');
  });

  test('TC_DOM_004 [@P1] Partición de Equivalencia: logo e Inicio navegan al ancla', async ({ page }) => {
    const homeLink = pageObject.navigation.getByRole('link', { name: 'Inicio' });
    await expect(pageObject.brandLink).toHaveAttribute('href', '#inicio');
    await expect(homeLink).toHaveAttribute('href', '#inicio');

    await pageObject.brandLink.click();
    await expect(page).toHaveURL(/#inicio$/);
    await homeLink.click();
    await expect(page).toHaveURL(/#inicio$/);
  });

  test('TC_DOM_005 [@P1] Partición de Equivalencia: destinos de navegación interna', async ({ page }) => {
    const expectedDestinations = [
      ['Nosotros', './pages/nosotros.html'],
      ['Productos', './pages/productos.html'],
      ['Especiales', './pages/especiales.html'],
      ['Contacto', './pages/contactos.html'],
    ] as const;

    for (const [name, destination] of expectedDestinations) {
      await expect(pageObject.navigation.getByRole('link', { name })).toHaveAttribute('href', destination);
    }
  });

  test('TC_DOM_006 [@P2] Partición de Equivalencia: destinos de enlaces sociales', async ({ page }) => {
    const socialLinks = [
      ['Instagram', 'https://instagram.com/'],
      ['Facebook', 'https://facebook.com/'],
      ['X (Twitter)', 'https://x.com/'],
    ] as const;

    for (const [name, destination] of socialLinks) {
      const accessibleName = name === 'X (Twitter)' ? /X \(Twitter\)/ : new RegExp(name);
      await expect(pageObject.footer.getByRole('link', { name: accessibleName }))
        .toHaveAttribute('href', destination);
    }
  });

  test('TC_DOM_007 [@P1] Partición de Equivalencia: diapositiva inicial del carrusel principal', async () => {
    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Memorias RAM');
    await expect(pageObject.activeSlide(pageObject.primaryCarousel).getByRole('img'))
      .toHaveAttribute('alt', 'Memoria RAM');
    await expect(pageObject.activeSlide(pageObject.primaryCarousel))
      .toContainText('Potencia y velocidad para tu equipo.');
  });

  test('TC_DOM_008 [@P1] Partición de Equivalencia: selección directa de diapositivas principales', async () => {
    const slides = [
      { number: 1, title: 'Memorias RAM', alt: 'Memoria RAM' },
      { number: 2, title: 'Procesadores', alt: 'Procesador CPU' },
      { number: 3, title: 'Notebooks', alt: 'Notebooks' },
    ];

    for (const slide of slides) {
      await pageObject.selectSlide(pageObject.primaryCarousel, slide.number);
      await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText(slide.title);
      await expect(pageObject.activeSlide(pageObject.primaryCarousel).getByRole('img'))
        .toHaveAttribute('alt', slide.alt);
      await expect(pageObject.activeIndicator(pageObject.primaryCarousel))
        .toHaveAttribute('aria-label', `Slide ${slide.number}`);
    }
  });

  test('TC_DOM_009 [@P1] Transición de Estados: Siguiente avanza una diapositiva principal', async () => {
    await pageObject.nextSlide(pageObject.primaryCarousel);
    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Procesadores');
    await expect(pageObject.activeIndicator(pageObject.primaryCarousel)).toHaveAttribute('aria-label', 'Slide 2');
  });

  test('TC_DOM_010 [@P1] Transición de Estados: Anterior retrocede una diapositiva principal', async () => {
    await pageObject.selectSlide(pageObject.primaryCarousel, 2);
    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Procesadores');
    await pageObject.previousSlide(pageObject.primaryCarousel);
    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Memorias RAM');
    await expect(pageObject.activeIndicator(pageObject.primaryCarousel)).toHaveAttribute('aria-label', 'Slide 1');
  });

  test('TC_DOM_011 [@P2] Transición de Estados: ciclo principal sincroniza contenido e indicador', async () => {
    await pageObject.selectSlide(pageObject.primaryCarousel, 3);
    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Notebooks');
    await pageObject.nextSlide(pageObject.primaryCarousel);

    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Memorias RAM');
    await expect(pageObject.activeIndicator(pageObject.primaryCarousel)).toHaveAttribute('aria-label', 'Slide 1');
  });

  test('TC_DOM_012 [@P2] Transición de Estados: Anterior recorre el límite inicial', async () => {
    await pageObject.previousSlide(pageObject.primaryCarousel);
    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Notebooks');
    await expect(pageObject.activeIndicator(pageObject.primaryCarousel)).toHaveAttribute('aria-label', 'Slide 3');
  });

  test('TC_DOM_013 [@P2] Partición de Equivalencia: estado inicial del segundo carrusel', async () => {
    await expect(pageObject.activeSlideTitle(pageObject.secondaryCarousel)).toHaveText('Memorias RAM');
    await expect(pageObject.activeSlide(pageObject.secondaryCarousel).getByRole('img'))
      .toHaveAttribute('alt', 'Memoria RAM');
  });

  test('TC_DOM_014 [@P1] Transición de Estados: los carruseles son independientes', async () => {
    await pageObject.selectSlide(pageObject.secondaryCarousel, 2);
    await expect(pageObject.activeSlideTitle(pageObject.secondaryCarousel)).toHaveText('Procesadores');
    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Memorias RAM');
    await expect(pageObject.activeIndicator(pageObject.secondaryCarousel)).toHaveAttribute('aria-label', 'Slide 2');
    await expect(pageObject.activeIndicator(pageObject.primaryCarousel)).toHaveAttribute('aria-label', 'Slide 1');
  });

  test('TC_DOM_015 [@P2] Transición de Estados: controles del segundo carrusel', async () => {
    await pageObject.nextSlide(pageObject.secondaryCarousel);
    await expect(pageObject.activeSlideTitle(pageObject.secondaryCarousel)).toHaveText('Procesadores');
    await pageObject.previousSlide(pageObject.secondaryCarousel);
    await expect(pageObject.activeSlideTitle(pageObject.secondaryCarousel)).toHaveText('Memorias RAM');
    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Memorias RAM');
  });

  test('TC_DOM_016 [@P2] Error Guessing: imágenes con texto alternativo descriptivo', async ({ page }) => {
    const alternativeTexts = await page.locator('img').evaluateAll(images =>
      images.map(image => image.getAttribute('alt')?.trim() ?? ''),
    );

    expect(alternativeTexts.length).toBeGreaterThan(0);
    expect(alternativeTexts.every(text => text.length > 0)).toBe(true);
    expect(alternativeTexts).toContain('Logo de la empresa');
    expect(alternativeTexts).toContain('Memoria RAM');
    expect(alternativeTexts).toContain('Procesador CPU');
    expect(alternativeTexts).toContain('Notebooks');
  });

  test('TC_DOM_017 [@P2] Error Guessing: controles con nombre accesible y operación por teclado', async ({ page }) => {
    const slideTwo = pageObject.slideIndicator(pageObject.primaryCarousel, 2);
    await expect(slideTwo).toBeVisible();
    await slideTwo.focus();
    await expect(slideTwo).toBeFocused();
    await page.keyboard.press('Enter');

    await expect(pageObject.activeSlideTitle(pageObject.primaryCarousel)).toHaveText('Procesadores');
    await expect(pageObject.primaryCarousel.getByRole('button', { name: 'Siguiente' })).toBeVisible();
    await expect(pageObject.primaryCarousel.getByRole('button', { name: 'Anterior' })).toBeVisible();
  });

  test('TC_DOM_018 [@P2] Partición de Equivalencia: encabezados y regiones semánticas', async ({ page }) => {
    await expect(page.getByRole('heading', { name: 'TECH SOLUCIONES', level: 1 })).toBeVisible();
    await expect(page.getByRole('heading', { name: 'Inicio', level: 2 })).toBeVisible();
    await expect(page.getByRole('heading', {
      name: 'Promociones Exclusivas y Experiencia de Compra Única',
      level: 2,
    })).toBeVisible();
    await expect(page.getByRole('banner')).toBeVisible();
    await expect(page.getByRole('navigation')).toBeVisible();
    await expect(page.getByRole('main')).toBeVisible();
    await expect(page.getByRole('contentinfo')).toBeVisible();
  });
});
