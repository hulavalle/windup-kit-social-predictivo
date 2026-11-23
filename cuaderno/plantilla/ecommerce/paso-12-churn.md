# Paso 12. Churn y señales

**Qué te llevas.** La definición de churn de tu tienda, las señales que lo anticipan, las ventanas del modelo, su validación con meses guardados y el lift por deciles que dice si el modelo sirve.

## Por qué importa

¿A quién llamamos esta semana? Predecir no es adivinar quién se va: es ordenar a quién mirar primero.

**Qué es churn** depende de tu modelo de venta:

- **Con contrato**, como una suscripción, el churn es la baja. Churn mensual = bajas del mes / suscriptores activos al empezar el mes.
- **Sin contrato**, como la compra suelta, no hay baja. Se fija un umbral de inactividad: un cliente se da por perdido si pasa más días sin comprar de los que suele pasar entre dos compras. El umbral sale de tus datos, no de una regla general.

Hay tres tipos: churn de clientes (dejan de comprar), de ingresos (compran menos o bajan de plan) y de marketing (dejan de abrir tus emails). Empieza por el de clientes.

Un modelo de churn aprende de señales del pasado. Una **señal** solo vale si se conoce antes del momento que predices. La fecha de baja no es una señal: es la respuesta. Si el modelo la ve, acierta el 100 % y no sirve para nada. Se llama fuga de datos. Las tendencias pesan más que los totales: una cliente que salta dos entregas seguidas dice más que el total de entregas de su vida.

Y hay que **validarlo bien**. No se parten los datos al azar: se entrena con los meses antiguos y se valida con meses recientes que el modelo no ha visto, como pasará en la realidad. La medida que se entiende es el **lift por deciles**: ordenas a los clientes por riesgo, los partes en diez grupos y miras cuántas bajas hay en el grupo de más riesgo frente a la media. La exactitud engaña: si casi nadie se va, decir «nadie se va» ya acierta mucho.

GA4 tiene una métrica de probabilidad de abandono, pero exige al menos 1.000 usuarios que abandonan y 1.000 que no en una semana dentro de los últimos 28 días. Si no llegas, el modelo se hace con el histórico de la tienda.

## Ejemplo con Café Fandango

*Ejemplo 12.1. La definición de la tienda*

| Campo | Café Fandango |
| ------ | ------ |
| Qué cuenta como churn | Baja de la suscripción en el mes |
| Unidad | Una fila por suscripción y mes en riesgo |
| Churn mensual | 8,6 % de media en los últimos seis meses (44 bajas al mes) |
| Cada cuánto se calcula | Al empezar cada mes, para el mes que empieza |

*Ejemplo 12.2. Señales de la suscripción*

| Señal | De dónde sale | Ventana | Se van con la señal | Se van sin la señal |
| ------ | ------ | ------ | ------ | ------ |
| Dos entregas saltadas | Suscripciones | Dos meses anteriores | 70,6 % | 9,2 % (ninguna saltada) |
| Una entrega saltada | Suscripciones | Dos meses anteriores | 27,3 % | 9,2 % |
| Una incidencia de soporte | Pedidos e incidencias | Dos meses anteriores | 62,3 % | 8,6 % |
| Entró con el 50 % de descuento | Clientes | Desde el alta | 37,2 % | 7,1 % (sin descuento) |
| Red de captación TikTok | Clientes (UTM) | Desde el alta | Más riesgo en el modelo | |

*Ejemplo 12.3. Ventanas y partición del modelo*

| Campo | Café Fandango |
| ------ | ------ |
| Modelo | Regresión logística, una fila por suscripción y mes en riesgo |
| Ventana de observación | Los dos meses anteriores al mes que se predice |
| Ventana de predicción | El mes siguiente |
| Meses de entrenamiento | Junio de 2025 a agosto de 2026 (4.224 filas) |
| Meses guardados para validar | Septiembre y octubre de 2026 (1.097 filas) |
| Meses que no entran | Noviembre de 2026: va en curso y sus bajas están incompletas |

*Ejemplo 12.4. Lift por deciles en los meses guardados*

| Decil de riesgo | Filas | Churn real |
| ------ | ------ | ------ |
| 1 (más riesgo) | 110 | 41,8 % |
| 2 | 110 | 12,7 % |
| 3 | 109 | 10,1 % |
| 4 | 110 | 9,1 % |
| 5 | 110 | 4,5 % |
| 6 | 109 | 0,0 % |
| 7 | 110 | 0,9 % |
| 8 | 109 | 0,9 % |
| 9 | 110 | 1,8 % |
| 10 (menos riesgo) | 110 | 0,9 % |

Del 10 % con más riesgo se fue el 41,8 %, frente al 8,3 % de media: un lift de 5,0. El AUC en validación es 0,85. La exactitud es del 92,6 %, pero un «modelo» que dice que nadie se va acierta el 91,7 %. Por eso no se mira la exactitud.

Cuando la IA usó `fecha_baja` como señal, el mismo modelo dio un 100 % de exactitud. Acertaba porque miraba el futuro.

## Tu proyecto

1. Escribe tu definición de churn (plantilla 12.1).
2. Si no tienes contrato, calcula el umbral de inactividad. Toma los clientes con dos compras o más, calcula los días entre una compra y la siguiente, y mira el valor por debajo del cual caen la mayoría de esos intervalos (por ejemplo, ocho de cada diez). Ese es tu umbral: quien pasa más días sin comprar, se da por perdido.
3. Lista las señales candidatas (plantilla 12.2). En una tienda WooCommerce suelen estar en:
   - **Suscripciones**: entregas saltadas, pausas (estado en espera), cambios de plan, pagos fallidos.
   - **Pedidos**: días desde la última compra, frecuencia, ticket que baja, descuentos usados.
   - **Soporte**: incidencias por retraso o producto dañado.
   - **Email**: días sin abrir.
   - **Captación**: red, campaña, descuento de entrada.
4. Pasa cada señal por la prueba de la fuga (plantilla 12.5): ¿se conoce el día en que predices? Si no, fuera.
5. Fija las ventanas y la partición (plantilla 12.3). Deja fuera el mes en curso.
6. Pide el modelo a tu asistente de IA con el prompt de abajo.
7. Rellena el lift por deciles (plantilla 12.4). Si el decil de más riesgo no tiene claramente más bajas que la media, el modelo no ordena: no lo uses.
8. Repite la validación cada trimestre con los meses nuevos.

### Con tu asistente de IA

Adapta `prompts/s2-b2-churn.md`:

```text
Te adjunto [archivo con una fila por cliente o suscripción y mes] y su diccionario.
No hay datos personales. Churn significa: [tu definición].
Quiero un modelo sencillo (regresión logística) que dé, para cada fila, la probabilidad
de churn en el mes siguiente.
Reglas obligatorias:
- Usa solo señales conocidas ANTES del mes que se predice: [lista de señales].
- No uses fecha de baja, estado final ni nada calculado con ellos.
- Entrena con [meses] y valida con [meses guardados]. El mes en curso queda fuera.
Calcula con código y devuelve:
1. Las señales usadas y si suben o bajan el riesgo.
2. En validación, el churn real por decil de riesgo frente a la media, y el lift del decil 1.
3. El AUC y la exactitud de un modelo que dijera que nadie se va.
Si alguna señal parece demasiado buena, avísame.
```

### Cómo comprobarlo

- Si la exactitud pasa del 99 % o el AUC llega a 1, busca la fuga: pide la lista de columnas usadas.
- Comprueba a mano una tasa de señal: filtra las filas con dos entregas saltadas y cuenta cuántas tienen baja en el mes.
- Comprueba que la validación usa meses posteriores al entrenamiento.

*Plantilla 12.1. Tu definición*

| Campo | Tu proyecto |
| ------ | ------ |
| Qué cuenta como churn | |
| Umbral de inactividad, si no hay contrato | |
| Unidad (cliente y mes, suscripción y mes) | |
| Churn mensual actual | |
| Cada cuánto se calcula | |

*Plantilla 12.2. Tus señales*

| Señal | De dónde sale | Ventana | Se van con la señal | Se van sin la señal |
| ------ | ------ | ------ | ------ | ------ |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 12.3. Tus ventanas y tu partición*

| Campo | Tu proyecto |
| ------ | ------ |
| Modelo | |
| Ventana de observación | |
| Ventana de predicción | |
| Meses de entrenamiento | |
| Meses guardados para validar | |
| Meses que no entran | |

*Plantilla 12.4. Tu lift por deciles*

| Decil de riesgo | Filas | Churn real | Lift (churn del decil / churn medio) |
| ------ | ------ | ------ | ------ |
| 1 (más riesgo) | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 (menos riesgo) | | | |

*Plantilla 12.5. Tu prueba de la fuga*

| Columna | ¿Se conoce el día en que predices? | ¿Entra en el modelo? |
| ------ | -- | -- |
| | | |
| | | |
| | | |
| | | |

## Errores frecuentes

- Usar la fecha de baja o el estado final como señal.
- Partir los datos al azar en lugar de por fechas.
- Presumir de exactitud cuando casi nadie se va.
- Decidir por persona: del decil de más riesgo se van cuatro de cada diez, no todos.
- Contar el mes en curso como cerrado: parece que nadie se ha ido.
- Un umbral de inactividad copiado de otro negocio. El café se acaba en semanas; un sofá, en años.

## Antes de seguir

- [ ] Tu definición de churn está escrita y sirve para tu modelo de venta.
- [ ] Cada señal pasó la prueba de la fuga.
- [ ] El modelo se validó con meses guardados, no al azar.
- [ ] Tienes el lift por deciles y el decil de más riesgo destaca sobre la media.
- [ ] La validación se repite cada trimestre.
