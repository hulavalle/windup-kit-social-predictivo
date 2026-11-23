# Paso 0. Tu modelo y tu pregunta sobre redes

**Qué te llevas.** La ficha de tu negocio de captación, el embudo con sus etapas y su fuente, el inventario de redes con lo que cuesta cada una, el presupuesto y quién decide, y de 3 a 5 preguntas de negocio, cada una con la decisión que cambia.

## Para qué sirve

En un negocio de captación de leads, la venta no ocurre en la web. La web recoge un contacto. El comercial lo llama, lo cualifica y, a veces, lo cierra. El ingreso llega después, y en muchos negocios llega cada mes mientras el cliente sigue. Si no dibujas ese recorrido antes de analizar, acabarás midiendo lo que la web ve (leads) y no lo que paga las facturas (clientes que siguen).

La pregunta va antes que los datos. Una buena pregunta lleva a una decisión: mover presupuesto de una red a otra, cambiar el formulario, cambiar a quién llama primero el comercial. Si nadie haría nada distinto con la respuesta, la pregunta sobra.

## Cómo se hace

1. Escribe qué vendes y cómo se cobra: pago único, cuota mensual, pedido recurrente sin contrato.
2. Dibuja tu embudo con cuatro etapas: lead, cualificado, cliente e ingreso recurrente. Para cada una, escribe qué la marca y dónde queda registrada.
3. Haz el inventario de redes. Una fila por red y por uso: orgánico, anuncios, influencers. Apunta quién la lleva, cuántas horas al mes y cuánto se gasta.
4. Escribe el presupuesto total al mes y quién decide cómo se reparte.
5. Escribe de 3 a 5 preguntas. Para cada una, la decisión que permite tomar, quién la toma y cuándo.

### Con tu asistente de IA

Pega tu inventario y tus preguntas y pide: «Para cada pregunta, dime qué decisión permite tomar y qué datos harían falta para responderla. Si una pregunta no lleva a ninguna decisión, dímelo». No le pidas que invente las preguntas: le faltan el contexto de tu cliente y sus prioridades.

### Cómo comprobarlo

Lee cada pregunta a quien decide el presupuesto. Si contesta «¿y qué haría yo con eso?», reescríbela.

## Ejemplo con Fandango para cafeterías

*Ejemplo 0.1. Ficha del negocio*

| Campo | Fandango para cafeterías |
| --- | --- |
| Qué vende | Café para cafeterías, con un pedido cada mes |
| Cómo se cobra | Pedido mensual sin contrato: la cafetería pide cuando quiere |
| Conversión en la web | `generate_lead` (formulario de `/empresas.html`, `lead_type` = `b2b`) |
| Quién cualifica | El comercial: llamada y envío de una prueba |
| Dónde viven los leads | CRM (en el caso, `leads.csv` y `cuentas_b2b.csv`) |
| Margen bruto | 35 % |

*Ejemplo 0.2. El embudo y su fuente*

| Etapa | Qué la marca | Fuente |
| --- | --- | --- |
| Lead | Envía el formulario para cafeterías | GA4 (`generate_lead`) y CRM (estado «nuevo») |
| Cualificado | El comercial ha llamado y ha enviado la prueba | CRM (estado «cualificado», `fecha_cualificado`) |
| Cliente | Hace su primer pedido | CRM (estado «cliente», `fecha_cliente`) |
| Ingreso recurrente | Cada pedido mensual | Pedidos de la cuenta (`cuentas_b2b.csv`) |

*Ejemplo 0.3. Inventario de redes del carril de cafeterías*

| Red | Uso | Quién la lleva | Coste medio al mes |
| --- | --- | --- | --- |
| Instagram | Orgánico: reels y carruseles para cafeterías | Community manager | 78 € en horas |
| LinkedIn | Anuncios (LinkedIn Ads) | Community manager | 201 € en anuncios |
| LinkedIn | Orgánico: posts de caso de cliente y de equipo | Community manager | 106 € en horas |
| Google | Búsqueda orgánica | Nadie en concreto | 0 € en redes |
| Directo | Sin campaña | | 0 € en redes |

Las horas se valoran a 20 €/h. El presupuesto de redes de toda la marca ronda los 1.500 € al mes y lo decide la fundadora. El comercial decide a quién llama cada día.

*Ejemplo 0.4. Preguntas de negocio*

| Nº | Pregunta | Decisión que permite tomar | Quién decide |
| --- | --- | --- | --- |
| 1 | ¿Qué red trae cafeterías que acaban pidiendo? | Dónde invertir en anuncios y en horas | Fundadora |
| 2 | ¿Cuánto nos cuesta un cliente en cada red? | Subir o bajar LinkedIn Ads | Fundadora |
| 3 | ¿Por qué se pierden los leads de Instagram? | Cambiar el formulario o el mensaje del reel | Community manager |
| 4 | ¿Qué cafeterías van a dejar de pedir? | A quién llama el comercial esta semana | Comercial |
| 5 | ¿Qué leads es más probable que cierren? | En qué orden llama el comercial | Comercial |

## Tu proyecto

*Plantilla 0.1. Ficha del negocio*

| Campo | Tu proyecto |
| --- | --- |
| Qué vende | |
| Cómo se cobra | |
| Conversión en la web | |
| Quién cualifica | |
| Dónde viven los leads | |
| Margen bruto | |

*Plantilla 0.2. Tu embudo y su fuente*

| Etapa | Qué la marca | Fuente |
| --- | --- | --- |
| Lead | | |
| Cualificado | | |
| Cliente | | |
| Ingreso recurrente | | |

*Plantilla 0.3. Inventario de redes*

| Red | Uso | Quién la lleva | Horas al mes | Gasto al mes |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 0.4. Presupuesto y quién decide*

| Campo | Tu respuesta |
| --- | --- |
| Presupuesto total de redes al mes | |
| Valor de una hora de trabajo (€/h) | |
| Quién decide el reparto | |
| Cada cuánto se decide | |
| Quién decide a qué lead se llama primero | |

*Plantilla 0.5. Tus preguntas de negocio*

| Nº | Pregunta | Decisión que permite tomar | Quién decide |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Errores frecuentes

- Quedarse en el lead. «¿Qué red trae más leads?» premia a la red que trae contactos baratos, aunque no compren.
- Olvidar las horas. Una red sin anuncios no es gratis: cuesta las horas de quien la lleva.
- Preguntas sin dueño. Si nadie decide con la respuesta, nadie la va a mirar.
- Mezclar carriles. Si tu negocio también vende en la web, separa los dos embudos.

## Antes de seguir

- [ ] El embudo tiene las cuatro etapas y cada una dice su fuente.
- [ ] Cada red tiene su coste al mes, con las horas valoradas en euros.
- [ ] Sabes quién decide el presupuesto y quién decide el orden de llamada.
- [ ] Cada pregunta tiene su decisión y su dueño.
- [ ] Al menos una pregunta mira más allá del lead: cliente o ingreso.
