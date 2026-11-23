# Paso 3. Convención de UTMs de redes

**En la práctica del bucle 2 · tu proyecto.** Escribe tu convención para orgánico, anuncios e influencers y cinco enlaces.

GA4 clasifica una sesión como Organic Social si la fuente está en su lista de redes o el medio es `social`, y como Paid Social si la fuente es una red y el medio es de pago (`paid_social`, `cpc`). Todo en minúsculas, sin espacios ni tildes: GA4 distingue mayúsculas. La campaña empieza por la fecha: `AAAA-MM_nombre`.

*Ejemplo 3.1. Convención de Café Fandango*

| Origen | `utm_source` | `utm_medium` | `utm_campaign` | `utm_content` | Canal GA4 |
| ------ | ------ | ------ | ------ | ------ | ------ |
| Post de Instagram | `instagram` | `social` | `2026-11_navidad` | `reel` | Organic Social |
| Enlace de la bio | `instagram` | `social` | `siempre_bio` | `bio` | Organic Social |
| Microinfluencer | `instagram` | `social` | `2026-11_navidad` | `laura-cafe` | Organic Social |
| Anuncio de Meta | `facebook` | `paid_social` | `{{campaign.name}}` | `{{ad.name}}` | Paid Social |
| Anuncio de LinkedIn (cafeterías) | `linkedin` | `paid_social` | `2026-11_cafeterias-linkedin` | `anuncio-prueba-gratis` | Paid Social |

*Plantilla 3.1. Tu convención y cinco enlaces*

| Origen | `utm_source` | `utm_medium` | `utm_campaign` | `utm_content` | Canal GA4 |
| ------ | ------ | ------ | ------ | ------ | ------ |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

- [ ] Ningún valor lleva mayúsculas, espacios ni tildes.
- [ ] La fuente es la red, no la herramienta.
- [ ] Los anuncios llevan un medio de pago y las macros de la plataforma.

Versión completa: el paso 3 de tu plantilla añade la lista cerrada de valores y la auditoría mensual de enlaces.
