# Sesión 2 · Bucle 4 · Previsión de demanda

**Pregunta:** ¿cuántos kilos de café hará falta tostar las próximas 8 semanas?
**Adjunta:** `ventas_semanales.csv` y `diccionario.md`.

```
Eres analista de operaciones de Café Fandango. Te adjunto ventas_semanales.csv y el diccionario.

Calcula con código, para tienda y cafeterías por separado:
1. Describe la serie: tendencia, temporada (Black Friday, Navidad, agosto) y ruido.
2. Guarda las últimas 13 semanas sin usarlas. Con el resto, prevé esas 13 semanas con un
   método sencillo: kg de la misma semana del año anterior (52 semanas antes) × crecimiento.
   Crecimiento = kg de las 8 semanas anteriores a la previsión / kg de esas mismas 8 semanas
   del año anterior. Error de cada semana = real / previsto − 1. Da el error medio absoluto en %.
3. Con toda la serie, prevé las próximas 8 semanas con un rango del 80 %:
   previsión × (1 ± 1,28 × desviación típica de los errores del punto 2).
4. Un gráfico con la serie real, las 13 semanas guardadas y la previsión con su banda de rango.

Devuelve la tabla de las 8 semanas (tienda, cafeterías, total, rango) y el total de diciembre
(suma de las semanas que empiezan en diciembre, con su rango).
```

**Comprueba:** ¿cuántas de las 13 semanas guardadas caen dentro del rango? Si caen casi todas o casi ninguna, el rango está mal calculado.

**Errores típicos de la IA:** dar un solo número sin rango, o validar con semanas que ya ha usado para ajustar el modelo.
