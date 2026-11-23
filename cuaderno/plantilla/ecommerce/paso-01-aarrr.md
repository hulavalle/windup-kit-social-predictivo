# Paso 1. Tu AARRR

**Qué te llevas.** El embudo AARRR de tu tienda con un evento o dato por etapa, la columna `etapa_aarrr` en tu matriz de conversiones de la clase 1 y la etapa que priorizas este trimestre.

## Por qué importa

En la clase 1 la matriz de conversiones dijo qué medir. AARRR dice en qué momento del crecimiento está cada evento:

- **Adquisición.** ¿De dónde llegan? Una sesión con su fuente y su medio.
- **Activación.** ¿Tienen una primera experiencia de valor? Ver una ficha, leer una guía, añadir al carrito.
- **Retención.** ¿Vuelven? Segunda compra o renovación de la suscripción.
- **Recomendación.** ¿Traen a otros? Compartir o usar un código de amigo.
- **Ingresos.** ¿Pagan, y cuánto con el tiempo? La compra y lo que deja el cliente mientras sigue.

Si una etapa no tiene evento, no la estás midiendo. Y si casi todos tus eventos caen en Activación, tu medición mira la parte alta del embudo y no ve si el cliente vuelve.

En una tienda hay un problema extra: GA4 ve la web, pero no ve todo lo que pasa después. La renovación de una suscripción se cobra sola, sin visita, y GA4 no se entera. La Retención y los Ingresos a lo largo del tiempo salen de WooCommerce, no de GA4.

## Ejemplo con Café Fandango

*Ejemplo 1.1. La matriz de Café Fandango, lista para su etapa AARRR*

| id | Evento | Etapa AARRR |
| -- | ------ | ------ |
| 1 | Ve el listado de cafés (`view_item_list`) | |
| 2 | Abre la ficha de un café (`view_item`) | |
| 3 | Añade un café al carrito (`add_to_cart`) | |
| 4 | Lee la guía de preparación, 75 % de scroll (`page_read`) | |
| 5 | Pasa 5 segundos en la ficha de un café (`timer_5s`) | |
| 6 | Clic en «Suscribirme» del hero (`cta_click`) | |
| 7 | Empieza el pago (`begin_checkout`) | |
| 8 | Compra un café (`purchase`) | |
| 9 | Se suscribe al plan mensual (`purchase`) | |
| 10 | Envía el formulario para cafeterías (`generate_lead`) | |

La columna Etapa AARRR la rellenas tú en la práctica del bucle 1, en `datos/matriz_conversiones.csv`. Al rellenarla, responde tres preguntas:

- ¿Qué etapa se queda sin ninguna fila? ¿Es porque GA4 ya la mide sola o porque nadie la mide?
- ¿Cuántas filas caen en cada etapa? ¿Qué parte del embudo mira la medición?
- ¿Dónde está la Retención: en GA4 o en la tienda?

*Ejemplo 1.2. El AARRR completo de la tienda*

| Etapa | Evento o dato | Métrica | Fuente | ¿Se mide hoy? |
| ------ | ------ | ------ | ------ | -- |
| Adquisición | `session_start` con UTM de Instagram o TikTok | Sesiones por fuente, medio y contenido | GA4 | Sí |
| Activación | Las filas de la matriz en Activación | % de sesiones con al menos un evento de activación | GA4 | |
| Retención | Renovación de la suscripción, segunda compra suelta | % de suscriptores activos en el mes 3 por canal | WooCommerce | Sí, pero nadie lo mira |
| Recomendación | Las filas de la matriz en Recomendación | Clientes que traen a otro cliente | | |
| Ingresos | Las filas de la matriz en Ingresos | Ingresos de la primera compra y valor de vida | GA4 y WooCommerce | |

Las celdas vacías salen de la práctica del bucle 1.

*Ejemplo 1.3. La etapa que prioriza Café Fandango*

| Campo | Café Fandango |
| ------ | ------ |
| Etapa | Retención |
| Por qué | Se sabe qué red trae la primera compra, pero no qué red trae clientes que se quedan |
| Métrica que la sigue | % de suscriptores activos en los meses 1, 3, 6 y 12 desde el alta, por canal |
| Qué cambia primero | Mirar las bajas cada mes por canal de captación (pasos 11 y 12) |

## Tu proyecto

1. Abre tu matriz de conversiones de la clase 1 ([plan/matriz.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/matriz.csv) de tu copia del kit de la clase 1).
2. Añade una columna `etapa_aarrr` al final. Pon en cada fila una de las cinco etapas. Usa siempre las mismas palabras: Adquisición, Activación, Retención, Recomendación o Ingresos.
3. Cuenta cuántas filas tiene cada etapa. Una etapa sin filas es una etapa que no mides.
4. Rellena el AARRR completo (plantilla 1.1). Para Adquisición basta con las UTMs. Para Retención e Ingresos a lo largo del tiempo, escribe de qué parte de WooCommerce sale el dato: pedidos, clientes o suscripciones.
5. Para cada etapa sin medir, propón un evento o un dato. En una tienda WooCommerce, la Recomendación se mide con un cupón por cliente o un plugin de recomendación: el pedido lleva el código y sabes quién trajo a quién.
6. Elige una etapa para este trimestre (plantilla 1.3). La que más duele, no la más fácil de medir.

### Con tu asistente de IA

```text
Te adjunto la matriz de conversiones de mi tienda online (CSV, sin datos personales).
Añade una columna etapa_aarrr con uno de estos valores: Adquisición, Activación,
Retención, Recomendación o Ingresos. Justifica cada fila en una frase.
Después dime qué etapas no tienen ninguna fila y propón un evento o un dato
de la tienda para medirlas. No cambies las demás columnas.
```

Revisa cada fila. La IA tiende a poner en Ingresos eventos que todavía no traen dinero. Pregúntate en cada uno: ¿ya ha pagado?

### Cómo comprobarlo

- En GA4, **Administrar** > **Eventos**: cada evento de tu matriz aparece con su nombre exacto.
- En WooCommerce, filtra los pedidos de un cliente que ya ha comprado dos veces. Si los ves, tienes el dato de Retención aunque GA4 no lo tenga.
- Si vendes suscripción, en la lista de suscripciones de WooCommerce Subscriptions cada una tiene su estado: activa, en espera, pendiente de cancelación, cancelada o caducada. De ahí sale la Retención.

*Plantilla 1.1. Tu AARRR*

| Etapa | Evento o dato | Métrica | Fuente | ¿Se mide hoy? |
| ------ | ------ | ------ | ------ | -- |
| Adquisición | | | | |
| Activación | | | | |
| Retención | | | | |
| Recomendación | | | | |
| Ingresos | | | | |

*Plantilla 1.2. Tu matriz con la etapa AARRR*

| id | Evento | Macro o micro | Etapa AARRR |
| -- | ------ | ------ | ------ |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*Plantilla 1.3. La etapa que priorizas*

| Campo | Tu proyecto |
| ------ | ------ |
| Etapa | |
| Por qué | |
| Métrica que la sigue | |
| Qué cambia primero | |

## Errores frecuentes

- Poner una etapa por evento sin pensar en el cliente. La misma compra es Ingresos la primera vez y Retención la segunda.
- Dar por medida la Retención porque GA4 tiene el informe de retención. Ese informe cuenta visitas que vuelven, no clientes que vuelven a pagar.
- Dejar la Recomendación para más adelante. Un cliente que trae a otro vale más que su ticket, y sin dato no lo verás en el LTV del paso 13.
- Priorizar Adquisición por costumbre. Si tus clientes no vuelven, traer más es llenar un cubo con agujeros.

## Antes de seguir

- [ ] Cada fila de tu matriz tiene su etapa AARRR.
- [ ] Sabes qué etapas no tienen evento y tienes una propuesta para cada una.
- [ ] La Retención y los Ingresos a lo largo del tiempo dicen de dónde salen (WooCommerce, suscripciones o CRM).
- [ ] Has elegido una etapa para este trimestre y la métrica que la sigue.
