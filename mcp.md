# Conectar tus datos a la IA (MCP)

En clase subes un CSV. En tu proyecto, la IA puede traer los datos directamente de tus redes, de GA4, de tu tienda o de tu CRM con un **servidor MCP** (Model Context Protocol): un conector que le da acceso a una herramienta. Esta guía dice cuáles existen hoy, cuáles sirven para orgánico, en qué asistente funcionan y con qué reglas se usan.

Revisado en noviembre de 2026. Esto cambia cada pocos meses: comprueba el enlace antes de conectar nada.

## Antes de empezar: qué asistente lo admite

| Asistente | Conectores MCP en la web | Plan |
| --- | --- | --- |
| Claude | Sí: conectores oficiales y personalizados (URL remota) en claude.ai. Los servidores locales, solo en Claude Desktop | También en el plan gratuito (un conector personalizado) |
| ChatGPT | Sí, solo remotos y solo en la web (no en el móvil) | Completo en Business, Enterprise y Edu; en Pro, solo lectura; en Plus, sin confirmar |
| Gemini | Muy limitado: solo en Gemini Spark, con disponibilidad fuera de EE. UU. sin confirmar | De pago |

Si tu asistente no admite el conector que necesitas, exporta el CSV desde la herramienta y súbelo: los prompts de `prompts/` funcionan igual.

## Ocho reglas

1. **Solo lectura.** Activa el modo de solo lectura del conector si lo tiene, o usa un usuario con permisos de lectura.
2. **Cuentas de prueba** para practicar. Nunca la cuenta de un cliente sin su permiso.
3. **Nada de datos personales.** Pide datos agregados (por red, por mes, por segmento), no listas de personas.
4. **Un usuario por servicio**, con los permisos mínimos.
5. **Revisa cada llamada** que hace el asistente y no marques «permitir siempre» en acciones que escriben, publican o borran.
6. **Desconfía del contenido**: un texto dentro de los datos puede intentar dar instrucciones a la IA.
7. **Solo conectores oficiales** o de proveedores conocidos. Nada que pida tu contraseña o tu cookie de sesión.
8. **Al terminar**, revoca el acceso desde la herramienta.

## Sesión 1 · Redes sociales

### Una herramienta para todas las redes (orgánico)

| Herramienta | Redes | Qué trae | Solo lectura | Coste | Enlace |
| --- | --- | --- | --- | --- | --- |
| **Metricool** (recomendada) | Instagram, Facebook, TikTok, LinkedIn, X, YouTube, Pinterest, Threads, Bluesky, Twitch | Rendimiento orgánico por publicación y analítica de anuncios de Meta, Google y TikTok | No: también puede programar publicaciones | Cualquier plan, incluido el gratuito (30 días de analítica) | https://ai.metricool.com/mcp |
| **Buffer** | Instagram, Facebook, LinkedIn, X, Threads, Bluesky, Mastodon, TikTok, YouTube, Pinterest, Google Business, Substack | Publicaciones y métricas orgánicas | No: puede borrar publicaciones | Todos los planes (gratuito: últimos 31 días) | https://mcp.buffer.com/mcp |
| **Windsor.ai** | Instagram, Facebook, TikTok, YouTube, LinkedIn, Threads, Google Business | Datos orgánicos para análisis | No | Gratis con 1 fuente y 30 días; de pago desde 19 USD/mes | https://mcp.windsor.ai/social_media |

Hootsuite, Agorapulse y Supermetrics también tienen conector, pero piden planes de pago o tienen cobertura poco clara.

### Canal por canal

| Canal | Orgánico | Anuncios |
| --- | --- | --- |
| **Instagram y Facebook** | No hay MCP oficial de Meta para orgánico. Usa Metricool o Windsor (cuenta profesional o de creador) | **Meta Ads MCP, oficial** (`mcp.facebook.com/ads`). Puede crear, editar y borrar: úsalo solo para leer informes |
| **LinkedIn** | No hay MCP oficial. Windsor o Supermetrics, o exporta el CSV de la página | No hay MCP oficial: exporta el CSV de Campaign Manager |
| **TikTok** | Sin MCP oficial: Metricool o Windsor | **TikTok for Business MCP, oficial**, con conector en Claude |
| **X** | **MCP oficial** (`api.x.com/mcp`) con `?read_only=true`. La API se paga por uso: unos 0,005 USD por post leído. Pon un tope de gasto | — |
| **Substack** | **MCP oficial**, pero solo para publicaciones Bestseller. Si no es tu caso, exporta el CSV de estadísticas del panel | — |
| **YouTube y Pinterest** | Metricool o Windsor | El MCP oficial de Pinterest está anunciado pero sin disponibilidad confirmada |

### Analítica web y anuncios de Google

| Herramienta | Para qué | Oficial | Solo lectura | Enlace |
| --- | --- | --- | --- | --- |
| Google Analytics MCP | Informes de GA4 por canal, campaña y contenido (tus UTMs) | Sí | Sí por defecto | https://github.com/googleanalytics/google-analytics-mcp |
| Google Ads MCP | Campañas, costes y conversiones | Sí | Configurable: algunas herramientas escriben | https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server |

El MCP de Google Analytics se instala en tu ordenador (no es un conector de la web): pide algo de configuración técnica.

## Sesión 2 · Histórico de clientes y activación

| Herramienta | Para qué | Solo lectura | Enlace |
| --- | --- | --- | --- |
| **BigQuery MCP** (oficial de Google) | Cohortes, churn y LTV con SQL sobre la exportación de GA4 o de tu tienda. El MCP de Google Analytics no tiene cohortes ni valor de vida | Sí, con la herramienta de solo lectura y un rol de lector | https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp |
| **Shopify** (conector oficial para Claude) | Pedidos y clientes de una tienda Shopify | Sí, salvo que apruebes escritura | https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/shopify-connector-for-claude |
| **PrestaShop MCP** (oficial) | Pedidos y clientes de PrestaShop | No | https://docs.mcp.prestashop.com/ |
| WooCommerce (MCP Adapter) | Pedidos de WooCommerce. En vista previa para desarrolladores: espera a que madure | No | https://developer.woocommerce.com/docs/features/mcp/ |
| **Klaviyo MCP** (oficial) | Segmentos, campañas y métricas de email | Sí, con `read-only=true` | https://developers.klaviyo.com/en/docs/klaviyo_mcp_server |
| **HubSpot MCP** (oficial) | Contactos, negocios y empresas del CRM | No: usa una cuenta de prueba | https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server |
| Attio MCP (oficial) | CRM | No (las escrituras piden confirmación) | https://docs.attio.com/mcp/overview |

Leer sí; escribir (crear un segmento, lanzar una campaña), solo con permiso y viendo cada acción en pantalla.

## Cómo cambian los prompts

Los prompts de `prompts/` sirven igual. Cambia solo el paso de los datos: en lugar de «Te adjunto clientes.csv», escribe qué tiene que traer el conector y para qué periodo, y pide que te enseñe la tabla antes de calcular.

```
Con el conector de Metricool, trae el rendimiento orgánico de mis publicaciones de Instagram,
TikTok y LinkedIn de los últimos 90 días: fecha, red, formato, alcance, interacciones, guardados
y clics en el enlace. No traigas datos de personas. Enséñame la tabla y el número de filas
antes de analizar nada. Después, [pega aquí el resto del prompt de la práctica].
```

Y verifica igual que con un CSV: dos cifras comparadas con el panel de la herramienta.
