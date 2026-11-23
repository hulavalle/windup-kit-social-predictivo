# Paso 5. Valor de cada objetivo

**Qué te llevas.** El valor en euros de cada objetivo de tu tienda con su fórmula y sus fuentes, el valor de cada etapa del embudo de compra y la rutina para actualizarlos cada trimestre.

## Por qué importa

Si un objetivo no tiene valor en euros, no puede entrar en el ROI del paso 7. Y si cada objetivo lleva un valor inventado, el ROI también es inventado. El valor se calcula con datos de la tienda: ticket, margen y tasas de paso.

Hay tres tipos de objetivo en una tienda:

- **Compra.** Su valor es el margen del pedido: ticket medio × margen bruto. Nunca el ingreso entero: el café también cuesta.
- **Pasos intermedios**, como añadir al carrito o suscribirse a la newsletter. Su valor es la probabilidad de que acaben en compra × el valor de la compra.
- **Notoriedad**, como las impresiones orgánicas. Su valor es lo que costaría comprarlas: impresiones orgánicas / 1.000 × CPM medio de tus anuncios en redes. Se llama valor de medios propios.

Un caso especial es la **suscripción**. Su valor «hoy» es el primer pago por el margen, pero el suscriptor paga cada mes mientras se queda. Ese valor se queda corto, y lo corriges en el paso 13 con el LTV.

Los valores cambian: suben los precios, cambia el margen, cambian las tasas de paso. Un valor de hace un año da un ROI de hace un año. Por eso se revisan cada trimestre.

## Ejemplo con Café Fandango

*Ejemplo 5.1. Valor de los objetivos de la tienda*

| Objetivo | Fórmula | Datos | Valor | De dónde sale |
| ------ | ------ | ------ | ------ | ------ |
| Venta suelta (cliente de Instagram) | Ticket medio de la primera compra suelta × margen | 17,51 € × 45 % | 7,88 € | `clientes.csv` (junio de 2025 a octubre de 2026) y margen del diccionario |
| Alta de suscripción | Primer pago × margen | 24 € × 40 % | 9,60 €, menos si entra con descuento | Precio de la suscripción y margen |
| Notoriedad | Impresiones orgánicas / 1.000 × CPM de paid social | `redes_posts.csv` y facturas de Meta | Se calcula con tus impresiones y tu CPM | Plataformas |
| Suscriptor de la newsletter | Tasa de paso a compra × margen medio de la compra | El caso no trae datos de la newsletter | Queda como fórmula | Herramienta de email y WooCommerce |

El ticket medio de la primera compra suelta cambia por red: 17,51 € en Instagram, 18,17 € en Facebook y 10,93 € en TikTok. Si das un valor único a todas las ventas, TikTok sale mejor de lo que es.

*Ejemplo 5.2. Valor por etapa del embudo de compra*

| Etapa | Evento | Tasa de paso a compra | Valor de la compra | Valor de la etapa |
| ------ | ------ | ------ | ------ | ------ |
| Ficha vista | `view_item` | Compras / sesiones con `view_item` | 7,88 € | Tasa × 7,88 € |
| Carrito | `add_to_cart` | Compras / sesiones con `add_to_cart` | 7,88 € | Tasa × 7,88 € |
| Pago iniciado | `begin_checkout` | Compras / sesiones con `begin_checkout` | 7,88 € | Tasa × 7,88 € |
| Compra | `purchase` | 100 % | 7,88 € | 7,88 € |

Las tasas salen de GA4 (`ga4_adquisicion.csv` trae sesiones, `add_to_cart` y compras por fuente y mes). Cuanto más cerca de la compra, más vale el paso.

## Tu proyecto

1. Lista tus objetivos del paso 4 en la plantilla 5.1.
2. Para la compra, saca de WooCommerce el ticket medio del último trimestre: **WooCommerce** > **Análisis** > **Ingresos** o **Pedidos**. Usa el importe sin IVA y después de descuentos. Si puedes, sácalo por canal de captación.
3. Pide a finanzas el margen bruto por tipo de producto. Si no lo tienes, usa el de tu categoría más vendida y escríbelo como supuesto.
4. Para la suscripción, escribe el primer pago × margen y añade «se corrige en el paso 13».
5. Para los pasos intermedios, saca de GA4 la tasa de paso a compra (plantilla 5.2). En una exploración de embudo, pon los pasos `view_item`, `add_to_cart`, `begin_checkout` y `purchase`, y lee el porcentaje de cada paso que acaba en compra.
6. Para la notoriedad, suma las impresiones orgánicas del mes en las plataformas y multiplica por tu CPM medio de anuncios en redes / 1.000. Si no haces anuncios, usa el CPM que te daría Meta en una campaña de alcance de prueba y apúntalo como supuesto.
7. Escribe de dónde sale cada dato. Si una cifra no tiene fuente, no es un valor.
8. Si quieres que GA4 y Google Ads usen estos valores, el evento `purchase` ya lleva `value`. Para los pasos intermedios, decide si les das valor en Google Ads o si los dejas como métricas de seguimiento: en las pujas, solo optimiza por la compra.
9. Pon en el calendario la revisión trimestral (plantilla 5.3) y copia los valores a `plan/objetivos.csv`.

### Con tu asistente de IA

```text
Te adjunto un CSV con sesiones, add_to_cart, compras e ingresos por fuente y mes
(exportado de GA4, sin datos personales) y te digo mi margen bruto: [margen] %.
Con código, calcula para cada fuente:
1. Ticket medio = ingresos / compras.
2. Valor de una compra = ticket medio × margen.
3. Tasa de paso de add_to_cart a compra y el valor de un add_to_cart.
Enséñame las fórmulas y los supuestos. Usa solo meses completos.
```

Comprueba a mano el ticket medio de una fuente: ingresos entre compras en tu hoja de cálculo.

### Cómo comprobarlo

- El ticket medio de GA4 y el de WooCommerce deberían parecerse. Si difieren mucho, revisa si uno lleva IVA o gastos de envío y el otro no.
- El valor de un paso intermedio nunca puede ser mayor que el de la compra.

*Plantilla 5.1. El valor de tus objetivos*

| Objetivo | Fórmula | Datos | Valor | De dónde sale cada dato |
| ------ | ------ | ------ | ------ | ------ |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 5.2. Valor por etapa de tu embudo*

| Etapa | Evento | Tasa de paso a compra | Valor de la compra | Valor de la etapa |
| ------ | ------ | ------ | ------ | ------ |
| | | | | |
| | | | | |
| | | | | |
| Compra | `purchase` | 100 % | | |

*Plantilla 5.3. Revisión trimestral*

| Dato | Valor anterior | Valor nuevo | Fuente | Fecha | ¿Cambia algo en GA4 o Google Ads? |
| ------ | ------ | ------ | ------ | ------ | ------ |
| Ticket medio | | | | | |
| Margen bruto | | | | | |
| Tasa de paso de carrito a compra | | | | | |
| CPM medio de anuncios en redes | | | | | |
| Primer pago de la suscripción | | | | | |

## Errores frecuentes

- Usar el ingreso en lugar del margen. El ROI sale inflado.
- Un único ticket para todos los canales.
- Dar a un suscriptor el valor de su primer pago y olvidarlo. Es el error que corrige la sesión 2.
- Valores de notoriedad con un CPM que nadie ha pagado nunca.
- Dar valor a `add_to_cart` y a `purchase` en la misma campaña de Google Ads: se cuenta dos veces el mismo cliente.

## Antes de seguir

- [ ] Cada objetivo tiene fórmula, datos, valor y fuente.
- [ ] El valor usa el margen, no el ingreso.
- [ ] El valor de la suscripción está marcado para corregirlo en el paso 13.
- [ ] Tienes la tasa de paso a compra de cada etapa del embudo.
- [ ] La revisión trimestral está en el calendario.
