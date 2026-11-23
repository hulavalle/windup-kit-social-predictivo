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
- No uses fecha_baja ni nada calculado a partir de ella: es información del futuro.
- Entrena con los meses de junio de 2025 a agosto de 2026 (meses del calendario 1 a 15, no
  meses_desde_alta) y valida con septiembre y octubre de 2026. Noviembre está incompleto:
  déjalo fuera de la validación.

[Cafeterías] Define que una cafetería deja de pedir si pasa dos meses completos sin pedido.
Señal principal: un pedido por debajo del 80 % de la media de sus tres pedidos anteriores
(sin contar los pedidos de agosto). Mira cada pedido desde el cuarto, hasta los de agosto
de 2026 (para que los dos meses siguientes estén cerrados), y calcula qué % de los pedidos
con señal y sin señal va seguido de dos meses de calendario sin pedido.

Calcula con código y devuelve:
1. La lista de señales usadas y su efecto (más o menos riesgo).
2. En validación: ordena por riesgo, divide en 10 deciles y da el % real de bajas por decil
   frente a la media.
3. Qué % de exactitud tendría un modelo que dijera que nadie se va.
4. El umbral de riesgo alto: la probabilidad con la que empieza el decil de más riesgo en la
   validación (el percentil 90 de las probabilidades de septiembre y octubre). Lo usarás en la
   práctica de activación.
5. Un archivo descargable riesgo.csv con una fila por cliente activo hoy y dos columnas:
   [Tienda] id_cliente y probabilidad_baja de noviembre de 2026. Para calcularla, vuelve a
   entrenar el mismo modelo con todos los meses hasta octubre de 2026. Entran las suscripciones
   activas el 21 de noviembre que se dieron de alta antes de noviembre: filas de mes = 2026-11
   con meses_desde_alta de 1 en adelante y activa_al_cierre = sí.
   [Cafeterías] id_cuenta y probabilidad_baja (el % de bajas de su grupo, con señal o sin señal,
   según su último pedido) para las cafeterías con algún pedido desde el 22 de septiembre de 2026
   (últimos 60 días).
```

**Descarga `riesgo.csv`:** la IA lo deja en su respuesta como un enlace o un archivo; púlsalo para descargarlo. Si solo te enseña el texto, pídele «Dame el archivo para descargar», o copia la tabla a tu hoja de cálculo y guárdala como CSV con ese nombre. Lo adjuntas en la práctica de LTV.

**Comprueba:** el % de bajas del decil de más riesgo frente a la media. Apunta el umbral de riesgo alto del punto 4: lo pide la práctica de activación. Si la IA dice que acierta casi el 100 %, revisa qué columnas ha usado.

**Errores típicos de la IA:** usar `fecha_baja` (fuga de datos), partir los datos al azar en lugar de por fechas, o presumir de exactitud cuando casi nadie se va cada mes.
