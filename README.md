Repositorio de pruebas de practicas con agentes y mcp.

Estructuración y Creación de Skills (SKILL.md)

Creamos la carpeta base qa-agentic-framework y la estructura de carpetas en el workspace.

Definimos e implementamos las 3 Skills agénticas fundamentales:

qa-test-case-creator: Diseñada para analizar requerimientos/historias de usuario y generar matrices de prueba exhaustivas (Happy Path, Negativos, Edge Cases y Formato Markdown).

qa-web-playwright-automation: Criterios y patrones para automatización E2E Web con Playwright, TypeScript y Page Object Model (POM).

qa-api-playwright-automation: Reglas para automatización de servicios REST/SOAP usando APIRequestContext de Playwright, validando códigos de estado, esquemas JSON y SLA de respuesta.

Configuración del Servidor MCP (Model Context Protocol)

Configuramos el servidor MCP de filesystem (@modelcontextprotocol/server-filesystem) en tu settings.json de VS Code para que Copilot pueda leer y ejecutar las skills del workspace nativamente.

Ajustamos los permisos de confirmación ("chat.tools.confirmExecution": "never") y el modo autónomo en la interfaz para permitir que el agente lea archivos y ejecute comandos en la consola sin interrupciones manuales constantes.

Generación e Integración de Pruebas de API (pets-demo)

Conectamos la skill de API con la API real [https://pets-demo.onrender.com/pets](https://pets-demo.onrender.com/pets).

El agente inspeccionó de forma autónoma el endpoint en vivo y generó:

El servicio encapsulado (services/PetsService.ts).

La suite de pruebas completa (tests/api/pets.spec.ts) cubriendo el CRUD completo (GET, POST, PUT, PATCH, DELETE), aserciones de contrato JSON, Type Guards, Type Narrowing y medición de SLA de respuesta.

Resolución de Incompatibilidades y Entorno de Ejecución

Corregimos los comandos de consola para Windows CMD/PowerShell (npm init playwright@latest -y).

Resolvimos la falta de tipos globales instalando @types/node y typescript localmente (npx tsc --init), corrigiendo el error Cannot find name 'process'.

Exploración Web y Generación de Casos E2E

Diseñamos las estrategias y prompts específicos para que las Skills exploren componentes DOM web (como tu sitio [https://gustavoplaywright.github.io/playgroundweb/](https://gustavoplaywright.github.io/playgroundweb/)) y construyan matrices de prueba e interfaces POM autónomamente.

Limpieza del Repositorio y Subida a GitHub (pruebasQaAgentic)

Configuramos las reglas recursivas en .gitignore (**/node_modules/, test-results/, etc.) para evitar trackear archivos pesados de dependencias.

Limpiamos el caché del índice de Git (git rm -r --cached **/node_modules).

Renombramos la rama local de master a main (git branch -M main) y publicamos la versión limpia y funcional del repositorio remoto en GitHub (git push -u origin main).
