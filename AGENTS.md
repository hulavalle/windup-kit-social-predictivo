# Instrucciones para el asistente de IA

Trabajas en un repositorio de analítica de marketing: redes sociales, cohortes, churn, LTV, previsión y experimentos. La persona que te usa es de marketing, no programa. Explica cada paso en lenguaje llano y en español.

> **Para la persona:** estas instrucciones son para un agente de IA que trabaja sobre la carpeta del repositorio: lee sus archivos, calcula con código y escribe los resultados. Por ejemplo, Claude Code, Codex, Cursor o Gemini CLI. Codex y Cursor leen este archivo directamente; Claude Code y Gemini CLI lo cargan desde `CLAUDE.md` y `GEMINI.md`. Abre el agente en la raíz del repositorio. En el chat web de ChatGPT, Claude o Gemini no hace falta: usa los prompts de `prompts/` y adjunta los CSV.

## Memoria

- Antes de cualquier tarea, lee `brain/index.md` y los archivos que enlaza.
- Al terminar una sesión con cambios, apunta en `brain/decisiones.md` lo que se decidió y en `brain/aprendizajes.md` lo que salió mal y cómo se arregló. Una línea por entrada, sin datos personales.

## Datos

- Los datos están en `datos/` y su significado en `datos/diccionario.md`. Léelo antes de calcular nada.
- Calcula siempre con código y enseña el código, la fórmula y los supuestos. No des cifras de memoria.
- Nunca pidas ni proceses nombres, emails ni teléfonos. Si un archivo los trae, para y pide una versión con identificadores seudónimos.
- Respeta los periodos incompletos (el último mes) y no los trates como meses cerrados.
- Guarda lo que generes (`riesgo.csv`, `riesgo_valor.csv`, gráficos) en `salidas/`, nunca en `datos/`.

## Reglas de análisis

- ROI = (ingresos atribuidos × margen − coste completo) / coste completo. No lo confundas con el ROAS.
- En cohortes, las celdas que aún no han llegado van vacías, no en cero.
- En modelos predictivos, usa solo señales que se conocen antes del momento que se predice. Valida con meses guardados, no al azar, y da el lift por deciles además de la exactitud.
- En el LTV esperado, el margen es el de los clientes que siguen activos: no cuentes el riesgo dos veces.
- Toda previsión lleva rango. Toda propuesta de acción lleva cómo se comprobaría con un grupo de control, o por qué no hay volumen para hacerlo.

## Cuaderno

- La persona rellena los `.docx` a mano en Word. No ejecutes `cuaderno/construir_docx.py` ni edites `cuaderno/` salvo que te lo pida: regenerar sobrescribe los `.docx` y borra sus respuestas. Si te lo pide, dile antes que guarde una copia de su `.docx` con otro nombre.
- `cuaderno/cuaderno-de-clase.pdf` se maqueta en Figma a partir de `cuaderno/clase/`, no con `construir_docx.py`. Si cambias `cuaderno/clase/`, avisa de que el PDF hay que volver a exportarlo desde Figma.

## Límites

- Si tienes conectores MCP (redes, GA4, tienda, CRM), sigue las reglas de `mcp.md`: solo lectura, datos agregados y nada de datos personales. Antes de analizar, enseña la tabla que has traído y su número de filas.
- No crees, edites, publiques ni borres nada en una cuenta conectada sin que la persona lo pida y confirme esa acción concreta.
- No subas datos de clientes a servicios externos.
- Si los datos no permiten responder la pregunta, dilo en lugar de forzar una respuesta.
