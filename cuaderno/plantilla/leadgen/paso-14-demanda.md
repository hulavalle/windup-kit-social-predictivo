# Paso 14. Demanda

**Qué te llevas.** La previsión que necesita tu negocio (leads, pedidos o citas) con su rango, la decisión que alimenta, la serie mínima que hace falta, cómo validarla con semanas guardadas y la rutina para revisarla cada mes.

## Para qué sirve

Una previsión sirve para decidir antes de que pase: cuántas horas de comercial reservar, cuánto producto comprar, cuánto presupuesto poner en anuncios. Si no alimenta una decisión, no hace falta.

En captación de leads hay dos previsiones típicas. La de leads dice cuánta carga tendrá el equipo comercial y si hace falta más presupuesto para llegar al objetivo. La de pedidos o ingresos de los clientes dice cuánto hay que producir o comprar.

Una serie tiene tendencia (sube o baja con el tiempo), temporada (se repite cada año: agosto, Navidad) y ruido (lo que no se explica). Una previsión sin rango es una opinión: da siempre el intervalo en el que esperas estar.

Se valida contra semanas que guardaste sin enseñárselas al modelo. Si la previsión de esas semanas acierta y la realidad cae dentro del rango casi siempre, puedes fiarte de la siguiente.

## Cómo se hace

1. Elige qué prever y para qué decisión.
2. Elige el horizonte: tantas semanas como tarde en tener efecto la decisión.
3. Comprueba que tienes la serie mínima. Para un método que compara con la misma semana del año anterior, necesitas un año completo, más las semanas recientes con las que mides el crecimiento, más las que guardas para validar.
4. Empieza por un método sencillo: la misma semana del año anterior × el crecimiento de las últimas semanas frente a las mismas del año anterior.
5. Guarda las últimas 13 semanas, prevé esas semanas y mide el error medio.
6. Calcula el rango con el error de esas semanas y comprueba qué porcentaje de semanas reales cae dentro.
7. Prevé el horizonte completo con su rango.
8. Cada mes, compara lo real con lo previsto y apunta el error.

### Con tu asistente de IA

Usa el prompt de `prompts/s2-b4-demanda.md` con tu serie semanal. Pide un método sencillo primero, la validación con las 13 últimas semanas guardadas, el error medio y el rango. Si te propone un modelo complejo, pide que lo compare con el sencillo en las mismas semanas guardadas. Si no mejora, quédate con el sencillo.

### Cómo comprobarlo

Toma una semana guardada y calcula a mano la previsión: la misma semana del año anterior × el crecimiento. Compárala con lo que dice la IA y con lo real.

## Ejemplo con Fandango para cafeterías

*Ejemplo 14.1. La previsión*

| Campo | Fandango para cafeterías |
| --- | --- |
| Qué prevemos | Kilos por semana de las cafeterías, separados de la tienda |
| Para qué decisión | Cuánto café verde comprar y cuánto tostar |
| Horizonte | 8 semanas |
| Método | Misma semana del año anterior × crecimiento de las últimas 8 semanas |
| Crecimiento interanual usado | × 1,35 en cafeterías |
| Validación | 13 semanas guardadas, de agosto a noviembre de 2026: error medio del 6 % y el 85 % de las semanas reales dentro del rango (tienda y cafeterías juntas) |
| Serie disponible | 76 semanas en `ventas_semanales.csv` |

*Ejemplo 14.2. Kilos previstos de las cafeterías*

| Semana | Cafeterías | Total con la tienda | Rango del total |
| --- | --- | --- | --- |
| 2026-11-30 | 438 | 583 | 514–652 |
| 2026-12-07 | 446 | 594 | 523–664 |
| 2026-12-14 | 445 | 603 | 531–674 |
| 2026-12-21 | 337 | 466 | 410–521 |
| 2026-12-28 | 266 | 348 | 306–389 |

Las cafeterías bajan las dos últimas semanas del año. Para todo diciembre, la marca prevé 2.010 kg, entre 1.771 y 2.249 kg.

*Ejemplo 14.3. La previsión de leads*

| Campo | Fandango para cafeterías |
| --- | --- |
| Qué prevemos | Leads por semana y por red |
| Para qué decisión | Cuántas llamadas tendrá el comercial y si hay que subir LinkedIn Ads |
| Datos | `fecha_lead` y `red` de `leads.csv` |
| Resultado | Se calcula con tus datos |

## Tu proyecto

*Plantilla 14.1. Tu previsión*

| Campo | Tu proyecto |
| --- | --- |
| Qué prevés (leads, pedidos, citas, ingresos) | |
| Para qué decisión | |
| Horizonte | |
| Método | |
| Datos que usas | |
| Serie disponible | |

*Plantilla 14.2. Serie mínima*

| Pieza | Semanas o meses | ¿Las tienes? |
| --- | --- | -- |
| Un año completo para la temporada | | |
| Semanas recientes para el crecimiento | | |
| Semanas guardadas para validar | | |
| Total | | |

*Plantilla 14.3. Validación*

| Campo | Tu proyecto |
| --- | --- |
| Semanas guardadas | |
| Error medio | |
| Rango | |
| % de semanas reales dentro del rango | |

*Plantilla 14.4. Revisión mensual*

| Mes | Previsto | Real | Error | ¿Dentro del rango? | Qué cambias |
| --- | --- | --- | --- | -- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

## Errores frecuentes

- Una cifra sin rango. Nadie sabe si fallar por un 10 % es mucho o poco.
- Validar con las mismas semanas con las que se calculó el crecimiento.
- Mezclar carriles con temporadas distintas. Las cafeterías bajan en agosto; la tienda, no igual.
- Cambiar de método cada mes. Cambia solo si el nuevo mejora en las semanas guardadas.
- Prever leads sin pensar en el presupuesto. Si subes anuncios, la previsión de leads cambia: apúntalo.

## Antes de seguir

- [ ] La previsión alimenta una decisión con nombre.
- [ ] Tienes la serie mínima o sabes cuándo la tendrás.
- [ ] La validación usa semanas guardadas.
- [ ] Toda cifra prevista lleva su rango.
- [ ] La revisión mensual tiene responsable y fecha.
