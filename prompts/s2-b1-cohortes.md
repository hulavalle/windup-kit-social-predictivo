# Sesión 2 · Bucle 1 · Matriz de cohortes

**Pregunta:** ¿los clientes de unas redes se quedan más que los de otras?
**Adjunta:** tienda: `suscripciones.csv`; cafeterías: `cuentas_b2b.csv`. Siempre `diccionario.md`.

```
Eres analista de retención de Café Fandango. Te adjunto [archivo] y el diccionario.

[Tienda] Cohorte = mes de alta de la suscripción. Activo en el mes k = activa_al_cierre = "sí"
en la fila con meses_desde_alta = k. Si la suscripción no tiene fila en ese mes (se dio de
baja antes), cuenta como no activa: el denominador es siempre la cohorte entera.
[Cafeterías] Cohorte = mes del primer pedido. Activa en el mes k = tiene un pedido con
meses_desde_alta = k.

Calcula con código:
1. La matriz de retención: filas = cohortes, columnas = meses desde el alta (0 a 16),
   celdas = % de la cohorte activo. Las celdas que la cohorte todavía no ha alcanzado
   van vacías, no en cero. Noviembre de 2026 está incompleto: no lo uses como mes cerrado.
2. La misma retención por red de captación en los meses 1, 3, 6 y 12, contando solo las
   cohortes que ya han cumplido ese mes.
3. Un gráfico de curvas por red.

Enseña el código y di cuántas cohortes entran en cada celda de la tabla del punto 2.
```

**Comprueba:** elige una cohorte y un mes, filtra en tu hoja y cuenta a mano cuántos siguen activos. Tiene que coincidir con la celda de la IA.

**Errores típicos de la IA:** rellenar con ceros las celdas que aún no han llegado (hunde la curva) o contar noviembre como mes cerrado.
