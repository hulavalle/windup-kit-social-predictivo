# Sesión 1 · Bucle 5 · ROI por red

**Pregunta:** con unos 1.500 € al mes en redes, ¿qué red y qué formato devuelven más?
**Adjunta:** tienda: `clientes.csv`, `costes.csv`, `redes_posts.csv`, `ga4_adquisicion.csv` y `diccionario.md`; cafeterías: `leads.csv`, `cuentas_b2b.csv`, `costes.csv`, `redes_posts.csv`, `ga4_adquisicion.csv` y `diccionario.md`.

```
Eres analista de marketing de Café Fandango. Te adjunto [archivos] y el diccionario de datos.
Periodo: de junio de 2025 a octubre de 2026 (noviembre está incompleto).

[Tienda]
Calcula con código, por red de captación (Instagram, Facebook, TikTok):
clientes captados, ingresos de la primera compra, coste completo del carril tienda
(anuncios + influencer + horas, de costes.csv), CAC, ROAS (ingresos / gasto en anuncios)
y ROI = (ingresos de la primera compra × margen − coste completo) / coste completo.
El margen depende del tipo de primera compra (suelta o suscripción): está en el diccionario.

[Cafeterías]
Calcula con código, por red (Instagram, LinkedIn):
- leads: los de leads.csv con fecha_lead dentro del periodo;
- cualificados: de esos leads, los que tienen fecha_cualificado;
- clientes: cafeterías con fecha_cliente (primer pedido) dentro del periodo;
- coste completo del carril cafeterías (costes.csv, mismo periodo), coste por lead,
  coste por cualificado y coste por cliente;
- ROI por primera conversión = (leads × valor de un lead − coste completo) / coste completo.
  El valor de un lead es el de la práctica de valor de los objetivos: 16,37 €.

Y por formato (reel, carrusel, imagen, vídeo, post): en redes_posts.csv cada publicación
tiene formato y utm_content, y utm_content casa con ga4_adquisicion.csv. Une los dos archivos
por utm_content y da, por formato: publicaciones, coste (coste_eur), sesiones y compras
e ingresos (tienda) o leads (cafeterías) de GA4, y coste por compra o por lead.
Si un utm_content corresponde a más de un formato, dilo.

Devuélvelo en dos tablas (por red y por formato) y debajo escribe la fórmula de cada columna
y los supuestos.
No llames ROI al ROAS: son cifras distintas.
```

**Comprueba:** con una tabla dinámica, cuenta los clientes (o los leads) de una red y suma el coste de otra. Las dos cifras tienen que coincidir con las de la IA.

**Para tu proyecto:** sin inversión en anuncios, tu coste completo son las horas dedicadas a redes × €/hora, más el presupuesto de prueba que propongas (cuaderno, paso 7).
