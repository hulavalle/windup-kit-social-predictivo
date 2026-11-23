# Sesión 2 · Bucle 3 · LTV y ROI recalculado

**Pregunta:** ¿cuánto vale un cliente de cada red, y cambia eso el ROI de la sesión 1?
**Adjunta:** tienda: `clientes.csv`, `pedidos.csv`, `suscripciones.csv` y `costes.csv`; cafeterías: `cuentas_b2b.csv`, `leads.csv` y `costes.csv`. Siempre `diccionario.md` y el `riesgo.csv` que descargaste en la práctica de churn.

```
Eres analista de Café Fandango. Te adjunto [archivos] y el diccionario (con los márgenes).
Periodo: de junio de 2025 a octubre de 2026 (noviembre está incompleto).

Calcula con código el LTV esperado a 24 meses por red de captación:
LTV esperado = suma, para cada mes k de 0 a 23, de P(seguir activo en el mes k) × margen medio
de un cliente activo en ese mes.
- Mes k = meses de calendario desde la primera compra (tienda: fecha_alta de clientes.csv)
  o desde el primer pedido (cafeterías: meses_desde_alta de cuentas_b2b.csv).
- Activo en el mes k: [Tienda] tiene la suscripción activa al cierre de ese mes o hace alguna
  compra ese mes (pedidos.csv). [Cafeterías] hace un pedido ese mes.
- Margen del mes: importe de sus pedidos de ese mes × margen (suscripción 40 %, café 45 %,
  cafeterías 35 %).
- Meses 0 a 11: observados, solo con los clientes cuyo mes k ya ha terminado (hasta octubre
  de 2026). Meses 12 a 23: prolonga la caída media mensual de P × margen entre los meses 6 y 11
  (como mucho 0,99 por mes) y dilo.
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

Devuelve una tabla por red con: P(activo) en el mes 6, LTV esperado, ROI por primera
conversión, ROI con LTV y LTV/CAC. Enseña fórmulas y supuestos.

Por último, une riesgo.csv con el valor esperado de cada cliente de ese archivo: el margen
de los próximos 12 meses si sigue activo (curva de retención de su red desde su antigüedad),
sin multiplicarlo por su probabilidad de baja.
[Tienda] Valor = 24 € × 40 % × suma, para j de 1 a 12, de R(k + j) / R(k). R es la curva de
retención de la suscripción de su red (% con activa_al_cierre = sí en cada meses_desde_alta,
solo cohortes que ya han cumplido ese mes y hasta el último mes con al menos 40 suscripciones)
y k es su meses_desde_alta en noviembre. Donde la curva no llega, prolóngala con la caída media
mensual de sus 4 últimos meses (entre 0,80 y 0,995 por mes; 0,90 si tiene menos de 5 meses).

Dame un archivo descargable riesgo_valor.csv por cliente y tres columnas: id_cliente (o id_cuenta), probabilidad_baja y valor_esperado_eur.
```

**Descarga `riesgo_valor.csv`:** la IA lo deja en su respuesta como un enlace o un archivo; púlsalo para descargarlo. Si solo te enseña el texto, pídele «Dame el archivo para descargar», o copia la tabla a tu hoja de cálculo y guárdala como CSV con ese nombre. Lo adjuntas en la práctica de activación.

**Comprueba:** para una red, multiplica a mano la P(activo) del mes 6 por su margen medio y compáralo con lo que la IA suma en ese mes.

**Errores típicos de la IA:** multiplicar dos veces por la probabilidad de seguir, o usar el ingreso medio de todos los clientes en lugar del de los que siguen activos.
