/**
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
