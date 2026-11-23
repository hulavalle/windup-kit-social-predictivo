# Paso 10. Escalera de preguntas

**Qué te llevas.** Una pregunta por peldaño con la decisión que permite tomar, los datos que necesita cada una, el histórico mínimo y el inventario de datos de tu tienda.

## Por qué importa

La segunda frase de la fundadora fue: «Me entero de que se van cuando ya se han ido». Café Fandango tiene 647 suscriptores activos. En los últimos seis meses se ha dado de baja un 8,6 % al mes, unos 44 suscriptores. Ella lo ve en el informe del mes siguiente, cuando ya no puede hacer nada.

Las preguntas de datos suben por una escalera de cuatro peldaños:

- **Descriptivo**: qué pasó. ¿Cuántos se dieron de baja en octubre?
- **Diagnóstico**: por qué pasó. ¿Por qué se van más los que llegan de TikTok?
- **Predictivo**: qué pasará. ¿Quién es probable que se vaya en noviembre?
- **Prescriptivo**: qué hacer. ¿Qué acción reduce las bajas de los clientes de más valor, y cómo se demuestra?

La sesión 1 se quedó en los dos primeros. Subir de peldaño pide más datos y más histórico. Para predecir hace falta un año de histórico fiable, como mínimo, y para prescribir hace falta un experimento con grupo de control.

Las métricas predictivas de GA4, como la probabilidad de abandono, tienen un requisito alto: en un periodo de 7 días dentro de los últimos 28, al menos 1.000 usuarios que cumplen la condición (abandonan o compran) y 1.000 que no. Una tienda pequeña no llega. Por eso la sesión 2 trabaja con el histórico de la tienda y la IA.

## Ejemplo con Café Fandango

*Ejemplo 10.1. La escalera de la tienda*

| Peldaño | Pregunta | Decisión | Datos que necesita | Histórico mínimo |
| ------ | ------ | ------ | ------ | ------ |
| Descriptivo | ¿Cuántos suscriptores se dieron de baja en octubre? | Ninguna: solo informa | Estado de cada suscripción al cierre del mes | El mes |
| Diagnóstico | ¿Por qué se van más los que llegan de TikTok? | Revisar la oferta de entrada | Canal de captación, descuento de entrada y mes de alta de cada suscripción | Cohortes con 3 a 6 meses cumplidos |
| Predictivo | ¿Quién es probable que se vaya en noviembre? | A quién contactar esta semana | Una fila por suscripción y mes, con entregas saltadas e incidencias | Un año, más meses guardados para validar |
| Prescriptivo | ¿Qué acción reduce las bajas de los clientes de más valor? | Qué hacer y cómo probarlo | Lo anterior, más el valor de cada cliente y un grupo de control | Lo anterior, más la duración del experimento |

*Ejemplo 10.2. El inventario de datos de la tienda*

| Fuente | Qué guarda | Desde cuándo | Identificador del cliente | Cómo se exporta |
| ------ | ------ | ------ | ------ | ------ |
| Clientes | Fecha de la primera compra, UTMs, red, descuento de entrada | Junio de 2025 | `id_cliente` seudónimo | `clientes.csv` |
| Pedidos | Compras sueltas y cobros de la suscripción, con incidencias de soporte | Junio de 2025 | `id_cliente` | `pedidos.csv` |
| Suscripciones | Una fila por suscripción y mes: entrega, entrega saltada, incidencias, importe, si sigue activa | Junio de 2025 | `id_cliente` | `suscripciones.csv` |
| GA4 | Sesiones, compras y altas por fuente y mes | Junio de 2025 | Ninguno: datos agregados | `ga4_adquisicion.csv` |
| Ventas semanales | Kilos que salen del tostadero | Junio de 2025 | Ninguno | `ventas_semanales.csv` |

Café Fandango tiene datos de junio de 2025 a noviembre de 2026, con noviembre en curso. Llega justo para un modelo de churn: entrena con quince meses y valida con dos.

## Tu proyecto

1. Escribe una pregunta por peldaño (plantilla 10.1), todas sobre el mismo problema. Si vendes suscripción, el problema suele ser la baja. Si vendes en compra suelta, que el cliente no vuelva.
2. Escribe la decisión de cada pregunta. La del peldaño descriptivo puede ser «ninguna»: está bien, pero entonces no te quedes ahí.
3. Para cada pregunta, escribe los datos que necesita y el histórico mínimo.
4. Haz el inventario de tus fuentes (plantilla 10.2). En una tienda WooCommerce:
   - **Pedidos**: **WooCommerce** > **Pedidos**, o el informe de pedidos de **Análisis**, con la descarga a CSV.
   - **Clientes**: **WooCommerce** > **Clientes**. Incluye la fecha de la primera compra y el número de pedidos.
   - **Origen del pedido**: la atribución de pedidos, si está activada. Si se activó hace poco, los pedidos anteriores no la tienen: apúntalo.
   - **Suscripciones**: con WooCommerce Subscriptions, cada suscripción tiene su estado y sus pedidos de renovación.
   - **Soporte y email**: la herramienta de tickets y la de email, si guardan el mismo identificador de cliente.
5. Marca qué fuentes comparten identificador de cliente. Sin un identificador común, no puedes juntar la red de captación con la baja.
6. Compara lo que tienes con lo que pide cada peldaño. Si te falta histórico, escribe desde qué fecha empiezas a guardarlo y cuándo podrás subir de peldaño.

### Con tu asistente de IA

```text
Te adjunto el diccionario de columnas de las exportaciones de mi tienda (sin datos).
Mi pregunta predictiva es: [pregunta]. La decisión es: [decisión].
Dime qué columnas necesitaría para responderla, cuáles me faltan,
qué fuentes tengo que juntar y con qué identificador, y cuántos meses de histórico
harían falta para entrenar y además guardar meses para validar.
Si con estos datos no se puede responder, dilo.
```

### Cómo comprobarlo

- Toma un cliente seudónimo cualquiera y búscalo en todas tus fuentes. Si aparece en todas con el mismo identificador, puedes cruzarlas.
- Cuenta los meses completos que tienes. Si son menos de doce, el peldaño predictivo espera.

*Plantilla 10.1. Tu escalera*

| Peldaño | Pregunta | Decisión | Datos que necesita | Histórico mínimo | ¿Lo tienes? |
| ------ | ------ | ------ | ------ | ------ | -- |
| Descriptivo | | | | | |
| Diagnóstico | | | | | |
| Predictivo | | | | | |
| Prescriptivo | | | | | |

*Plantilla 10.2. Tu inventario de datos*

| Fuente | Qué guarda | Desde cuándo | Identificador del cliente | Cómo se exporta |
| ------ | ------ | ------ | ------ | ------ |
| Pedidos | | | | |
| Clientes | | | | |
| Origen del pedido | | | | |
| Suscripciones | | | | |
| Soporte | | | | |
| Email o CRM | | | | |
| GA4 | | | | |

## Errores frecuentes

- Quedarse en el peldaño descriptivo con un informe más bonito.
- Saltar al predictivo sin datos: un modelo con tres meses de histórico no aprende nada útil.
- Contar con las métricas predictivas de GA4 sin comprobar si la propiedad llega a los 1.000 usuarios.
- Fuentes que no comparten identificador. Se descubre tarde, cuando ya se ha exportado todo.

## Antes de seguir

- [ ] Tienes una pregunta por peldaño, todas sobre el mismo problema.
- [ ] Cada pregunta tiene su decisión y los datos que necesita.
- [ ] Tu inventario dice desde cuándo guardas cada dato.
- [ ] Sabes qué fuentes comparten identificador de cliente.
- [ ] Sabes si tienes histórico para el peldaño predictivo, y si no, desde cuándo lo tendrás.
