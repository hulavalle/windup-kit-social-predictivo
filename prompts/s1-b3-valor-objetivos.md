# Sesión 1 · Bucle 3 · Valor de los objetivos

**Pregunta:** ¿cuánto vale en euros cada objetivo de mi carril?
**Adjunta:** tienda: `clientes.csv` y `redes_posts.csv`; cafeterías: `leads.csv`, `cuentas_b2b.csv` y `redes_posts.csv`. Siempre `diccionario.md` (trae los márgenes).

```
Eres analista de marketing de Café Fandango, una tienda online de café.
Te adjunto [archivos] y el diccionario de datos, que incluye los márgenes.
Periodo: de junio de 2025 a octubre de 2026 (noviembre está incompleto).

Calcula con código, no de memoria, el valor en euros de estos objetivos:
[Tienda]
1. Una venta suelta: ticket medio de la primera compra suelta × margen del café.
   Ticket medio = media de importe_primera_compra de los clientes captados en el periodo
   con tipo_primera_compra = suelta. Dalo en total y por red.
2. Un alta de suscripción: primer pago × margen de la suscripción. Primer pago = precio
   de la suscripción, 24 € (diccionario). Di también cuánto baja con el primer pago medio
   real de las altas del periodo, que llevan descuento de entrada.
3. Un suscriptor de la newsletter: no hay datos de newsletter en los archivos. No calcules nada:
   escribe la fórmula (% de suscriptores de la newsletter que compran × valor de una venta suelta)
   y di qué dato me falta para calcularla.
4. Notoriedad (Owned Media Value) de octubre de 2026: impresiones orgánicas del mes / 1.000 × CPM medio
   de paid social. Impresiones orgánicas: las de octubre de todas las publicaciones con
   tipo_publicacion = orgánico (tres redes y dos carriles). El CPM sale de redes_posts.csv con todo
   el periodo: coste / impresiones × 1.000 de las publicaciones promocionadas con anuncio de Meta
   (sin las de LinkedIn).

[Cafeterías]
1. Un lead, por primera conversión: tasa de cierre × primer pedido medio × margen B2B.
   - Tasa de cierre = leads con estado = cliente / todos los leads, solo con los leads de junio
     de 2025 a agosto de 2026 (fecha_lead). Esos ya están resueltos; los de septiembre en
     adelante todavía no han tenido tiempo de cerrar.
   - Primer pedido medio = importe medio de los pedidos con meses_desde_alta = 0 en cuentas_b2b.csv.
2. Un lead, con el primer año: pedido mensual medio × 12 × tasa de cierre × margen B2B.
   Pedido mensual medio = importe medio de los pedidos con meses_desde_alta de 1 en adelante.
3. Notoriedad (Owned Media Value) de octubre de 2026: impresiones orgánicas del mes / 1.000 × CPM medio
   de paid social. Impresiones orgánicas: las de octubre de todas las publicaciones con
   tipo_publicacion = orgánico (tres redes y dos carriles). El CPM sale de redes_posts.csv con todo
   el periodo: coste / impresiones × 1.000 de las publicaciones promocionadas con anuncio de Meta
   (sin las de LinkedIn).

Para cada objetivo enseña la fórmula, los datos que has usado (con filtros y fechas) y el resultado.
Dime qué supuestos has tenido que hacer.
```

**Comprueba:** calcula a mano en tu hoja uno de los datos de entrada (el ticket medio o la tasa de cierre) con un filtro. Si no coincide, pide a la IA el filtro exacto que usó.

**Errores típicos de la IA:** contar como resueltos leads que todavía están en curso, o usar el importe con IVA o sin descuento.
