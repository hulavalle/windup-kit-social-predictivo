# Paso 12. Churn y señales

**Qué te llevas.** La definición de churn de tus cuentas con su umbral de inactividad, las señales que lo anticipan, la puntuación de leads (qué lead va a cerrar) con sus señales, y cómo validar los dos con meses guardados y lift por deciles.

## Para qué sirve

Con contrato, el churn es la baja. Sin contrato, nadie se da de baja: un día dejan de pedir. Para saber cuándo un cliente se ha ido hay que fijar un umbral de inactividad según el tiempo habitual entre pedidos. Si piden cada mes, dos meses completos sin pedido es una señal clara.

Predecir el churn no es adivinar quién se va. Es ordenar a quién mirar primero. El modelo da a cada cliente una probabilidad, y lo útil es que el grupo con más riesgo se vaya mucho más que la media. Eso se mide con el lift por deciles: se ordena por riesgo, se divide en diez grupos y se compara el grupo de arriba con la media.

En captación de leads, el mismo tipo de modelo sirve para otra pregunta: qué lead va a cerrar. Es la puntuación de leads. Usa lo que se sabe cuando llega el lead (red, contenido, tamaño del negocio, lo que contestó en el formulario) y da una probabilidad de cierre. Con ella, el comercial llama primero a quien más probabilidades tiene.

Una señal solo vale si se conoce antes de predecir. La fecha en que se perdió un lead, su motivo de pérdida o su estado actual son información del futuro. Si entran en el modelo, acierta casi siempre en la prueba y falla en la vida real. Es la fuga de datos.

La exactitud engaña. En la tienda de Café Fandango, un modelo que dice «nadie se va» acierta el 91,7 %, porque casi nadie se va cada mes. Por eso se mira el lift.

GA4 tiene su propia probabilidad de abandono, pero pide al menos 1.000 usuarios que cumplen la condición y 1.000 que no en un periodo reciente. Un negocio B2B pequeño no llega: por eso se trabaja con el histórico del CRM.

## Cómo se hace

### Churn de cuentas

1. Mide el tiempo habitual entre pedidos de tus clientes.
2. Fija el umbral: cuántos meses sin pedido cuentan como churn.
3. Calcula el churn mensual: cuentas que cruzan el umbral / cuentas activas al empezar el mes.
4. Haz la lista de señales candidatas. Las tendencias pesan más que los totales: un pedido más pequeño que los anteriores avisa antes que el total del año.
5. Para cada señal, calcula qué porcentaje de cuentas con y sin la señal deja de pedir.
6. Si tienes pocos casos de churn, quédate con una regla: la señal más clara y una revisión semanal.

### Puntuación de leads

1. Toma los leads ya resueltos: cliente o perdido.
2. Lista las señales que se conocen al llegar el lead: red, contenido, número de locales, respuestas del formulario.
3. Calcula la tasa de cierre con y sin cada señal.
4. Combínalas: con pocas señales, una tabla de puntos; con más datos, una regresión logística.
5. Valida con meses guardados: entrena con los leads más antiguos y prueba con los más recientes, nunca al azar.
6. Mide el lift: tasa de cierre del 10 % con más puntuación frente a la media.

### Con tu asistente de IA

Usa el prompt de `prompts/s2-b2-churn.md`. Para la puntuación de leads, adapta el bloque de reglas: «Usa solo columnas que se conocen el día del lead: `red`, `canal_captacion`, `utm_content`, `n_locales`. No uses `estado`, `fecha_cualificado`, `fecha_cliente`, `fecha_perdido`, `motivo_perdida` ni `id_cuenta`: son del futuro. Entrena con los leads más antiguos, valida con los más recientes y dame la tasa de cierre por decil frente a la media».

### Cómo comprobarlo

Si la IA dice que acierta casi el 100 %, revisa qué columnas ha usado. Comprueba a mano la tasa con y sin la señal principal con un filtro.

## Ejemplo con Fandango para cafeterías

*Ejemplo 12.1. Definición de churn de cuentas*

| Campo | Fandango para cafeterías |
| --- | --- |
| Qué cuenta como churn | Último pedido seguido de dos meses completos sin pedir |
| Cliente activo | Pedido en los últimos 60 días: 85 de 122 cafeterías captadas |
| Churn de partida | 3,3 cafeterías al mes dejan de pedir (media de marzo a agosto de 2026) |
| Cada cuánto se calcula | Cada semana para las señales; cada mes para el churn |

*Ejemplo 12.2. La señal de las cafeterías*

| Señal | Casos | Dejan de pedir en los dos meses siguientes |
| --- | --- | --- |
| Pedido por debajo del 80 % de la media de sus tres pedidos anteriores (sin contar agosto) | 30 | 40 % |
| Sin esa señal | 247 | 0 % |

Con tan pocos casos, no hace falta un modelo: la regla separa muy bien y el comercial la entiende. Ahora mismo hay 8 cafeterías activas con pedidos decrecientes.

*Ejemplo 12.3. Señales para la puntuación de leads*

| Señal | ¿Se conoce el día del lead? | Qué se sabe ya |
| --- | --- | --- |
| Red de captación | Sí | Cierra el 47 % en LinkedIn y el 4 % en Instagram |
| Contenido (`utm_content`) | Sí | Se calcula con tus datos |
| Número de locales (`n_locales`) | Sí | Se calcula con tus datos |
| Zona de reparto | Sí, si el formulario pide el código postal | 32 leads de Instagram se perdieron por estar fuera de la zona |
| Motivo de pérdida | No: se sabe al final | No puede ser señal |
| Fecha de cualificado | No: se sabe después | No puede ser señal |

*Ejemplo 12.4. Validación de la puntuación de leads*

| Campo | Fandango para cafeterías |
| --- | --- |
| Entrenamiento | Leads resueltos más antiguos |
| Validación | Los meses más recientes con leads ya resueltos |
| Fuera | Los leads de las últimas semanas: aún no se han resuelto |
| Métrica | Tasa de cierre del decil de más puntuación frente al 16,6 % de media |
| Resultado | Se calcula con tus datos |

Como referencia de lo que da un buen modelo: en la tienda, del 10 % de suscriptores con más riesgo se fue el 41,8 %, frente al 8,3 % de media.

## Tu proyecto

*Plantilla 12.1. Tu definición de churn*

| Campo | Tu proyecto |
| --- | --- |
| Qué cuenta como churn | |
| Tiempo habitual entre pedidos o pagos | |
| Umbral de inactividad | |
| Cliente activo | |
| Churn de partida | |
| Cada cuánto lo calculas | |

*Plantilla 12.2. Señales de churn*

| Señal | De dónde sale | ¿Se conoce antes de predecir? | % que se va con la señal | % que se va sin ella |
| --- | --- | -- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 12.3. Señales de la puntuación de leads*

| Señal | Campo del formulario o del CRM | ¿Se conoce el día del lead? | Tasa de cierre con la señal | Tasa sin ella |
| --- | --- | -- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 12.4. Validación*

| Campo | Churn de cuentas | Puntuación de leads |
| --- | --- | --- |
| Meses de entrenamiento | | |
| Meses guardados para validar | | |
| Periodo que queda fuera | | |
| Media del suceso | | |
| Decil de más riesgo o puntuación | | |
| Lift | | |

## Errores frecuentes

- Usar información del futuro. El estado, la fecha de pérdida o el motivo dan un acierto falso.
- Validar al azar. Mezcla meses y el modelo ve el futuro; valida siempre con los meses más recientes.
- Presumir de exactitud. Si casi nadie se va, la exactitud siempre es alta.
- Un umbral que no tiene en cuenta la temporada. Un agosto flojo no es un churn.
- Un modelo para un puñado de casos. Con pocas bajas al mes, una regla clara es más honesta.

## Antes de seguir

- [ ] El churn de cuentas tiene umbral de inactividad y cifra de partida.
- [ ] Cada señal se conoce antes de predecir.
- [ ] La puntuación de leads usa solo lo que se sabe el día del lead.
- [ ] La validación usa meses guardados, no una muestra al azar.
- [ ] Das el lift por deciles además de la exactitud.
