# Paso 8. Tu prompt de 4 pasos

**Qué te llevas.** Tus análisis con IA hechos con el método de los 4 pasos, una biblioteca de prompts de tu tienda que reutilizas cada mes y las reglas de datos personales que sigue todo el equipo.

## Por qué importa

La IA calcula en segundos; tú respondes de que la cifra es cierta. Analizar con IA tiene cuatro pasos, y funciona igual en ChatGPT, Claude y Gemini:

1. **Pregunta.** La pregunta de negocio y la decisión que permite tomar, escritas antes de abrir los datos.
2. **Datos.** El CSV con su diccionario de columnas, sin datos personales.
3. **Prompt.** Rol, datos, pregunta, formato de salida, «calcula con código» y «enséñame la fórmula y los supuestos».
4. **Verificación.** Dos cifras comprobadas a mano y la pregunta «¿qué no sabes?».

Pedir que calcule con código importa. Sin código, el asistente puede dar una cifra que suena bien y no sale de tus datos. Con código, ves qué columnas usó y cómo.

Una tienda repite los mismos análisis cada mes: ROI por red, auditoría de UTMs, cohortes, bajas. Si cada mes escribes el prompt de cero, cada mes sale distinto. Una **biblioteca de prompts** guarda la versión que funciona con sus cifras de control.

Y los datos de tus clientes no son tuyos para subirlos a cualquier sitio. Las **reglas de datos personales** dicen qué se sube, qué no y cómo se prepara un archivo antes.

## Ejemplo con Café Fandango

*Ejemplo 8.1. El análisis de ROI con los 4 pasos*

| Paso | Qué hizo Café Fandango |
| ------ | ------ |
| Pregunta | ¿Qué red tiene mejor ROI por primera compra? Para decidir cómo repartir el presupuesto de redes |
| Datos | `clientes.csv`, `costes.csv` y `diccionario.md`, con identificadores seudónimos |
| Prompt | Rol de analista, la pregunta, «calcula con código», tabla por red con fórmula y supuestos |
| Verificación | Clientes de TikTok (1.007) y coste de Instagram (12.943 €), con una tabla dinámica |
| Qué falló la IA | Llamó ROI al ROAS: no restaba el coste ni aplicaba el margen |

*Ejemplo 8.2. La biblioteca de prompts de la tienda*

| Análisis | Cada cuánto | Archivos | Prompt | Cifras de control |
| ------ | ------ | ------ | ------ | ------ |
| Auditoría de UTMs | Cada mes | Exportación de GA4 y lista cerrada | `prompts/s1-b2-auditoria-utm.md`, adaptado | Número de valores fuera de la lista |
| ROI por red | Cada mes | Clientes y costes | `prompts/s1-b5-roi.md`, adaptado | Clientes de una red y coste de otra |
| Cohortes por canal | Cada mes | Suscripciones | `prompts/s2-b1-cohortes.md`, adaptado | Una celda de la matriz, como la cohorte de junio de 2025 en el mes 6: 56,0 % |
| Riesgo de baja | Cada mes | Suscripciones | `prompts/s2-b2-churn.md`, adaptado | Churn del decil de más riesgo frente a la media |
| LTV por canal | Cada trimestre | Clientes, pedidos y suscripciones | `prompts/s2-b3-ltv.md`, adaptado | LTV de un canal rehecho a mano |
| Previsión de demanda | Cada mes | Ventas semanales | `prompts/s2-b4-demanda.md`, adaptado | Error medio en las semanas guardadas |

## Tu proyecto

1. Rehaz tu primer análisis con los 4 pasos (plantilla 8.1). Escribe la pregunta y la decisión antes de exportar nada.
2. Prepara los datos:
   - Exporta solo las columnas que necesitas. Para el ROI no hacen falta nombres, direcciones ni notas del pedido.
   - Cambia el email o el ID de cliente de WooCommerce por un identificador seudónimo, como `CLI-00042`. En la hoja de cálculo: lista de clientes únicos, una columna con `CLI-` y un número correlativo, y un BUSCARV para sustituirlo en las demás hojas.
   - Guarda la tabla de correspondencia (cliente real y seudónimo) en un archivo aparte que nunca subes.
   - Escribe el diccionario: una línea por columna con su significado, como `diccionario.md` del kit.
3. Escribe el prompt con las seis piezas: rol, datos que adjuntas, pregunta, formato de salida, «calcula con código» y «enséñame la fórmula y los supuestos».
4. Pide primero que liste las columnas y el número de filas que ha leído. Si no coinciden con tu archivo, para.
5. Verifica dos cifras a mano (plantilla 8.4). Elige una que la IA pueda haber hecho mal, como un total con filtro.
6. Pregunta al final: «¿Qué supuestos has hecho y qué no puedes saber con estos datos?».
7. Guarda en la biblioteca (plantilla 8.2) el prompt que funcionó, con la fecha y sus cifras de control. El mes que viene usas el mismo y comparas.
8. Escribe las reglas de datos personales del equipo (plantilla 8.3) y compártelas.

### Antes de subir un archivo

- Usa la cuenta de empresa del asistente, si la tenéis, y revisa en su configuración si los datos se usan para entrenar modelos. Desactívalo si se puede.
- Abre el CSV y busca `@`, números de teléfono y nombres de calle. Los campos libres, como las notas del pedido o los mensajes de soporte, suelen esconder datos personales.
- Si trabajas el repositorio del kit con tu asistente, `AGENTS.md` ya le prohíbe procesar nombres, emails y teléfonos. Añade tus reglas a `brain/decisiones.md`.

*Plantilla 8.1. Tu análisis con los 4 pasos*

| Paso | Qué hiciste |
| ------ | ------ |
| Pregunta y decisión | |
| Datos (archivos y diccionario) | |
| Prompt | |
| Verificación (dos cifras) | |
| Qué falló la IA | |
| Qué no sabe la IA con estos datos | |

*Plantilla 8.2. Tu biblioteca de prompts*

| Análisis | Cada cuánto | Archivos | Prompt (versión y fecha) | Cifras de control |
| ------ | ------ | ------ | ------ | ------ |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 8.3. Tus reglas de datos personales*

| Dato | ¿Se sube a la IA? | Cómo se trata |
| ------ | -- | ------ |
| Nombre y apellidos | No | Se borra la columna |
| Email | No | Se cambia por un identificador seudónimo |
| Teléfono | No | Se borra la columna |
| Dirección | No | Se deja como mucho la provincia, si hace falta |
| Notas del pedido y mensajes de soporte | No | Se borran o se resumen en una categoría (retraso, bolsa dañada) |
| ID de pedido y de cliente de WooCommerce | | |
| Importes, fechas, productos, UTMs | | |

*Plantilla 8.4. Tu verificación*

| Cifra de la IA | Cómo la compruebas | Valor a mano | ¿Cuadra? |
| ------ | ------ | ------ | -- |
| | | | |
| | | | |

## Errores frecuentes

- Pedir el análisis sin pregunta: la IA te devuelve todo lo que se puede calcular.
- Aceptar una cifra sin código.
- Subir la exportación de clientes tal cual sale de WooCommerce, con emails y direcciones.
- Cambiar el prompt cada mes y comparar resultados que no se calcularon igual.
- No preguntar qué no sabe. La IA no te dirá sola que le falta el mes en curso o que GA4 no ve las renovaciones.

## Antes de seguir

- [ ] Tu análisis tiene la pregunta y la decisión escritas antes.
- [ ] El archivo que subiste no tenía datos personales.
- [ ] Comprobaste dos cifras a mano.
- [ ] El prompt que funcionó está en la biblioteca con fecha y cifras de control.
- [ ] El equipo conoce las reglas de datos personales.

## Datos conectados (MCP)

Cuando tu proyecto tenga datos, la IA puede traerlos sin exportar: un conector MCP le da acceso a la herramienta. El prompt es el mismo; cambia solo el paso de los datos: di qué tiene que traer el conector y de qué periodo, y pide que te enseñe la tabla antes de calcular.

- Redes en orgánico: Metricool (casi todas las redes, también en el plan gratuito) o Buffer.
- Anuncios: los MCP oficiales de Meta Ads, TikTok Ads y Google Ads. Escriben: úsalos solo para leer.
- GA4: el MCP oficial de Google Analytics, de solo lectura.
- Histórico de clientes: BigQuery, tu tienda o tu CRM, en solo lectura o en una cuenta de prueba.

Antes de conectar nada, comprueba que tu asistente lo admite (Claude, en la web; ChatGPT, según el plan; Gemini, casi no) y sigue las ocho reglas de `mcp.md`: solo lectura, nada de datos personales y revisar cada llamada.
