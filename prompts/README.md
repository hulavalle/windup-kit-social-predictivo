# Prompts de las prácticas

Un archivo por práctica. Sirven igual en ChatGPT, Claude y Gemini: usa el que tengas. Copia el bloque del prompt, adjunta los archivos que pide y rellena lo que va entre corchetes.

`[Tienda]` y `[Cafeterías]` marcan bloques: deja el de tu carril y borra el otro, con su etiqueta. Donde pone `[archivo]` o `[archivos]`, escribe los nombres de los que adjuntas.

## Plan gratuito y archivos de una práctica a otra

- Las prácticas se hacen con el plan gratuito de ChatGPT, Claude o Gemini. El plan gratuito tiene límites de archivos adjuntos y de mensajes. Si llegas al límite, cambia de asistente (los prompts sirven en los tres) o trabaja en pareja con un compañero.
- La práctica de churn termina con `riesgo.csv` y la de LTV con `riesgo_valor.csv`. Descárgalos: la de activación adjunta `riesgo_valor.csv`. Apunta también el umbral de riesgo alto que da la práctica de churn: lo pide la de activación.
- Para descargar un archivo que genera la IA: la IA lo deja en su respuesta como un enlace o un archivo; púlsalo para descargarlo. Si solo te enseña el texto, pídele «Dame el archivo para descargar», o copia la tabla a tu hoja de cálculo y guárdala como CSV con ese nombre.

## Analizar con IA en 4 pasos

1. **Pregunta.** Escribe la pregunta de negocio y la decisión que permite tomar antes de abrir los datos.
2. **Datos.** Adjunta los CSV de `datos/` que pide la práctica y `datos/diccionario.md`, que explica cada columna. Nunca subas nombres, emails ni teléfonos: los datos de Café Fandango usan identificadores seudónimos y los de tu proyecto también deberían.
3. **Prompt.** Rol, datos, pregunta y formato de salida. Pide siempre que calcule con código y no de memoria, y que enseñe la fórmula y los supuestos.
4. **Verificar.** Comprueba dos cifras a mano con una tabla dinámica o un filtro en tu hoja de cálculo. Después pregunta a la IA qué no sabe o qué supuestos ha tenido que hacer.

## Si la IA se equivoca

- **Inventa columnas o cifras.** Pídele que liste las columnas que ha leído y el número de filas de cada archivo antes de calcular.
- **Calcula sin código.** Repite: «Calcula con código y enséñame el código».
- **Da un número sin rango.** Pide el intervalo o el rango y cómo lo ha calculado.
- **Llama ROI al ROAS.** Pide la fórmula completa con el margen y el coste completo.

## Con datos conectados (MCP)

Si conectas tus redes, GA4, tu tienda o tu CRM a tu asistente (`mcp.md`), el prompt es el mismo: cambia solo el paso de los datos. En lugar de «Te adjunto clientes.csv», di qué tiene que traer el conector y de qué periodo, y pide que te enseñe la tabla antes de calcular. Solo lectura y nada de datos personales.

## Archivos

| Práctica | Archivo |
| --- | --- |
| Sesión 1 · Bucle 2 · Auditoría de UTMs | `s1-b2-auditoria-utm.md` |
| Sesión 1 · Bucle 3 · Valor de los objetivos | `s1-b3-valor-objetivos.md` |
| Sesión 1 · Bucle 5 · ROI por red | `s1-b5-roi.md` |
| Sesión 2 · Bucle 1 · Matriz de cohortes | `s2-b1-cohortes.md` |
| Sesión 2 · Bucle 2 · Modelo de churn | `s2-b2-churn.md` |
| Sesión 2 · Bucle 3 · LTV y ROI recalculado | `s2-b3-ltv.md` |
| Sesión 2 · Bucle 4 · Previsión de demanda | `s2-b4-demanda.md` |
| Sesión 2 · Bucle 5 · Activación y experimento | `s2-b5-activacion.md` |
