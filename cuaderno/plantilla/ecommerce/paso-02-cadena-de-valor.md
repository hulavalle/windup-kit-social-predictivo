# Paso 2. La cadena de valor social

**Qué te llevas.** La cadena de tu tienda del post a la caja, con la métrica y la fuente de cada eslabón, las métricas adelantadas y retrasadas de cada objetivo y el diseño del informe mensual que sustituye al informe de vanidad.

## Por qué importa

Entre un post y un euro hay una cadena: impresión, interacción, clic, sesión, evento clave, cliente, ingreso y valor de vida. Cada eslabón lo mide una fuente distinta:

- La **plataforma** (Instagram, TikTok, Meta Ads) mide hasta el clic.
- **GA4** mide desde la sesión hasta el evento clave, si el enlace lleva UTM.
- La **tienda** mide el cliente, el ingreso real y si vuelve a comprar.

Si un eslabón no se mide, la cadena se rompe ahí y el informe se queda en el like. Un like vale cero euros hasta que la cadena llega a la caja.

Las métricas de arriba de la cadena son **adelantadas**: se mueven rápido y avisan. Las de abajo son **retrasadas**: tardan, pero son las que importan. Un buen informe junta las dos: la retrasada dice si el objetivo se cumplió y las adelantadas dicen a tiempo si va mal.

Un informe útil tiene pocas métricas. Con quince o treinta cifras en pantalla, nadie decide nada. Con tres a cinco, cada una ligada a una decisión, el informe se usa.

## Ejemplo con Café Fandango

*Ejemplo 2.1. La cadena de la tienda*

| Eslabón | Métrica | Fuente | ¿Se rompe aquí? |
| ------ | ------ | ------ | ------ |
| Impresión | Alcance e impresiones | Instagram, TikTok | No |
| Interacción | Me gusta, comentarios, guardados, compartidos | Instagram, TikTok | No |
| Clic | Clics en el enlace | Instagram, TikTok, Meta Ads | No |
| Sesión | Sesiones por fuente, medio y contenido | GA4 (UTMs) | Sí, si hay enlaces mal etiquetados (lo compruebas en el paso 3) |
| Evento clave | `purchase` | GA4 | En parte: falta cerca del 8 % de las compras por rechazo de cookies |
| Cliente | Clientes nuevos por canal de captación | WooCommerce | No |
| Ingreso | Ingresos de la primera compra | WooCommerce | No |
| Valor de vida | Margen mientras sigue activo | WooCommerce y suscripciones | Sí: nadie lo calcula hasta el paso 13 |

El informe que recibía la fundadora solo tenía los dos primeros eslabones: seguidores, engagement y alcance.

*Ejemplo 2.2. Métricas adelantadas y retrasadas*

| Objetivo | Métrica retrasada | Métricas adelantadas | Umbral de acción |
| ------ | ------ | ------ | ------ |
| Captar suscriptores desde Instagram | Altas de suscripción al mes y retención en el mes 3 | Clics en el enlace, sesiones con `add_to_cart`, clics en «Suscribirme» | Si las sesiones con `add_to_cart` caen dos semanas seguidas, revisar el contenido |
| Traer compradores nuevos desde TikTok | Clientes nuevos al mes y coste por cliente | Visualizaciones, clics, sesiones con `timer_5s` | Si el coste por cliente pasa de 5 € dos semanas, revisar los vídeos |

*Ejemplo 2.3. El informe mensual que sustituye al de vanidad*

| Bloque | Métrica | Fuente | Decisión que alimenta | Quién la mira |
| ------ | ------ | ------ | ------ | ------ |
| Dinero | ROI por red con coste completo | WooCommerce y hoja de costes | Reparto del presupuesto | Fundadora |
| Clientes | Clientes nuevos y altas de suscripción por red | WooCommerce | Qué red se empuja | Fundadora |
| Calidad | Retención en el mes 3 por red | Suscripciones | Si un canal trae clientes que no se quedan | Fundadora |
| Contenido | Compras y altas por contenido | GA4 | Qué formatos se repiten | Community manager |
| Alerta | Métricas adelantadas con su umbral | Plataformas y GA4 | Qué se corrige este mes | Community manager |

## Tu proyecto

1. Copia la cadena (plantilla 2.1). Para cada eslabón, escribe la métrica y la fuente que tienes hoy.
2. Marca dónde se rompe. Las roturas típicas de una tienda: enlaces sin UTM (la venta cae en Direct), compras sin consentimiento de cookies, y clientes que nadie sigue después de la primera compra.
3. Para cada rotura, escribe cómo la arreglas y en qué paso: UTMs en el 3, cohortes en el 11, LTV en el 13.
4. Toma los objetivos que vas a fijar en el paso 4. Para cada uno, escribe una o dos métricas retrasadas y de tres a cinco adelantadas (plantilla 2.2). Cada adelantada lleva un umbral que dispara una acción.
5. Diseña el informe mensual (plantilla 2.3). Como mucho cinco bloques. Cada métrica dice qué decisión alimenta y quién la mira. Si una métrica no alimenta ninguna decisión, sácala.
6. Decide el día del mes en que sale el informe y quién lo prepara.

### Con tu asistente de IA

```text
Te adjunto el informe de redes que se presenta hoy en mi tienda online.
Coloca cada métrica en un eslabón de esta cadena: impresión, interacción, clic,
sesión, evento clave, cliente, ingreso, valor de vida.
Marca los eslabones que no tienen ninguna métrica.
Después propón un informe de cinco métricas como máximo, cada una con la decisión
que alimenta y su fuente (plataforma, GA4 o tienda). No inventes cifras.
```

### Cómo comprobarlo

- Toma una semana cualquiera y sigue la cadena con números reales: clics en Instagram, sesiones de `instagram / social` en GA4, compras en GA4 y pedidos de esa fuente en WooCommerce.
- Si la caída de clics a sesiones es muy grande, sospecha de las UTMs o de la bio. Si la caída de compras en GA4 a pedidos en WooCommerce pasa de una de cada diez, revisa el consentimiento y el etiquetado.
- WooCommerce guarda el origen de cada pedido si tienes activada la atribución de pedidos (**WooCommerce** > **Ajustes** > **Avanzado** > **Características**). La caja de atribución del pedido trae el origen, el tipo de fuente, la campaña y el medio. Es la mejor forma de cruzar GA4 con la tienda.

*Plantilla 2.1. Tu cadena*

| Eslabón | Métrica | Fuente | ¿Se rompe aquí? | Cómo lo arreglas y en qué paso |
| ------ | ------ | ------ | -- | ------ |
| Impresión | | | | |
| Interacción | | | | |
| Clic | | | | |
| Sesión | | | | |
| Evento clave | | | | |
| Cliente | | | | |
| Ingreso | | | | |
| Valor de vida | | | | |

*Plantilla 2.2. Tus métricas adelantadas y retrasadas*

| Objetivo | Métrica retrasada | Métricas adelantadas | Umbral de acción |
| ------ | ------ | ------ | ------ |
| | | | |
| | | | |
| | | | |

*Plantilla 2.3. Tu informe mensual*

| Bloque | Métrica | Fuente | Decisión que alimenta | Quién la mira |
| ------ | ------ | ------ | ------ | ------ |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## Errores frecuentes

- Juntar en una cifra métricas de fuentes distintas sin decirlo. Las compras de GA4 y los pedidos de la tienda no coinciden, y no tienen por qué.
- Quedarse en el clic porque es lo último que da la plataforma.
- Informes con todas las métricas disponibles. El que lo lee no sabe cuál mirar.
- Métricas adelantadas sin umbral. Si nadie sabe cuándo preocuparse, avisan tarde.

## Antes de seguir

- [ ] Cada eslabón de tu cadena tiene métrica y fuente, o está marcado como roto.
- [ ] Cada rotura tiene un arreglo y el paso donde se hace.
- [ ] Cada objetivo tiene una métrica retrasada y al menos tres adelantadas con umbral.
- [ ] Tu informe mensual tiene cinco bloques como máximo, cada uno con su decisión.
- [ ] Sabes qué día sale el informe y quién lo prepara.
