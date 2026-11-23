# Diccionario de datos · Café Fandango

Datos sintéticos del caso de la clase 2 (inventados, siempre los mismos). Periodo: junio de 2025 a noviembre de 2026; noviembre va en curso (datos hasta el día 21). Identificadores seudónimos: no hay nombres, emails ni teléfonos, así que se pueden subir a ChatGPT, Claude o Gemini.

Formato: CSV en UTF-8, separado por comas, punto decimal y fechas AAAA-MM-DD. En Google Sheets: Archivo > Importar. En Excel: Datos > Obtener datos > Desde texto/CSV, origen UTF-8 y delimitador coma.

## Supuestos del negocio

- Margen bruto: café suelto 45 %, suscripción 40 %, cafeterías (B2B) 35 %.
- Suscripción SUB-MES: 24 € al mes, dos bolsas de 250 g. El descuento de entrada solo se aplica al primer mes.
- Catálogo y UTMs: los de la clase 1 ([especificacion.md](https://github.com/hulavalle/windup-kit-medicion/blob/main/especificacion.md) y [plan/utms.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/utms.csv) del kit de la clase de GTM).
- Horas de community manager valoradas a 20 €/h.

## redes_posts.csv

Publicaciones de Café Fandango en Instagram, TikTok y LinkedIn, y las de la microinfluencer. Una fila por publicación. Métricas tal como las da cada plataforma.

Filas: 576.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `id_post` | texto | Identificador de la publicación |
| `fecha` | fecha | Día de publicación (AAAA-MM-DD) |
| `red` | texto | Instagram, TikTok o LinkedIn |
| `cuenta` | texto | marca (cuenta de Café Fandango) o laura-cafe (cuenta de la microinfluencer) |
| `carril` | texto | tienda o cafeterías: a qué negocio apunta la publicación |
| `formato` | texto | reel, carrusel, imagen, vídeo (TikTok) o post (LinkedIn) |
| `tipo_publicacion` | texto | orgánico, promocionado (con anuncio de Meta o LinkedIn) o influencer |
| `utm_campaign` | texto | Campaña del enlace (AAAA-MM_nombre) |
| `utm_content` | texto | Contenido del enlace: casa con utm_content de ga4_adquisicion.csv |
| `alcance` | entero | Cuentas únicas que vieron la publicación |
| `impresiones` | entero | Veces que se mostró |
| `me_gusta` | entero | Me gusta |
| `comentarios` | entero | Comentarios |
| `compartidos` | entero | Veces compartida |
| `guardados` | entero | Veces guardada |
| `clics_enlace` | entero | Clics en el enlace con UTM (bio, anuncio o post) |
| `coste_eur` | decimal | Coste en euros si es promocionada o de la influencer; 0 si es orgánica |

## informe_redes_mensual.csv

El informe mensual de redes que recibe la fundadora (el de las cifras «de vanidad»). Suma las publicaciones de la marca de redes_posts.csv.

Filas: 18.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `mes` | texto | Mes (AAAA-MM) |
| `mes_completo` | texto | sí o no (noviembre de 2026 va en curso) |
| `publicaciones` | entero | Publicaciones de la marca en el mes |
| `seguidores_nuevos` | entero | Seguidores ganados en el mes, sumando las tres redes |
| `seguidores_totales` | entero | Seguidores al cierre del mes, sumando las tres redes |
| `alcance` | entero | Suma del alcance de las publicaciones del mes |
| `impresiones` | entero | Suma de impresiones |
| `interacciones` | entero | Me gusta + comentarios + compartidos + guardados |
| `engagement_pct` | decimal | Interacciones / alcance × 100 |

## ga4_adquisicion.csv

Exportación tipo GA4 (informe de adquisición de tráfico, último clic) por mes, fuente/medio, campaña y contenido de la sesión. GA4 no ve todo: falta en torno a un 8 % de las conversiones (rechazo de cookies) y no ve las renovaciones de la suscripción, que se cobran solas.

Filas: 378.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `mes` | texto | Mes (AAAA-MM) |
| `utm_source` | texto | Fuente de la sesión |
| `utm_medium` | texto | Medio de la sesión |
| `utm_campaign` | texto | Campaña de la sesión ((organic) o (direct) si no hay UTM) |
| `utm_content` | texto | Contenido manual de la sesión ((not set) si no hay) |
| `grupo_canales` | texto | Agrupación de canales predeterminada de GA4 (Organic Social, Paid Social, Email, Organic Search, Direct) |
| `sesiones` | entero | Sesiones |
| `sesiones_con_interaccion` | entero | Sesiones con interacción |
| `add_to_cart` | entero | Eventos add_to_cart |
| `compras` | entero | Eventos purchase (compras sueltas y altas de suscripción) |
| `ingresos_compras` | decimal | Ingresos de esas compras en euros (con descuento, sin IVA) |
| `altas_suscripcion` | entero | Compras con item_category = Suscripción (incluidas en compras) |
| `leads` | entero | Eventos generate_lead (formulario de cafeterías) |

## costes.csv

Lo que cuesta estar en redes, por mes, red y concepto. Noviembre de 2026 va hasta el día 21.

Filas: 144.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `mes` | texto | Mes (AAAA-MM) |
| `red` | texto | Instagram, Facebook, TikTok o LinkedIn |
| `concepto` | texto | anuncios, influencer u horas |
| `carril` | texto | tienda o cafeterías |
| `detalle` | texto | Qué es exactamente |
| `horas` | entero | Horas de community manager (vacío si no son horas) |
| `euros` | decimal | Coste en euros (las horas, a 20 €/h) |

## utms_auditoria.csv

Veinte enlaces que la marca ha usado este mes en redes, anuncios y newsletter, tienda y cafeterías. Algunos están mal etiquetados.

Filas: 20.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `id_enlace` | texto | Identificador del enlace |
| `donde_se_usa` | texto | Dónde está publicado |
| `carril` | texto | tienda o cafeterías |
| `url_destino` | texto | Página de destino sin parámetros |
| `utm_source` | texto | Valor de utm_source (vacío si no lleva) |
| `utm_medium` | texto | Valor de utm_medium |
| `utm_campaign` | texto | Valor de utm_campaign |
| `utm_content` | texto | Valor de utm_content |
| `url_final` | texto | URL completa tal como está publicada |

## clientes.csv

Clientes de la tienda online captados entre junio de 2025 y el 21 de noviembre de 2026. Una fila por cliente. Identificadores seudónimos: no hay nombres, emails ni teléfonos.

Filas: 3.278.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `id_cliente` | texto | Identificador seudónimo (CLI-00042) |
| `fecha_alta` | fecha | Fecha de la primera compra |
| `utm_source` | texto | Fuente de la visita de la primera compra |
| `utm_medium` | texto | Medio |
| `utm_campaign` | texto | Campaña |
| `utm_content` | texto | Contenido |
| `red` | texto | Red o canal de captación según utm_source: Instagram, Facebook, TikTok, Newsletter, Google o Directo |
| `canal_captacion` | texto | Detalle: Instagram orgánico, Instagram influencer, Instagram anuncios, Facebook anuncios, TikTok orgánico, Newsletter, Google orgánico o Directo |
| `descuento_entrada_pct` | entero | Descuento de la primera compra: 0, 20 o 50 (%) |
| `tipo_primera_compra` | texto | suelta o suscripción |
| `importe_primera_compra` | decimal | Euros pagados en la primera compra |

## pedidos.csv

Pedidos de la tienda: compras sueltas y cobros mensuales de la suscripción. Una fila por pedido.

Filas: 9.144.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `id_pedido` | texto | Identificador del pedido |
| `id_cliente` | texto | Cliente (clientes.csv) |
| `fecha` | fecha | Fecha del pedido o del cobro |
| `tipo` | texto | suelta o suscripción |
| `item_id` | texto | ETI-250, COL-250, BRA-250, FAN-1KG o SUB-MES (catálogo de la clase 1) |
| `unidades` | entero | Unidades |
| `kg` | decimal | Kilos de café del pedido |
| `importe_bruto` | decimal | Precio por unidades, sin descuento |
| `descuento_pct` | entero | Descuento aplicado (%) |
| `importe` | decimal | Euros cobrados |
| `incidencia_soporte` | texto | sí si el cliente abrió una incidencia por ese pedido (retraso, bolsa dañada…) |

## suscripciones.csv

Historial mes a mes de cada suscripción (SUB-MES, 24 €/mes). Una fila por suscripción y mes, desde el mes de alta hasta el de la baja o noviembre de 2026.

Filas: 7.146.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `id_suscripcion` | texto | Identificador de la suscripción |
| `id_cliente` | texto | Cliente (clientes.csv) |
| `red` | texto | Red de captación del cliente |
| `canal_captacion` | texto | Canal de captación del cliente |
| `descuento_entrada_pct` | entero | Descuento del primer mes: 0, 20 o 50 (%) |
| `fecha_alta` | fecha | Fecha de alta |
| `fecha_baja` | fecha | Fecha de baja (vacía si sigue activa) |
| `mes` | texto | Mes de esta fila (AAAA-MM) |
| `meses_desde_alta` | entero | 0 = mes del alta |
| `entrega` | texto | entregada, saltada (el cliente pidió saltarse el mes), baja o pendiente (la renovación de noviembre aún no ha llegado) |
| `entrega_saltada` | entero | 1 si ese mes se saltó la entrega |
| `incidencias_soporte` | entero | Incidencias abiertas ese mes |
| `importe_cobrado` | decimal | Euros cobrados ese mes |
| `activa_al_cierre` | texto | sí o no: sigue activa al cierre del mes (en noviembre, al día 21) |

## leads.csv

Solicitudes del formulario de cafeterías (Fandango para cafeterías). Una fila por lead.

Filas: 829.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `id_lead` | texto | Identificador del lead |
| `fecha_lead` | fecha | Fecha del formulario |
| `utm_source` | texto | Fuente de la visita |
| `utm_medium` | texto | Medio |
| `utm_campaign` | texto | Campaña |
| `utm_content` | texto | Contenido |
| `red` | texto | Instagram, LinkedIn, Google o Directo |
| `canal_captacion` | texto | Detalle del canal |
| `n_locales` | entero | Locales que dice tener la cafetería |
| `estado` | texto | nuevo (sin contactar), cualificado (llamada hecha, en prueba), cliente o perdido |
| `fecha_cualificado` | fecha | Fecha en que pasó a cualificado (vacía si no llegó) |
| `fecha_cliente` | fecha | Fecha del primer pedido (vacía si no es cliente) |
| `fecha_perdido` | fecha | Fecha en que se dio por perdido |
| `motivo_perdida` | texto | Por qué se perdió |
| `id_cuenta` | texto | Cuenta de cafetería (cuentas_b2b.csv) si es cliente |

## cuentas_b2b.csv

Pedidos mensuales de cada cafetería cliente. Una fila por cuenta y pedido (como mucho uno al mes). Un mes sin fila es un mes sin pedido.

Filas: 810.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `id_cuenta` | texto | Identificador seudónimo de la cafetería (CAF-0031) |
| `id_lead` | texto | Lead de origen (leads.csv) |
| `red` | texto | Red de captación |
| `canal_captacion` | texto | Detalle del canal |
| `utm_source` | texto | Fuente del lead |
| `utm_medium` | texto | Medio del lead |
| `n_locales` | entero | Locales |
| `fecha_alta` | fecha | Fecha del primer pedido |
| `mes` | texto | Mes del pedido (AAAA-MM) |
| `meses_desde_alta` | entero | 0 = mes del primer pedido |
| `fecha_pedido` | fecha | Fecha del pedido |
| `kg` | decimal | Kilos de café |
| `importe` | decimal | Euros del pedido |

## ventas_semanales.csv

Kilos que salen del tostadero cada semana (lunes a domingo), tienda y cafeterías por separado. Incluye a clientes anteriores a junio de 2025 y pedidos fuera de estas tablas, así que no cuadra con la suma de pedidos.csv y cuentas_b2b.csv. La semana del 16 de noviembre de 2026 no está: va en curso.

Filas: 76.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `semana_inicio` | fecha | Lunes de la semana |
| `kg_tienda` | decimal | Kg vendidos en la tienda online |
| `kg_cafeterias` | decimal | Kg vendidos a cafeterías |
| `kg_total` | decimal | Suma de los dos |

## matriz_conversiones.csv

La matriz de conversiones de Café Fandango de la clase 1, con una columna nueva para rellenar en clase.

Filas: 10.

| Columna | Tipo | Significado |
| --- | --- | --- |
| `id … contrapeso` | texto | Las columnas de la matriz de la clase 1 ([plan/matriz.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/matriz.csv) del kit de la clase de GTM), sin cambios |
| `etapa_aarrr` | texto | Vacía: etapa del embudo AARRR de cada fila (Adquisición, Activación, Retención, Recomendación o Ingresos) |
