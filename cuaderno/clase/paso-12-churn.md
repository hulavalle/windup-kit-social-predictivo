# Paso 12. Churn y señales

**En la práctica del bucle 2 · tu proyecto.** Define el churn de tu negocio y cinco señales que lo anticipan.

Con contrato (suscripción), el churn es la baja. Sin contrato (compra suelta, cafetería que pide cuando quiere), se fija un umbral de inactividad según el tiempo habitual entre pedidos. En captación de leads, el mismo tipo de modelo puntúa qué lead va a cerrar. Una señal solo vale si se conoce antes de predecir: la fecha de baja no es una señal.

*Ejemplo 12.1. Señales de Café Fandango*

| Señal | Se van con la señal | Se van sin la señal |
| ------ | ------ | ------ |
| Dos entregas saltadas en dos meses | 70,6 % | 9,2 % |
| Una incidencia de soporte en dos meses | 62,3 % | 8,6 % |
| Entró con el 50 % de descuento | 37,2 % | 7,1 % |
| Cafetería con pedidos cada vez más pequeños | 40 % | 0 % |

El modelo de churn ordena a los suscriptores por riesgo: del 10 % con más riesgo se fue el 41,8 %, frente al 8,3 % de media.

*Plantilla 12.1. Tu definición*

| Campo | Tu proyecto |
| ------ | ------ |
| Qué cuenta como churn (o como lead que cierra) | |
| Umbral de inactividad, si no hay contrato | |
| Cada cuánto lo calcularías | |

*Plantilla 12.2. Tus cinco señales*

| Señal | De dónde sale | ¿Se conoce antes de predecir? |
| ------ | ------ | -- |
| | | |
| | | |
| | | |
| | | |
| | | |

Versión completa: el paso 12 de tu plantilla añade cómo validar el modelo con meses guardados y el lift por deciles.
