# Paso 5. Valor de cada objetivo

**Qué te llevas.** El valor en euros de cada etapa de tu embudo (lead, cualificado y cliente), el valor de los objetivos que no son ventas, de dónde sale cada dato y una tabla de versiones para actualizarlo cada trimestre.

## Para qué sirve

Si un objetivo no tiene valor en euros, no puede entrar en el ROI. Y en captación de leads hay que darle valor a algo que todavía no ha pagado: un contacto que quizá compre dentro de un mes.

El valor de un lead se calcula con datos, no se inventa: la probabilidad de que acabe siendo cliente multiplicada por lo que deja un cliente. Cuanto más abajo está la etapa, más cerca del dinero y más alto el valor. Un lead cualificado vale más que un lead, porque ya ha pasado un filtro.

Hay dos formas de medir lo que deja un cliente. Por primera conversión, el margen del primer pedido. Con el tiempo, el margen de todos los pedidos que hará mientras siga. En un negocio con pedido recurrente la segunda es la buena, y la diferencia es enorme. En la sesión 2 la afinas con el LTV (paso 13).

Este valor no se queda en el informe. Lo usarás para el ROI (paso 7) y como valor de conversión en las pujas de Google Ads o Meta (paso 13).

## Cómo se hace

1. Calcula la tasa de cierre con los leads ya resueltos: los que llegaron hace tiempo suficiente para haber cerrado o haberse perdido. Si incluyes los de las últimas semanas, la tasa sale más baja de lo que es.
2. Calcula la tasa de cualificado a cliente: clientes / cualificados resueltos.
3. Calcula lo que deja un cliente: primer pedido × margen, o pedido mensual × meses del primer año × margen.
4. Valor del cliente = lo que deja un cliente.
5. Valor del cualificado = tasa de cualificado a cliente × valor del cliente.
6. Valor del lead = tasa de cierre × valor del cliente.
7. Si las redes tienen tasas muy distintas, calcula el valor del lead por red.
8. Para la notoriedad: impresiones orgánicas / 1.000 × CPM de los anuncios en esa red.
9. Apunta la versión: fecha, datos usados y valor. Repite cada trimestre.

### Con tu asistente de IA

Usa el prompt de `prompts/s1-b3-valor-objetivos.md` con tu export del CRM. Pide que calcule cada tasa con código, que diga qué leads ha dejado fuera por no estar resueltos y que dé el valor por etapa y por red. Comprueba a mano la tasa de cierre con un filtro: cuenta clientes y leads resueltos.

### Cómo comprobarlo

El valor del lead tiene que ser menor que el del cualificado, y este menor que el del cliente. Si no, hay un error en las tasas.

## Ejemplo con Fandango para cafeterías

*Ejemplo 5.1. Datos de partida*

| Dato | Valor | De dónde sale |
| --- | --- | --- |
| Tasa de cierre | 16,6 % | `leads.csv`, leads hasta agosto de 2026, ya resueltos |
| Primer pedido medio | 282 € | `cuentas_b2b.csv`, mes 0 |
| Pedido mensual medio | 379 € | `cuentas_b2b.csv`, meses 1 en adelante |
| Margen B2B | 35 % | Supuestos del negocio |

*Ejemplo 5.2. Valor del lead de cafetería*

| Objetivo | Fórmula | Datos | Valor |
| --- | --- | --- | --- |
| Lead, por primera conversión | Tasa de cierre × primer pedido × margen | 16,6 % × 282 € × 35 % | 16,37 € |
| Lead, con el primer año | Pedido mensual × 12 × tasa de cierre × margen | 379 € × 12 × 16,6 % × 35 % | 263,53 € |
| Cualificado | Tasa de cualificado a cliente × valor del cliente | Clientes / cualificados resueltos, de `leads.csv` | Fórmula: se calcula con tus datos |
| Notoriedad en Instagram | Impresiones orgánicas / 1.000 × CPM | `redes_posts.csv` y el CPM de tus anuncios | Fórmula: se calcula con tus datos |

El mismo lead vale 16 € o 264 € según se mire. Con el primer valor, cualquier red barata parece rentable. El 263,53 € sale de la tasa de cierre sin redondear.

*Ejemplo 5.3. Por qué el valor cambia por red*

| Red | Tasa de cualificación | Tasa de cierre |
| --- | --- | --- |
| Instagram | 31 % | 4 % |
| LinkedIn | 72 % | 47 % |
| Google | 60 % | 18 % |
| Directo | 65 % | 19 % |

Un lead de LinkedIn tiene una probabilidad de cerrar más de diez veces mayor que uno de Instagram. Si das el mismo valor a los dos, el ROI premia a la red que trae volumen. El valor por red es tasa de cierre de la red × valor del cliente de esa red (paso 13).

*Ejemplo 5.4. Tabla de versiones*

| Versión | Fecha | Datos usados | Valor del lead | Cambio |
| --- | --- | --- | --- | --- |
| 1 | Noviembre de 2026 | Leads de junio de 2025 a agosto de 2026 | 263,53 € (primer año) | Primera versión |

## Tu proyecto

*Plantilla 5.1. Tus datos de partida*

| Dato | Valor | De dónde sale |
| --- | --- | --- |
| Tasa de cualificación | | |
| Tasa de cualificado a cliente | | |
| Tasa de cierre | | |
| Primer pago o pedido medio | | |
| Pago mensual medio | | |
| Margen | | |

*Plantilla 5.2. Valor por etapa del embudo*

| Etapa | Fórmula | Datos | Valor |
| --- | --- | --- | --- |
| Cliente | | | |
| Cualificado | | | |
| Lead | | | |

*Plantilla 5.3. Valor del lead por red*

| Red | Tasa de cierre | Valor del cliente | Valor del lead |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |

*Plantilla 5.4. Objetivos que no son ventas*

| Objetivo | Fórmula | De dónde sale cada dato | Valor |
| --- | --- | --- | --- |
| | | | |
| | | | |

*Plantilla 5.5. Tabla de versiones*

| Versión | Fecha | Datos usados | Valor del lead | Cambio |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

## Errores frecuentes

- Calcular la tasa de cierre con leads que aún no han tenido tiempo de cerrar. Deja fuera las semanas más recientes.
- Usar el precio en lugar del margen. El valor es lo que te queda, no lo que cobras.
- Un único valor para todas las redes cuando las tasas de cierre son muy distintas.
- No volver a calcularlo. Si cambias precios, mercado o comercial, el valor cambia.

## Antes de seguir

- [ ] La tasa de cierre usa solo leads resueltos.
- [ ] Cada etapa tiene su valor, y el valor sube al bajar por el embudo.
- [ ] Cada dato dice de dónde sale.
- [ ] Si las tasas por red son distintas, tienes el valor del lead por red.
- [ ] La tabla de versiones tiene la fecha de la próxima revisión.
