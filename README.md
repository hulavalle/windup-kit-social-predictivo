# Kit de analítica social y predictiva · Máster Técnico en Marketing Digital & IA

Este repositorio acompaña la clase de análisis de datos con IA (analítica de redes sociales) y análisis predictivo. En clase practicas con los datos de Café Fandango; el cuaderno lleva cada paso a tu proyecto, y la plantilla larga te sirve para aplicarlo de verdad cuando tengas datos.

## Antes de clase

Trae esto preparado. Si te falta algo, en clase vas por detrás.

| Qué necesitas | Para qué | Cómo se consigue |
| --- | --- | --- |
| Una cuenta de Google | Entrar en la cuenta de demostración de GA4 | [Crear una cuenta de Google](https://support.google.com/accounts/answer/27441?hl=es) |
| Acceso a la cuenta de demostración de GA4 de Google | La exploración en GA4 del paso 6 del cuaderno (propiedad Google Merchandise Store) | Gratis para cualquier cuenta de Google: [Cuenta de demostración](https://support.google.com/analytics/answer/6367342?hl=es) |
| Un asistente de IA: ChatGPT, Claude o Gemini, en plan gratuito | Las prácticas con IA (carpeta `prompts/`) | Crea la cuenta en [chatgpt.com](https://chatgpt.com/), [claude.ai](https://claude.ai/) o [gemini.google.com](https://gemini.google.com/) |
| Una hoja de cálculo con tablas dinámicas | Comprobar a mano dos cifras de cada práctica | [Google Sheets](https://docs.google.com/spreadsheets/) o Excel |
| Una cuenta de GitHub (opcional) | Crear tu copia del kit | [Crear una cuenta de GitHub](https://github.com/signup) |

El plan gratuito de los asistentes tiene límites de archivos adjuntos y de mensajes. Si llegas al límite en mitad de una práctica, cambia de asistente (los prompts sirven igual en los tres) o trabaja en pareja con un compañero.

## Por dónde empezar

1. **Crea tu copia del kit.** Entra en [github.com/hulavalle/windup-kit-social-predictivo](https://github.com/hulavalle/windup-kit-social-predictivo) y pulsa **Use this template** > **Create a new repository**. Ponle el nombre de tu proyecto y elige **Private**: tu copia va a tener datos de tu proyecto. Después, llévala a tu ordenador: en tu copia, pulsa **Code** > **Download ZIP** y descomprímelo, o clónala con GitHub Desktop. Trabaja sobre esa carpeta. Si no usas GitHub, pulsa el botón **Code** > **Download ZIP** y descomprímelo en tu ordenador.
2. **Abre `cuaderno/cuaderno-de-clase.docx` en el paso 0.**

## Si no estuviste en clase

Haz los pasos del cuaderno en orden. Cada paso trae Café Fandango resuelto, en la tienda y en las cafeterías. Las prácticas con IA tienen su prompt en `prompts/`:

- **Paso 0.** Tu modelo y tu pregunta. Sin prompt.
- **Pasos 1 y 2.** Práctica sin prompt. Rellena la columna `etapa_aarrr` de `datos/matriz_conversiones.csv` y mira qué etapa se queda sin evento. Después coloca las métricas de `datos/informe_redes_mensual.csv` en la cadena de valor del paso 2.
- **Paso 3.** `prompts/s1-b2-auditoria-utm.md`.
- **Pasos 4 y 5.** `prompts/s1-b3-valor-objetivos.md`.
- **Paso 6.** Práctica sin prompt, en la cuenta de demostración de GA4. Ve a **Explorar** > **Exploración de forma libre**. Pon en filas **Fuente/medio de la sesión** y en valores **Sesiones**, **Eventos clave** e **Ingresos totales**. Compara las cifras con **Informes** > **Adquisición** > **Adquisición de tráfico**.
- **Pasos 7 y 8.** `prompts/s1-b5-roi.md`.
- **Pasos 9 y 10.** Checklist de la sesión 1 y escalera de preguntas. Sin prompt.
- **Paso 11.** `prompts/s2-b1-cohortes.md`.
- **Paso 12.** `prompts/s2-b2-churn.md`. Descarga `riesgo.csv` y apunta el umbral de riesgo alto.
- **Paso 13.** `prompts/s2-b3-ltv.md`. En la tienda, descarga `riesgo_valor.csv`.
- **Paso 14.** `prompts/s2-b4-demanda.md`.
- **Pasos 15 y 16.** `prompts/s2-b5-activacion.md`.
- **Pasos 17 y 18.** Ficha de riesgos y checklist de la sesión 2. Sin prompt.

## Viene de la clase de GTM

Las prácticas no lo necesitan: `datos/` ya trae Café Fandango y su matriz está en `datos/matriz_conversiones.csv`. Para tu proyecto, los pasos 1 y 3 parten de [plan/matriz.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/matriz.csv) y [plan/utms.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/utms.csv) de tu copia del kit de la clase 1 ([windup-kit-medicion](https://github.com/hulavalle/windup-kit-medicion)). Si no la tienes, créala allí con **Use this template**.

## Qué hay dentro

| Carpeta o archivo | Qué es | Cuándo lo usas |
| --- | --- | --- |
| `datos/` | Los datos de Café Fandango en CSV y `diccionario.md`, que explica cada columna | En todas las prácticas |
| `prompts/` | Un prompt por práctica, para ChatGPT, Claude o Gemini | En las prácticas con IA |
| `cuaderno/` | `cuaderno-de-clase.docx`: los 19 pasos en versión corta. `cuaderno-de-clase.pdf`: el mismo cuaderno maquetado para imprimir. `plantilla-ecommerce.docx` y `plantilla-leadgen.docx`: los 19 pasos completos para proyectos reales. Sus fuentes en markdown están en `cuaderno/clase/` y `cuaderno/plantilla/` | El cuaderno de clase, en clase. La plantilla, después, con datos de tu proyecto |
| `mcp.md` | Cómo conectar tus redes, GA4, tu tienda o tu CRM a la IA (MCP): qué existe, en qué asistente funciona y con qué reglas | En tu proyecto, en lugar de exportar CSV |
| `chuleta.md` | AARRR, UTMs, fórmulas, cohortes, churn, APPA y el método de IA en una página | Para consultar |
| `plan/` | Plantillas en CSV para tu proyecto: objetivos, costes y backlog de experimentos (las filas que traen son ejemplos de Café Fandango: sustitúyelas) | Cuando lo apliques |
| `AGENTS.md` | Instrucciones para tu asistente de IA si trabajas el repositorio con él (`CLAUDE.md` y `GEMINI.md` remiten a él) | Con IA |
| `brain/` | La memoria del proyecto: qué es, qué se decidió y qué se aprendió | La lee tu asistente antes de trabajar |

## El caso: Café Fandango

Tienda online de café de especialidad con dos negocios, que son los dos modelos de los proyectos del máster:

- **Tienda (ecommerce):** compra suelta y suscripción mensual de 24 €.
- **Cafeterías (captación de leads):** formulario, llamada, prueba y pedido mensual.

Los datos van de junio de 2025 a noviembre de 2026 (noviembre está incompleto). Son inventados, pero con patrones reales que vas a descubrir.

## En clase

1. Cuando la slide diga «Cuaderno, paso N», abre ese paso en `cuaderno/clase/` o en `cuaderno-de-clase.docx`. Si no estuviste en clase, sigue «Si no estuviste en clase».
2. En las prácticas con IA, abre el prompt de `prompts/`, adjunta los CSV que pide y `datos/diccionario.md`. Algunas prácticas terminan con un archivo que descargas y adjuntas en la siguiente (`prompts/README.md`).
3. Comprueba siempre dos cifras a mano con una hoja de cálculo. En Excel no abras los CSV con doble clic, porque se descolocan las columnas y las tildes: usa **Datos** > **Obtener datos** > **Desde texto/CSV** (origen UTF-8, delimitador coma) y guarda como **CSV UTF-8 (delimitado por comas)**.

## Para tu proyecto

1. Trabaja en tu copia del repositorio (la que creaste en «Por dónde empezar»).
2. Sigue la plantilla de tu modelo de negocio (`cuaderno/plantilla/ecommerce/` o `cuaderno/plantilla/leadgen/`), partiendo de lo que rellenaste en clase.
3. Cuando tengas datos, expórtalos con identificadores seudónimos (sin nombres, emails ni teléfonos), escribe su diccionario y usa los mismos prompts cambiando los nombres de archivo y columnas. O conecta la fuente a tu asistente con un MCP (`mcp.md`): Metricool para tus redes, GA4, tu tienda o tu CRM, siempre en solo lectura.
4. Apunta objetivos, costes y experimentos en `plan/`.

## Regla de oro

La IA calcula; tú decides y compruebas. Ninguna cifra va a un informe sin haber verificado dos a mano, y ninguna acción se da por buena sin grupo de control.
