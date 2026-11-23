# Sesión 2 · Bucle 3 · LTV y ROI recalculado

**Pregunta:** ¿cuánto vale un cliente de cada red, y cambia eso el ROI de la sesión 1?
**Adjunta:** tienda: `clientes.csv`, `pedidos.csv`, `suscripciones.csv` y `costes.csv`; cafeterías: `cuentas_b2b.csv`, `leads.csv` y `costes.csv`. Siempre `diccionario.md`. Tienda: también el `riesgo.csv` que descargaste en la práctica de churn (cafeterías no lo necesita aquí).

```
Eres analista de Café Fandango. Te adjunto [archivos] y el diccionario (con los márgenes).
Periodo: de junio de 2025 a octubre de 2026 (noviembre está incompleto).

Calcula con código el LTV esperado a 24 meses por red de captación. [Cafeterías] Junta Google
y Directo en un solo grupo, «Google y directo»: tienen pocas cuentas.
LTV esperado = suma, para cada mes k de 0 a 23, de P(seguir activo en el mes k) × margen medio
de un cliente activo en ese mes.
- Mes k = meses de calendario desde la primera compra (tienda: fecha_alta de clientes.csv)
  o desde el primer pedido (cafeterías: meses_desde_alta de cuentas_b2b.csv).
- Activo en el mes k: [Tienda] tiene la suscripción activa al cierre de ese mes o hace alguna
  compra ese mes (pedidos.csv). [Cafeterías] hace un pedido ese mes.
- Margen del mes: importe de sus pedidos de ese mes × margen (suscripción 40 %, café 45 %,
  cafeterías 35 %). Un cliente activo sin pedidos ese mes cuenta con 0 €.
- Meses 0 a 11: observados, solo con los clientes cuyo mes k ya ha terminado (hasta octubre
  de 2026). Meses 12 a 23: prolonga con caída geométrica. Llama V(k) a P × margen del mes k.
  q = (V(11) / V(6)) elevado a 1/5, como mucho 0,99 (si V(6) o V(11) es 0, q = 0,90).
  V(k) = V(11) × q elevado a (k − 11). Di qué q sale en cada red.
- El margen medio tiene que ser el de los clientes que SIGUEN activos: no lo multipliques
  por la probabilidad si ya incluye a los que se fueron (contarías el riesgo dos veces).

Después calcula el ROI por red de dos formas, con los clientes captados en el periodo y el
coste completo del carril en el periodo (costes.csv: anuncios + influencer + horas):
- ROI por primera conversión.
  [Tienda] (ingresos de la primera compra × margen − coste completo) / coste completo; el margen
  depende de tipo_primera_compra (suelta 45 %, suscripción 40 %).
  [Cafeterías] (leads × 16,37 € − coste completo) / coste completo. Leads: los de fecha_lead
  en el periodo. 16,37 € es el valor de un lead de la sesión 1 (tasa de cierre × primer pedido
  medio × margen).
- ROI con LTV = (clientes captados × LTV esperado − coste completo) / coste completo.
  Clientes captados: [Tienda] fecha_alta en el periodo. [Cafeterías] fecha_cliente en el periodo.
- LTV/CAC = LTV esperado / (coste completo / clientes captados).
- Las redes sin filas en costes.csv (Google, Newsletter y Directo) no tienen coste: da su LTV,
  pero no calcules su ROI ni su LTV/CAC. Escribe «sin coste».

Devuelve una tabla por red con: P(activo) en el mes 6, LTV esperado, ROI por primera
conversión, ROI con LTV y LTV/CAC. Enseña fórmulas y supuestos.

[Tienda] Por último, une riesgo.csv con el valor esperado de cada cliente de ese archivo: el margen
de los próximos 12 meses si sigue activo (curva de retención de su red desde su antigüedad),
sin multiplicarlo por su probabilidad de baja.
Valor = 24 € × 40 % × suma, para j de 1 a 12, de R(k + j) / R(k). R es la curva de
retención de la suscripción de su red (red de suscripciones.csv): en cada meses_desde_alta,
% de suscripciones con activa_al_cierre = sí, solo de las que ya han cumplido ese mes (hasta
octubre de 2026). Las que se dieron de baja antes no tienen fila ese mes: cuentan en el
denominador como no activas. La curva para en el primer mes con menos de 40 suscripciones que lo hayan
cumplido. k es su meses_desde_alta en noviembre. Donde la curva no llega, prolóngala mes a mes
con q = (último R / R de cuatro meses antes) elevado a 1/4, entre 0,80 y 0,995 (0,90 si la
curva tiene menos de 5 meses).
Dame un archivo descargable riesgo_valor.csv por cliente con tres columnas: id_cliente,
probabilidad_baja y valor_esperado_eur.
[Cafeterías] No hagas riesgo_valor.csv: la matriz de riesgo × valor es solo de la tienda. En la
práctica de activación usarás el riesgo.csv de la práctica de churn.
```

**Descarga `riesgo_valor.csv` (tienda):** la IA lo deja en su respuesta como un enlace o un archivo; púlsalo para descargarlo. Si solo te enseña el texto, pídele «Dame el archivo para descargar», o copia la tabla a tu hoja de cálculo y guárdala como CSV con ese nombre. Lo adjuntas en la práctica de activación.

**Comprueba:** para una red, multiplica a mano la P(activo) del mes 6 por su margen medio y compáralo con lo que la IA suma en ese mes.

**Errores típicos de la IA:** multiplicar dos veces por la probabilidad de seguir, o usar el ingreso medio de todos los clientes en lugar del de los que siguen activos.
