# Sesión 2 · Bucle 5 · Activación y experimento

**Pregunta:** ¿qué hacemos con cada cliente según su riesgo y su valor, y cómo sabremos que ha funcionado?
**Adjunta:** tienda: `riesgo_valor.csv` (lo descargaste al final de la práctica de LTV); cafeterías: `riesgo.csv` (lo descargaste al final de la práctica de churn). Siempre `diccionario.md`. Si no tienes el archivo, vuelve a esa práctica y pídelo otra vez.
**Tienda: cambia `[umbral]`** por el umbral de riesgo alto que apuntaste en la práctica de churn. En Café Fandango es 13,6 %. Cafeterías no usa umbral.

```
Eres responsable de CRM y paid media de Café Fandango.
[Tienda] Te adjunto riesgo_valor.csv: una fila por cliente con su probabilidad de baja
(probabilidad_baja) y su valor esperado en euros (valor_esperado_eur).
[Cafeterías] Te adjunto riesgo.csv: una fila por cafetería activa con id_cuenta, senal (sí si su
último pedido está por debajo del 80 % de la media de sus tres pedidos anteriores, sin contar
agosto) y probabilidad_baja.

1. [Tienda] Cruza riesgo y valor en una matriz 2×2.
   Riesgo alto: probabilidad_baja igual o mayor que [umbral] % (en el archivo va entre 0 y 1:
   13,6 % es 0,136), el umbral del decil de más
   riesgo en la validación del modelo de churn. No lo calcules con este archivo: aquí solo
   están los clientes activos y saldrían más.
   Valor alto: valor_esperado_eur igual o mayor que la mediana.
   Di cuántos clientes caen en cada cuadrante.
   [Cafeterías] Riesgo alto: las que tienen senal = sí. No uses un umbral de probabilidad. No hay columna de
   valor, así que no hay matriz: di cuántas cafeterías tienen la señal y cuántas no.
2. Propón una acción de CRM y una de paid media por cuadrante (tienda) o por grupo (cafeterías),
   por ejemplo: contacto personal, email automático, pedir recomendación, audiencias por valor,
   excluir de captación.
3. Para el cuadrante de valor alto y riesgo alto (tienda) o las cafeterías con la señal
   (cafeterías), rellena esta ficha de experimento:
   hipótesis (Si…, entonces…), etapa AARRR, ICE (impacto, confianza y facilidad de 1 a 10),
   grupo de control (qué % y cómo se elige), métrica primaria, contrapeso, tamaño de muestra
   y duración, y la decisión que tomaremos con cada resultado.
4. Dime con franqueza si hay volumen suficiente para un test o si es mejor implantar la acción
   directamente y vigilarla.
```

**Comprueba:** tienda, que los cuatro cuadrantes suman el total de clientes; cafeterías, filtra `senal` = sí en `riesgo.csv` y cuéntalas; y calcula el tamaño de muestra con una calculadora de tests A/B para comparar con lo que dice la IA.

**Errores típicos de la IA:** prometer que la acción «reducirá el churn un X %» sin grupo de control, o proponer un test con tan pocos clientes que nunca dará un resultado claro.
