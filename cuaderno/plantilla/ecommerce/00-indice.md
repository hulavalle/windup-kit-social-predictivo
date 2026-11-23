# Plantilla para proyectos de ecommerce

Máster Técnico en Marketing Digital & IA · Análisis de datos con IA y análisis predictivo · 2026

Si estuviste en clase, ya tienes el cuaderno rellenado; si no, empieza aquí por el paso 0. Esta plantilla repite los diecinueve pasos en versión completa, para que apliques el método a una tienda online real fuera del máster: con sus datos, sus redes y su presupuesto. Si tu proyecto capta contactos, citas o presupuestos en vez de vender, usa la plantilla de captación de leads.

El ejemplo de cada paso es la tienda de Café Fandango: café de especialidad en compra suelta y una suscripción mensual de 24 €. Cuando hay que concretar menús o exportaciones, la tienda está en WordPress con WooCommerce, GTM4WP y GA4, como la dejaste en la clase 1. Todas las cifras del ejemplo salen de los CSV de la carpeta `datos/` del kit.

La sesión 1 responde a la pregunta de la fundadora: «¿Y esto cuánto café vende?». La sesión 2 responde a la segunda: «Me entero de que se van cuando ya se han ido». Al terminar la plantilla tendrás para tu tienda un informe de ROI por red con el valor de vida del cliente, una lista de clientes ordenada por riesgo, un plan de acción en el CRM y en paid media, y un experimento que demuestra si ese plan funciona.

*Plantilla A. Datos del proyecto*

| Campo | Tu respuesta |
| ---- | ------ |
| Proyecto | |
| Cliente o empresa | |
| URL de la tienda | |
| Plataforma (WordPress con WooCommerce u otra) | |
| Equipo | |
| Responsable del dato | |
| Asistente de IA que usáis (ChatGPT, Claude o Gemini) | |
| Fecha de entrega | |

## Cómo se usa

1. Sigue los pasos en orden. Cada paso usa lo que sale del anterior: el ROI necesita el valor de los objetivos, y el LTV necesita las cohortes y el churn.
2. Lee el ejemplo de Café Fandango antes de rellenar tu plantilla. Las plantillas tienen las mismas columnas que los ejemplos.
3. Cuando un paso pida un análisis, hazlo con tu asistente de IA y el método de los 4 pasos (paso 8): pregunta, datos, prompt y verificación. Los prompts de esta plantilla sirven igual en ChatGPT, Claude y Gemini.
4. Comprueba a mano dos cifras de cada análisis antes de copiarlas a la plantilla. Si no cuadran, no sigas.
5. Pasa el control de «Antes de seguir» al final de cada paso. Si una casilla queda sin marcar, vuelve atrás.
6. Si te falta espacio, añade filas en Word.

## Los pasos

| Paso | Qué te llevas | Sesión |
| --- | ------ | --- |
| 0. Tu modelo y tu pregunta sobre redes | Ficha, inventario de redes, presupuesto y quién decide | 1 |
| 1. Tu AARRR | Un evento por etapa y la columna `etapa_aarrr` en tu matriz | 1 |
| 2. La cadena de valor social | La cadena del post a la caja, métricas adelantadas y retrasadas e informe mensual | 1 |
| 3. Convención de UTMs de redes | Lista cerrada de valores, enlaces y auditoría mensual | 1 |
| 4. Objetivos por campaña | Campañas con objetivo, KPI y umbral, OKR trimestrales y contrapesos | 1 |
| 5. Valor de cada objetivo | Cada objetivo en euros, por etapa del embudo, y su revisión trimestral | 1 |
| 6. Pregunta y exploración en GA4 | Exploraciones de forma libre, de rutas y de atribución | 1 |
| 7. Costes y ROI | Coste completo, ROI, MER, incrementalidad e informe para la dirección | 1 |
| 8. Tu prompt de 4 pasos | Biblioteca de prompts y reglas de datos personales | 1 |
| 9. Checklist de la sesión 1 | Checklist del informe de ROI social | 1 |
| 10. Escalera de preguntas | Una pregunta por peldaño con los datos y el histórico que pide | 2 |
| 11. Cohorte y cliente activo | Definición de cohorte y de activo, matriz de retención y su rutina mensual | 2 |
| 12. Churn y señales | Definición de churn, señales, validación con meses guardados y lift por deciles | 2 |
| 13. LTV | LTV esperado por canal, ROI recalculado y pujas por valor | 2 |
| 14. Demanda | Previsión con rango, serie mínima y revisión mensual | 2 |
| 15. Plan de activación | Matriz riesgo × valor, campos y flujos del CRM y audiencias | 2 |
| 16. Ficha del experimento (APPA) | Backlog, ICE, ficha con grupo de control, tamaño de muestra y seguimiento | 2 |
| 17. Ficha de riesgos | Riesgos, consentimiento, transparencia y revisión del modelo | 2 |
| 18. Checklist de la sesión 2 | Checklist del informe completo y calendario de revisión | 2 |

Las fuentes de cada paso están en «Recursos», al final, con lo que aporta cada una. Del kit vas a usar:

- `chuleta.md`: las fórmulas en una página.
- `prompts/`: un prompt por práctica, que adaptas a tus archivos.
- `plan/objetivos.csv`, `plan/costes.csv` y `plan/backlog-appa.csv`: donde copias objetivos, costes y experimentos de tu tienda.
- `AGENTS.md` y `brain/`: las reglas y la memoria de tu asistente de IA si trabajas el repositorio con él.

## Los datos que vas a necesitar

| Fuente | Qué te da | Cómo la sacas |
| --- | ------ | ------ |
| Plataformas de redes (Meta Business Suite, TikTok, LinkedIn) | Alcance, impresiones, clics y gasto por publicación y por anuncio | Exportación a CSV de cada plataforma |
| GA4 | Sesiones, eventos clave e ingresos por fuente, medio, campaña y contenido | Exploración de forma libre, botón de exportar |
| WooCommerce | Pedidos, clientes, origen de cada pedido e importes reales | **WooCommerce** > **Pedidos** y los informes de **Análisis**, con su descarga a CSV |
| WooCommerce Subscriptions, si vendes suscripción | Altas, renovaciones, pausas y bajas de cada suscripción | Exportación de suscripciones a CSV |
| Herramienta de email o CRM | Aperturas, clics, campos del contacto y consentimiento | Exportación de contactos y de campañas |
| Hoja de costes | Gasto en anuncios, influencers, herramientas y horas | La mantienes tú, un registro por mes, red y concepto |

GA4 no ve todo. Pierde las compras de quien rechaza las cookies y no ve las renovaciones de la suscripción, que se cobran solas. Para los clientes y el dinero, la fuente es la tienda. GA4 te sirve para el canal y el comportamiento en la web.

## Una regla antes de empezar

A ningún asistente de IA se le suben nombres, emails, teléfonos ni direcciones. Antes de subir un CSV, cambia cada cliente por un identificador seudónimo, como `CLI-00042`, y guarda la tabla de correspondencia fuera de la IA. El paso 8 explica cómo.

## Vocabulario

| Término | Qué significa |
| --- | ------ |
| AARRR | Embudo de cinco etapas: Adquisición, Activación, Retención, Recomendación e Ingresos |
| Evento clave | Evento marcado en GA4 como conversión, como `purchase` |
| ROAS | Ingresos atribuidos / gasto en anuncios |
| ROI | (Ingresos atribuidos × margen − coste completo) / coste completo |
| MER | Ingresos totales de la tienda / gasto total en marketing |
| CAC | Coste completo / clientes nuevos captados |
| Cohorte | Grupo con un rasgo común, una acción y un momento: los que se suscribieron en marzo desde Instagram |
| Churn o baja | Cliente que deja de serlo: se da de baja de la suscripción o pasa demasiado tiempo sin comprar |
| LTV | Valor de vida del cliente: el margen que deja mientras sigue siendo cliente |
| Lift por deciles | Cuántas veces más bajas hay en el 10 % con más riesgo que en la media |
| Grupo de control (holdout) | Parte del segmento, elegida al azar, que no recibe la acción, para comparar |
| APPA | Analysis, Plan, Practice, Action: el método para convertir una predicción en una acción probada |
| ICE | Impacto × confianza × facilidad, de 1 a 10 cada uno, para priorizar |
