# Paso 3. Convención de UTMs de redes

**Qué te llevas.** Tu convención de UTMs para orgánico, anuncios, influencers, email y offline; la lista cerrada de valores permitidos; la comprobación de que las UTMs llegan al CRM; y la auditoría mensual de enlaces.

## Para qué sirve

Sin UTMs, el lead existe pero no se sabe de qué red viene. GA4 clasifica una sesión como Organic Social si la fuente está en su lista de redes o el medio es `social`, y como Paid Social si la fuente es una red y el medio es de pago (`paid_social`, `cpc`). Mensajería, enlaces copiados y aplicaciones sin UTM caen en Direct.

GA4 distingue mayúsculas: `LinkedIn` y `linkedin` son dos fuentes. Por eso todo va en minúsculas, sin espacios ni tildes. La campaña empieza por la fecha, `AAAA-MM_nombre`, para que la campaña de este noviembre no se mezcle con la del anterior.

En captación de leads, la convención tiene una segunda misión: las UTMs tienen que llegar al CRM con el lead. Es lo que permite calcular, meses después, cuántos clientes y cuánto ingreso trajo cada red.

## Cómo se hace

1. Escribe la lista cerrada de `utm_source`: una por red o plataforma, nunca la herramienta (`hootsuite`, `metricool`).
2. Escribe la lista cerrada de `utm_medium`: `social` para orgánico e influencers, `paid_social` para anuncios en redes, `email` para la newsletter.
3. Fija la regla de `utm_campaign`: `AAAA-MM_nombre`, o `siempre_nombre` para enlaces fijos como el de la bio.
4. Fija la regla de `utm_content`: formato o pieza (`reel-cafeterias`, `anuncio-prueba-gratis`), o el nombre de la creadora.
5. En los anuncios, usa las macros de la plataforma para no escribir a mano.
6. Para los QR de folletos y ferias, usa una fuente que diga dónde estaba el QR y el medio `qr`. Caerá fuera de los canales sociales, y está bien: no es una red.
7. Pide que el formulario guarde las UTMs en campos ocultos y que el CRM las conserve. Haz un envío de prueba con un enlace etiquetado y búscalo en el CRM.
8. Cada mes, audita los enlaces publicados.

### Con tu asistente de IA

Usa el prompt de `prompts/s1-b2-auditoria-utm.md` con tu lista de enlaces. Pide que compare cada enlace con tu lista cerrada y que diga, para cada error, en qué canal de GA4 caería. Comprueba a mano tres enlaces: cópialos en el navegador y míralos en el informe Tiempo real de GA4.

### Cómo comprobarlo

Abre un enlace corregido y busca la sesión en Tiempo real con el canal esperado. Después envía el formulario de prueba y comprueba que el lead aparece en el CRM con sus cuatro UTMs.

## Ejemplo con Fandango para cafeterías

*Ejemplo 3.1. Convención del carril de cafeterías*

| Origen | `utm_source` | `utm_medium` | `utm_campaign` | `utm_content` | Canal GA4 |
| --- | --- | --- | --- | --- | --- |
| Reel de Instagram | `instagram` | `social` | `2026-11_cafeterias` | `reel-cafeterias` | Organic Social |
| Carrusel de Instagram | `instagram` | `social` | `2026-11_cafeterias` | `carrusel-cafeterias` | Organic Social |
| Post de LinkedIn | `linkedin` | `social` | `2026-11_cafeterias` | `post-caso-cliente` | Organic Social |
| Anuncio de LinkedIn | `linkedin` | `paid_social` | `2026-11_cafeterias-linkedin` | `anuncio-prueba-gratis` | Paid Social |
| Newsletter para cafeterías | `newsletter` | `email` | `2026-11_cafeterias` | `banner` | Email |

Todos apuntan a `/empresas.html`.

*Ejemplo 3.2. Lista cerrada de valores*

| Parámetro | Valores permitidos | Regla |
| --- | --- | --- |
| `utm_source` | `instagram`, `facebook`, `tiktok`, `linkedin`, `newsletter` | La red, nunca la herramienta |
| `utm_medium` | `social`, `paid_social`, `email` | Orgánico e influencer, `social`; anuncios, `paid_social` |
| `utm_campaign` | `AAAA-MM_nombre`, `siempre_bio` | Minúsculas y guiones; el carril va en el nombre (`_cafeterias`) |
| `utm_content` | Pieza o creadora: `reel-cafeterias`, `post-equipo`, `laura-cafe` | Sin espacios ni tildes |

*Ejemplo 3.3. Errores típicos de una auditoría*

| Error | Ejemplo | Corrección | Qué pasa en GA4 |
| --- | --- | --- | --- |
| Medio que no es de pago en un anuncio | `linkedin / anuncio` | `linkedin / paid_social` | Cae en Organic Social |
| Campaña sin fecha | `feria-hosteleria` | `2027-02_feria-hosteleria` | Se mezcla con la del año anterior |
| Fuente que es la herramienta | `hootsuite / social` | `linkedin / social` | El tráfico de LinkedIn va a hootsuite |
| Fuente que no es una red | `patrocinado` con medio de pago | `linkedin / paid_social` | Cae en Paid Other |
| Espacio y tilde | `menú degustación` | `menu-degustacion` | Llega codificado y no se agrupa |
| Mayúscula | `LinkedIn` | `linkedin` | Fila aparte de linkedin |
| Sin UTM | QR de un folleto | `folleto-feria / qr` | Direct |

Son ejemplos inventados. Los enlaces de `datos/utms_auditoria.csv` los auditas tú en la práctica del bucle 2.

## Tu proyecto

*Plantilla 3.1. Tu convención*

| Origen | `utm_source` | `utm_medium` | `utm_campaign` | `utm_content` | Canal GA4 |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Plantilla 3.2. Tu lista cerrada*

| Parámetro | Valores permitidos | Regla |
| --- | --- | --- |
| `utm_source` | | |
| `utm_medium` | | |
| `utm_campaign` | | |
| `utm_content` | | |

*Plantilla 3.3. Las UTMs en el CRM*

| Comprobación | Resultado | Fecha |
| --- | --- | --- |
| El formulario tiene los cuatro campos ocultos | | |
| El lead de prueba aparece en el CRM con sus UTMs | | |
| Los leads por teléfono o WhatsApp llevan un origen | | |
| % de leads del último mes sin `utm_source` | | |

*Plantilla 3.4. Auditoría mensual de enlaces*

| Enlace | Dónde se usa | Error | Corrección | Canal en GA4 con el error |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## Errores frecuentes

- Etiquetar los anuncios a mano. Usa las macros: no se equivocan con las mayúsculas.
- Cambiar la convención a mitad de año. Si cambias un valor, apúntalo y agrupa los dos en los informes.
- Usar UTMs en enlaces internos de tu web. Cortan la sesión y borran la fuente real.
- Olvidar los leads que no pasan por el formulario. Al que llama por teléfono, pregúntale cómo os conoció y apúntalo en el CRM con la misma lista de fuentes.

## Antes de seguir

- [ ] Ningún valor lleva mayúsculas, espacios ni tildes.
- [ ] La fuente es siempre la red, no la herramienta.
- [ ] Los anuncios llevan un medio de pago y las macros de la plataforma.
- [ ] El lead de prueba llegó al CRM con sus cuatro UTMs.
- [ ] La auditoría mensual tiene fecha y responsable.
