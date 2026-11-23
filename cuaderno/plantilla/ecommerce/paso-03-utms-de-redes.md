# Paso 3. Convención de UTMs de redes

**Qué te llevas.** La lista cerrada de valores de UTM de tu tienda para orgánico, anuncios e influencers, un enlace etiquetado por cada origen y la auditoría mensual que encuentra los enlaces mal etiquetados.

## Por qué importa

Sin etiqueta, la venta existe pero no tiene padre. Un clic desde la bio de Instagram que no lleva UTM puede llegar a GA4 como Direct o como Referral, y esa compra no cuenta para Instagram.

GA4 asigna cada sesión a un canal con reglas fijas:

- **Organic Social**: la fuente está en la lista de redes sociales de GA4 (`instagram`, `facebook`, `tiktok`, `linkedin`, `pinterest`…) o el medio es `social`.
- **Paid Social**: la fuente está en esa lista y el medio es de pago, como `paid_social`, `cpc` o cualquier medio que empiece por `paid`.
- **Paid Other**: medio de pago con una fuente que no es una red. Es el cajón al que va un anuncio con una fuente inventada.
- **Direct**: sin fuente ni medio. Ahí caen los enlaces copiados en WhatsApp o en mensajes privados, lo que se llama dark social. La UTM es la única forma de rescatarlos.

GA4 distingue mayúsculas: `TikTok` y `tiktok` salen en filas distintas. Algunas redes, como X o Threads, pueden no estar en la lista de fuentes sociales: con `utm_medium=social` entran igual en Organic Social.

La convención de la clase 1 ya fijaba lo básico. Para una tienda real faltan dos cosas: una **lista cerrada** que nadie amplía sin acuerdo, y una **auditoría mensual**, porque los enlaces se rompen solos. Alguien copia un enlace viejo, una herramienta de enlaces en la bio cambia la fuente o una creadora escribe su nombre con tilde.

## Ejemplo con Café Fandango

*Ejemplo 3.1. La lista cerrada de Café Fandango*

| Parámetro | Valores permitidos | Regla |
| ------ | ------ | ------ |
| `utm_source` | `instagram`, `facebook`, `tiktok`, `linkedin`, `x`, `newsletter` | La red, nunca la herramienta |
| `utm_medium` | `social`, `paid_social`, `email` | `social` para orgánico e influencers; `paid_social` para anuncios |
| `utm_campaign` | `AAAA-MM_nombre`, `siempre_bio` | La fecha delante; `siempre_bio` para el enlace fijo de la bio |
| `utm_content` | `reel`, `carrusel`, `imagen`, `video`, `bio`, nombre de la creadora | Formato o creadora, en minúsculas y con guiones |

*Ejemplo 3.2. Enlaces de la tienda*

| Origen | `utm_source` | `utm_medium` | `utm_campaign` | `utm_content` | Canal GA4 |
| ------ | ------ | ------ | ------ | ------ | ------ |
| Reel de Instagram | `instagram` | `social` | `2026-11_navidad` | `reel` | Organic Social |
| Enlace de la bio | `instagram` | `social` | `siempre_bio` | `bio` | Organic Social |
| Microinfluencer | `instagram` | `social` | `2026-11_navidad` | `laura-cafe` | Organic Social |
| Vídeo de TikTok | `tiktok` | `social` | `2026-11_navidad` | `video` | Organic Social |
| Anuncio de Meta | `facebook` | `paid_social` | `{{campaign.name}}` | `{{ad.name}}` | Paid Social |

*Ejemplo 3.3. Errores típicos de una auditoría*

| Enlace | Dónde | Error | Corrección | Canal en GA4 con el error |
| ------ | ------ | ------ | ------ | ------ |
| `facebook / anuncio`, `2026-12_navidad` | Anuncio de Meta (carrusel) | `utm_medium=anuncio` no es un medio de pago | `facebook / paid_social` | Organic Social en lugar de Paid Social |
| `instagram / paid_social`, `rebajas` | Anuncio de rebajas | Campaña sin fecha: se mezcla con la del año anterior | `2027-01_rebajas` | Paid Social, pero sin distinguir el año |
| `metricool / social`, `2026-12_navidad` | Post programado en Instagram | La fuente es la herramienta (`metricool`) | `instagram / social` | Organic Social con fuente `metricool` |
| `reels / paid_social`, `2026-12_navidad` | Anuncio en reels de Instagram | Fuente `reels`, que no es una red, con medio de pago | `instagram / paid_social` | Paid Other |
| `instagram / social`, `utm_content=receta café` | Post con receta | Espacio y tilde en `utm_content` | `utm_content=receta-cafe` | Organic Social, pero no se agrupa con `receta-cafe` |
| `TikTok / social`, `2026-12_navidad` | Vídeo de TikTok | `utm_source` en mayúscula | `tiktok / social` | Organic Social, en una fila aparte |
| Sin UTM | Mensaje de difusión de WhatsApp | Sin UTM | `whatsapp / social` | Direct |

Son enlaces inventados para el ejemplo. Los de `datos/utms_auditoria.csv` los auditas tú en la práctica del bucle 2.

## Tu proyecto

1. Escribe tu lista cerrada (plantilla 3.1) con las redes de tu inventario del paso 0. Decide quién puede añadir un valor nuevo.
2. Fija la convención de `utm_campaign`: la fecha delante, `AAAA-MM_nombre`. Para enlaces fijos, como la bio, usa un nombre sin fecha que no cambie.
3. Escribe un enlace por origen (plantilla 3.2). Como mínimo: post orgánico, bio, anuncio e influencer si trabajas con ellos.
4. En Meta Ads, pon en **Parámetros de URL** del anuncio la fuente, el medio y las macros `{{campaign.name}}` y `{{ad.name}}`. Nombra campañas y anuncios en Meta con la misma convención: las macros copian esos nombres.
5. A cada influencer, dale su enlace hecho. No le pidas que lo monte: es donde aparecen las tildes y los espacios.
6. Si usas una herramienta de enlaces en la bio, pon la UTM en cada enlace de dentro con `utm_source=instagram`. La herramienta no es la fuente.
7. Copia la lista y los enlaces a [plan/utms.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/utms.csv) de tu copia del kit de la clase 1.
8. Monta la auditoría mensual (plantilla 3.3) y ponla en el calendario.

### La auditoría mensual, paso a paso

1. En GA4, ve a **Informes** > **Adquisición** > **Adquisición de tráfico**. Cambia la dimensión a **Fuente / medio de la sesión** y añade **Campaña de la sesión** como dimensión secundaria. Pon el último mes.
2. Exporta la tabla. Marca cada fila cuya fuente, medio o campaña no esté en tu lista cerrada.
3. Mira las filas de Paid Other, Referral y Direct con muchas sesiones. Suelen ser enlaces de redes mal etiquetados.
4. Busca el enlace que las genera: en los anuncios, en la bio, en las publicaciones de la influencer y en la newsletter.
5. Corrige el enlace y apunta la fecha. Los datos pasados no se corrigen en GA4: se quedan con el valor mal escrito.
6. Cruza con WooCommerce. En la atribución de pedidos, el origen de los pedidos del mes debería repartirse de forma parecida a GA4.

### Con tu asistente de IA

```text
Te adjunto dos archivos: la lista cerrada de valores UTM de mi tienda y una exportación
de GA4 con fuente/medio y campaña de la sesión del último mes. No hay datos personales.
Con código, marca cada fila cuyo utm_source, utm_medium o utm_campaign no esté en la lista,
y di en qué canal de GA4 cae por culpa del error y cuál sería el valor correcto.
Comprueba también mayúsculas, espacios, tildes y campañas sin la fecha AAAA-MM delante.
Devuelve una tabla: valor encontrado, sesiones, error, corrección, canal con el error.
```

Haz tres a mano antes de pedírselo a la IA. Así sabes si sus correcciones tienen sentido.

### Cómo comprobarlo

1. Abre cada enlace nuevo en una ventana de incógnito.
2. En GA4, **Informes** > **Tiempo real**: busca tu fuente, tu medio o tu campaña.
3. Al día siguiente, en **Adquisición de tráfico**, comprueba que la sesión está en el canal esperado.

*Plantilla 3.1. Tu lista cerrada*

| Parámetro | Valores permitidos | Regla | Quién puede añadir valores |
| ------ | ------ | ------ | ------ |
| `utm_source` | | | |
| `utm_medium` | | | |
| `utm_campaign` | | | |
| `utm_content` | | | |

*Plantilla 3.2. Tus enlaces*

| Origen | `utm_source` | `utm_medium` | `utm_campaign` | `utm_content` | Canal GA4 esperado |
| ------ | ------ | ------ | ------ | ------ | ------ |
| Post orgánico | | | | | |
| Enlace de la bio | | | | | |
| Anuncio | | | | | |
| Influencer | | | | | |
| | | | | | |
| | | | | | |

*Plantilla 3.3. Tu auditoría mensual*

| Valor encontrado | Dónde está el enlace | Error | Corrección | Canal con el error | Fecha de corrección |
| ------ | ------ | ------ | ------ | ------ | ------ |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

## Errores frecuentes

- Poner como fuente la herramienta (`later`, `metricool`) en lugar de la red.
- Usar `utm_medium=paid` con una fuente que no está en la lista social. Cae en Paid Other.
- Mayúsculas, espacios y tildes. Cada variante es una fila distinta en GA4.
- Poner UTMs en enlaces internos de la tienda, como un banner de la portada. GA4 empieza una sesión nueva con esa campaña y pierdes la fuente real.
- Corregir el enlace y no apuntarlo. En la siguiente auditoría no sabrás desde cuándo está bien.

## Antes de seguir

- [ ] Ningún valor de tu lista lleva mayúsculas, espacios ni tildes.
- [ ] La fuente es siempre la red, nunca la herramienta.
- [ ] Los anuncios llevan un medio de pago y las macros de la plataforma.
- [ ] Cada influencer tiene su enlace hecho.
- [ ] Cada enlace nuevo aparece en GA4 en el canal esperado.
- [ ] La auditoría mensual está en el calendario, con responsable.
