# Paso 2. La cadena de valor social

**Qué te llevas.** La cadena completa del post al pedido mensual, con la métrica, la fuente y la clave que une cada eslabón con el siguiente; las métricas adelantadas y retrasadas de cada objetivo; y el diseño del informe mensual de redes.

## Para qué sirve

Cada eslabón tiene su fuente. La plataforma mide hasta el clic. GA4 mide desde la sesión hasta el lead. El CRM mide la cualificación, el cliente y el ingreso. Si dos eslabones seguidos no comparten un dato que los una, la cadena se rompe ahí y el informe de redes se queda en el like.

En captación de leads la cadena es más larga que en una tienda, y se rompe casi siempre en el mismo sitio: entre GA4 y el CRM. El lead llega al CRM sin saber de qué red vino. La solución es que el formulario guarde las UTMs en campos ocultos y que el CRM las guarde con el lead. Así, cada cliente lleva su red de origen.

Las métricas de arriba de la cadena son adelantadas: se mueven rápido y avisan. Las de abajo son retrasadas: tardan meses, pero son las que pagan. Un buen informe enseña las dos y no confunde una con otra.

## Cómo se hace

1. Escribe los eslabones de tu cadena: impresión, interacción, clic, sesión, lead, cualificado, cliente, ingreso recurrente y valor de vida.
2. Para cada eslabón, escribe la métrica y la fuente.
3. Entre cada par de eslabones, escribe la clave que los une: las UTMs, el identificador del lead, el de la cuenta.
4. Marca dónde se rompe hoy. Si es entre GA4 y el CRM, pide a quien gestiona la web que el formulario envíe `utm_source`, `utm_medium`, `utm_campaign` y `utm_content` en campos ocultos.
5. Para cada objetivo, separa las métricas adelantadas de las retrasadas.
6. Diseña el informe mensual: una sección por etapa AARRR, de arriba abajo, y una decisión al final.

### Con tu asistente de IA

Adjunta un export del CRM con identificadores seudónimos y pide: «Dime qué porcentaje de leads tiene `utm_source` vacío, por mes. Enséñame el código». Si más de uno de cada diez llega sin fuente, la cadena se rompe entre la web y el CRM.

### Cómo comprobarlo

Cuenta a mano los leads de un mes en GA4 (`generate_lead`) y en el CRM. No coincidirán del todo: GA4 pierde los que rechazan cookies y el CRM recibe leads por teléfono. Si la diferencia pasa de un 15 %, busca la causa antes de seguir.

## Ejemplo con Fandango para cafeterías

*Ejemplo 2.1. La cadena de cafeterías*

| Eslabón | Métrica | Fuente | Clave con el siguiente |
| --- | --- | --- | --- |
| Impresión | Alcance e impresiones | Instagram, LinkedIn | `utm_content` del enlace |
| Interacción | Comentarios, guardados, compartidos | Instagram, LinkedIn | |
| Clic | Clics en el enlace | Instagram, LinkedIn | UTMs en la URL |
| Sesión | Sesiones por fuente/medio y contenido | GA4 | UTMs |
| Lead | `generate_lead` | GA4 y CRM | UTMs en campos ocultos del formulario |
| Cualificado | Leads cualificados | CRM | `id_lead` |
| Cliente | Cafeterías cliente | CRM | `id_cuenta` |
| Ingreso recurrente | Pedidos de cada mes | Pedidos de la cuenta | `id_cuenta` |
| Valor de vida | LTV de la cuenta | Hoja de cálculo | |

En el caso, `leads.csv` trae las UTMs de cada lead y `cuentas_b2b.csv` el lead de origen de cada cuenta: la cadena no se rompe.

*Ejemplo 2.2. Métricas adelantadas y retrasadas*

| Objetivo | Métricas adelantadas | Métricas retrasadas |
| --- | --- | --- |
| Conseguir cafeterías cliente con LinkedIn Ads | Clics, leads, tasa de cualificación | Clientes, coste por cliente |
| Que las cafeterías sigan pidiendo | Pedidos por debajo del 80 % de su media | Cuentas que piden en el mes 6, LTV |
| Que Instagram traiga leads que encajan | Leads «no es una cafetería» al mes | Tasa de cierre de Instagram |

*Ejemplo 2.3. El informe mensual de cafeterías*

| Sección | Qué enseña | Fuente |
| --- | --- | --- |
| Adquisición | Sesiones y clics por red y contenido | Plataformas y GA4 |
| Ingresos (lead) | Leads, cualificados y clientes por red, con sus tasas | CRM |
| Coste | Coste por lead, por cualificado y por cliente | Costes y CRM |
| Retención | Cuentas activas, cuentas que dejan de pedir, señales | Pedidos de la cuenta |
| Valor | LTV por red y ROI | Hoja de cálculo |
| Decisión | Una propuesta para el mes siguiente | Equipo |

Comparado con el informe que recibía la fundadora (+2.300 seguidores, 4,1 % de engagement y 180.000 de alcance en octubre), este informe empieza por arriba y termina en euros.

## Tu proyecto

*Plantilla 2.1. Tu cadena*

| Eslabón | Métrica | Fuente | Clave con el siguiente | ¿Se rompe aquí? |
| --- | --- | --- | --- | -- |
| Impresión | | | | |
| Interacción | | | | |
| Clic | | | | |
| Sesión | | | | |
| Lead | | | | |
| Cualificado | | | | |
| Cliente | | | | |
| Ingreso recurrente | | | | |
| Valor de vida | | | | |

*Plantilla 2.2. Métricas adelantadas y retrasadas por objetivo*

| Objetivo | Métricas adelantadas | Métricas retrasadas |
| --- | --- | --- |
| | | |
| | | |
| | | |

*Plantilla 2.3. Tu informe mensual*

| Sección | Qué enseña | Fuente | Quién lo prepara |
| --- | --- | --- | --- |
| Adquisición | | | |
| Activación | | | |
| Ingresos (lead) | | | |
| Coste | | | |
| Retención | | | |
| Valor | | | |
| Decisión | | | |

## Errores frecuentes

- Un informe que termina en el lead. Sin cualificados ni clientes, gana la red que trae contactos baratos.
- UTMs que se pierden en el formulario. Si el formulario está en otra página o el lead vuelve otro día, las UTMs de la primera visita se pierden si nadie las guarda.
- Mezclar las cifras de GA4 y del CRM en la misma columna. Son fuentes distintas: di siempre de cuál sale cada número.
- Celebrar una métrica adelantada como si fuera un resultado. Más leads no es más clientes.

## Antes de seguir

- [ ] Cada eslabón tiene métrica y fuente.
- [ ] Hay una clave entre GA4 y el CRM, o una tarea para crearla.
- [ ] Sabes qué porcentaje de leads llega al CRM sin fuente.
- [ ] Cada objetivo tiene al menos una métrica adelantada y una retrasada.
- [ ] El informe mensual termina en una decisión.
