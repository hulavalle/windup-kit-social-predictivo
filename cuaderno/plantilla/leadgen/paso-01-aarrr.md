# Paso 1. Tu AARRR

**Qué te llevas.** Tu matriz de conversiones con la columna `etapa_aarrr`, las etapas que viven en el CRM y no en GA4, una propuesta para cada etapa que no mides y la etapa que priorizas este trimestre.

## Para qué sirve

La matriz de conversiones de la clase de GTM dice qué medir. AARRR dice en qué momento del crecimiento está cada evento: Adquisición, Activación, Retención, Recomendación e Ingresos. Cuando colocas cada fila en su etapa, ves dónde tienes medición y dónde no.

En captación de leads, GA4 ve bien la parte alta: de dónde llega la visita, qué páginas lee y si envía el formulario. La parte baja, la que paga, vive en el CRM: si el lead se cualifica, si compra y si sigue comprando. Si tu AARRR solo tiene eventos de GA4, la Retención y los Ingresos a lo largo del tiempo quedarán vacíos.

## Cómo se hace

1. Abre tu matriz de conversiones: es [plan/matriz.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/matriz.csv) de tu copia del kit de la clase 1, no de este kit. Añade la columna `etapa_aarrr`.
2. Pon cada fila en una etapa. Usa esta regla: si el evento demuestra interés, Activación; si es el lead o el pago, Ingresos; si se repite en el tiempo, Retención.
3. La Adquisición no suele tener fila: la mide GA4 con la sesión y sus UTMs.
4. Añade las etapas del CRM como filas aparte, con su fuente: cualificado, cliente, pedido recurrente.
5. Busca las etapas vacías. Para cada una, propón cómo medirla.
6. Elige la etapa que priorizas este trimestre: la que más duele y donde puedes actuar.

### Con tu asistente de IA

Adjunta tu matriz en CSV y pide: «Asigna a cada fila una etapa AARRR y explica en una frase por qué. Después dime qué etapas quedan sin ningún evento». Revisa cada asignación: la IA tiende a poner el lead en Adquisición, y en tu negocio es Ingresos, porque es la puerta del dinero.

### Cómo comprobarlo

Cada etapa tiene al menos un evento o una propuesta. Cada fila del CRM dice de qué campo sale.

## Ejemplo con Fandango para cafeterías

*Ejemplo 1.1. El AARRR del carril de cafeterías*

| Etapa | Pregunta | Evento o dato | Métrica | Fuente |
| --- | --- | --- | --- | --- |
| Adquisición | ¿De dónde llegan? | Sesión con UTM de Instagram o LinkedIn | Sesiones por fuente/medio | GA4 |
| Activación | ¿Tienen una primera experiencia de valor? | Visita a «Cafeterías» | Sesiones que llegan a `/empresas.html` | GA4 |
| Retención | ¿Vuelven? | Pedido mensual de la cuenta | Cuentas que piden en el mes 6 | CRM |
| Recomendación | ¿Traen a otros? | ¿Qué evento la mide? | Cafeterías que llegan recomendadas por otra | |
| Ingresos | ¿Pagan, y cuánto con el tiempo? | Cualificado, cliente, pedidos | Cualificados, clientes e ingreso mensual | CRM |

Las filas de la matriz de Café Fandango (`datos/matriz_conversiones.csv`) las colocas tú en la práctica del bucle 1. Al terminar, mira qué etapa se queda sin ninguna fila.

*Ejemplo 1.2. Etapas que viven en el CRM*

| Etapa del embudo | Etapa AARRR | Campo | Archivo del caso |
| --- | --- | --- | --- |
| Lead cualificado | Ingresos | `estado` = cualificado, `fecha_cualificado` | `leads.csv` |
| Cliente | Ingresos | `estado` = cliente, `fecha_cliente` | `leads.csv` |
| Pedido de cada mes | Retención | `mes`, `importe` | `cuentas_b2b.csv` |
| Motivo de pérdida | Ingresos | `motivo_perdida` | `leads.csv` |

*Ejemplo 1.3. La etapa que se prioriza*

| Campo | Fandango para cafeterías |
| --- | --- |
| Etapa | Ingresos: el paso de lead a cliente |
| Por qué | De los leads de Instagram, 113 se perdieron porque no eran una cafetería y 88 porque solo querían precios |
| Qué se quiere mover | La tasa de cualificación de Instagram, hoy del 31 % (en LinkedIn, del 72 %) |
| Propuesta para la etapa sin medir | Sale de la práctica del bucle 1 (plantilla 1.3) |

## Tu proyecto

*Plantilla 1.1. Tu matriz con su etapa AARRR*

| Nº | Acción de negocio | Evento | Etapa AARRR | Fuente |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |

*Plantilla 1.2. Tus etapas del CRM*

| Etapa del embudo | Etapa AARRR | Campo del CRM | ¿Lleva fecha? |
| --- | --- | --- | --- |
| Lead cualificado | | | |
| Cliente | | | |
| Pago o pedido recurrente | | | |
| Motivo de pérdida | | | |

*Plantilla 1.3. Etapas sin medir*

| Etapa | Por qué no se mide | Propuesta | Quién la implanta |
| --- | --- | --- | --- |
| | | | |
| | | | |

*Plantilla 1.4. La etapa que priorizas*

| Campo | Tu proyecto |
| --- | --- |
| Etapa | |
| Por qué (con una cifra) | |
| Qué métrica quieres mover | |
| Hasta cuándo | |

## Errores frecuentes

- Poner el lead en Adquisición. La Adquisición es la visita; el lead ya es la primera puerta del ingreso.
- Dejar la Retención vacía porque GA4 no la ve. En tu negocio, la Retención está en el CRM o en la facturación.
- Un CRM sin fechas. Sin la fecha de cada cambio de estado no podrás hacer cohortes ni medir el tiempo hasta el cierre.
- Motivos de pérdida en texto libre. Usa una lista cerrada: así se pueden contar.

## Antes de seguir

- [ ] La matriz tiene la columna `etapa_aarrr` en todas las filas.
- [ ] Las etapas del CRM tienen su campo y su fecha.
- [ ] Cada etapa sin medir tiene una propuesta y un responsable.
- [ ] La etapa que priorizas tiene una cifra que justifica la prioridad.
- [ ] Los motivos de pérdida del CRM son una lista cerrada.
