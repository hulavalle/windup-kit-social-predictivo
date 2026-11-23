# Sesión 2 · Bucle 2 · Modelo de churn

**Pregunta:** ¿qué suscriptores es más probable que se den de baja?
**Adjunta:** tienda: `suscripciones.csv`; cafeterías: `cuentas_b2b.csv`. Siempre `diccionario.md`.

Los meses del modelo son meses del calendario, no la columna `meses_desde_alta`: el mes 1 es junio de 2025, el mes 15 es agosto de 2026 y los meses 16 y 17 son septiembre y octubre de 2026.

```
Eres analista de datos de Café Fandango. Te adjunto [archivo] y el diccionario.

[Tienda] Quiero un modelo sencillo (regresión logística) que estime, para cada suscripción
y mes, la probabilidad de darse de baja ese mes. Una fila por suscripción y mes con
meses_desde_alta de 1 en adelante; baja = 1 si en esa fila entrega = baja.
Reglas obligatorias:
- Usa solo señales que se conocen ANTES del mes que se predice: meses desde el alta (con tope
  en 12), primeros meses (meses_desde_alta 1 o 2), descuento de entrada del 20 % y del 50 %,
  entrega saltada el mes anterior, dos entregas saltadas en los dos meses anteriores, alguna
  incidencia en los dos meses anteriores y red de captación.
- «El mes anterior» y «los dos meses anteriores» son las filas anteriores de la misma
  suscripción (ordenada por meses_desde_alta). Si no hay fila anterior, cuenta 0.
- Red de captación: una columna 0/1 por red. Directo es la base y no lleva columna.
- Modelo: LogisticRegression de scikit-learn con los ajustes por defecto. No escales las
  variables: el umbral del punto 4 cambia si las escalas.
- No uses fecha_baja ni nada calculado a partir de ella: es información del futuro.
- Entrena con los meses de junio de 2025 a agosto de 2026 (meses del calendario 1 a 15, no
  meses_desde_alta) y valida con septiembre y octubre de 2026. Noviembre está incompleto:
  déjalo fuera de la validación.

[Cafeterías] No hay modelo: hay una regla. Una cafetería deja de pedir después de un pedido
si no hace ningún pedido en los dos meses de calendario siguientes (aquí sí cuentan los de
agosto). Señal: un pedido por debajo del 80 % de la media de sus tres pedidos anteriores.
Calcúlala así, cafetería a cafetería:
- Ordena sus pedidos por fecha_pedido y quita de la lista todos los pedidos de agosto (de 2025
  y de 2026). No se evalúan ni entran en la media.
- Sus tres pedidos anteriores son los tres anteriores de esa lista, aunque haya meses sin
  pedido entre medias.
- Evalúa cada pedido de la lista desde el cuarto hasta los de julio de 2026 (así los dos meses
  siguientes están cerrados). Si la cafetería tiene menos de 4 pedidos en la lista, no entra.
- Calcula qué % de los pedidos con señal y sin señal va seguido de dos meses sin pedido.

Calcula con código y devuelve:
1. [Tienda] La lista de señales usadas y su efecto (más o menos riesgo).
   [Cafeterías] Cuántos pedidos tienen la señal y cuántos no.
2. [Tienda] En validación, el % real de bajas por decil frente a la media. Para los deciles,
   ordena las filas de mayor a menor probabilidad (en un empate, deja el orden por id_suscripcion
   y mes), numéralas 1, 2, 3… y corta esa numeración en 10 grupos con pd.qcut(numero, 10).
   El decil 1 son las 110 filas con más riesgo. No lo cortes con «probabilidad ≥ percentil 90»:
   hay empates y saldrían más filas.
   [Cafeterías] El % que deja de pedir con señal y sin señal, frente a la media de todos los pedidos.
3. [Tienda] Qué % de exactitud tendría un modelo que dijera que nadie se va.
   [Cafeterías] Qué % acertaría decir que ninguna cafetería deja de pedir.
4. [Tienda] El umbral de riesgo alto: el percentil 90 de las probabilidades de septiembre y
   octubre (pandas quantile(0.9)). Lo usarás en la práctica de activación.
   [Cafeterías] No hay umbral: riesgo alto = tener la señal en su último pedido.
5. Un archivo descargable riesgo.csv con una fila por cliente activo hoy. probabilidad_baja va
   en tanto por uno, entre 0 y 1 (13,6 % se escribe 0,136):
   [Tienda] id_cliente y probabilidad_baja de noviembre de 2026. Para calcularla, vuelve a
   entrenar el mismo modelo con todos los meses hasta octubre de 2026. Entran las suscripciones
   activas el 21 de noviembre que se dieron de alta antes de noviembre: filas de mes = 2026-11
   con meses_desde_alta de 1 en adelante y activa_al_cierre = sí.
   [Cafeterías] id_cuenta, senal y probabilidad_baja, para las cafeterías con algún pedido desde
   el 22 de septiembre de 2026 (últimos 60 días). senal = sí si su último pedido de la lista sin
   agosto está por debajo del 80 % de la media de los tres anteriores de esa lista; no en otro
   caso, también si tiene menos de 4 pedidos en la lista. probabilidad_baja = la parte que deja de
   pedir en su grupo (con señal o sin señal), en tanto por uno. Di cuántas tienen senal = sí.
```

**Descarga `riesgo.csv`:** la IA lo deja en su respuesta como un enlace o un archivo; púlsalo para descargarlo. Si solo te enseña el texto, pídele «Dame el archivo para descargar», o copia la tabla a tu hoja de cálculo y guárdala como CSV con ese nombre. Tienda: lo adjuntas en la práctica de LTV. Cafeterías: lo adjuntas en la práctica de activación.

**Comprueba:** tienda, el % de bajas del decil de más riesgo frente a la media; apunta el umbral de riesgo alto del punto 4, lo pide la práctica de activación. Cafeterías, filtra en tu hoja una cafetería con señal y mira a mano si volvió a pedir en los dos meses siguientes. Si la IA dice que acierta casi el 100 %, revisa qué columnas ha usado.

**Errores típicos de la IA:** usar `fecha_baja` (fuga de datos), partir los datos al azar en lugar de por fechas, o presumir de exactitud cuando casi nadie se va cada mes.
