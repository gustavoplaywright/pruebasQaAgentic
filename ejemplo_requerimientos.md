# ESPECIFICACIÓN DE REQUERIMIENTOS DE SOFTWARE (SRS)

## Módulo: Autenticación y Seguridad

### RF-001: Registro de Nuevos Usuarios
**Descripción:** El sistema debe permitir el registro de nuevos usuarios mediante correo electrónico y contraseña segura.
- **Criterios de Aceptación:**
  1. El usuario debe ingresar un correo electrónico con formato válido (`usuario@dominio.com`).
  2. La contraseña debe tener una longitud mínima de 8 caracteres y máxima de 20 caracteres.
  3. La contraseña debe incluir al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (`!@#$%^&*`).
  4. Al registrarse correctamente, el sistema debe enviar un correo de confirmación con un enlace de activación vigente por 24 horas.
  5. Si el correo electrónico ya existe en la base de datos, el sistema debe mostrar un mensaje: "El correo ya se encuentra registrado".

### RF-002: Inicio de Sesión y Bloqueo de Cuenta por Intentos Fallidos
**Descripción:** El sistema debe autenticar a los usuarios registrados y proteger contra ataques de fuerza bruta.
- **Criterios de Aceptación:**
  1. El usuario ingresa correo y contraseña válidos y accede exitosamente a su panel principal.
  2. Si el usuario ingresa credenciales incorrectas, el sistema muestra: "Credenciales inválidas".
  3. Al acumular 3 intentos fallidos consecutivos, el estado de la cuenta cambia a "Bloqueada temporalmente" por un periodo de 15 minutos.
  4. Se debe enviar una notificación por correo electrónico alertando sobre el bloqueo de seguridad.
  5. No se debe permitir iniciar sesión mientras la cuenta permanezca en estado bloqueado.

---

## Módulo: Carrito de Compras y Checkout

### RF-003: Aplicación de Cupones de Descuento en Checkout
**Descripción:** El sistema debe validar y aplicar cupones promocionales sobre el total de la orden de compra antes del pago.
- **Reglas de Negocio:**
  - El cupón `DESCUENTO10` otorga un 10% de descuento y requiere un monto mínimo de compra de $50 USD.
  - El cupón `SUPER50` otorga un descuento fijo de $50 USD en compras iguales o superiores a $200 USD.
  - El monto máximo permitido por transacción en el checkout es de $10,000 USD.
  - No es posible combinar múltiples cupones en una misma orden de compra.
- **Criterios de Aceptación:**
  1. Si el cupón es válido y el carrito cumple el monto mínimo, el descuento se calcula y se refleja inmediatamente en el desglose de precios.
  2. Si el cupón ha expirado o no existe, se muestra el mensaje: "El cupón ingresado no es válido o ha expirado".
  3. Si el monto del carrito no alcanza el mínimo requerido para el cupón, se muestra: "Monto insuficiente para aplicar este cupón".

### RF-004: Carga de Imagen de Perfil de Usuario
**Descripción:** Los usuarios pueden personalizar su perfil cargando una fotografía representativa.
- **Criterios de Aceptación:**
  1. Formatos de archivo permitidos exclusivamente: `.jpg`, `.jpeg`, `.png`.
  2. El tamaño máximo del archivo de imagen no debe superar los 2 MB (2048 KB).
  3. Al cargar un archivo que no sea imagen o supere el límite de 2 MB, el sistema debe rechazar la carga y advertir al usuario con un mensaje comprensible.
  4. La imagen cargada exitosamente debe almacenarse y visualizarse inmediatamente en el avatar de usuario.

