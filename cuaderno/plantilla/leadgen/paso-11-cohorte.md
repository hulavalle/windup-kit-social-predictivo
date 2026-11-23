# Paso 11. Cohorte y cliente activo

**Qué te llevas.** La definición de cohorte y de cliente activo de tu negocio, la matriz de retención de cuentas por mes del primer pedido y por canal, la cohorte de leads con el tiempo hasta el cierre, la retención bruta, neta y de ingresos, y la rutina para montar la matriz cada mes.

## Para qué sirve

Una media mezcla a los clientes que se quedan con los que se van. La cohorte los separa. Una cohorte es un grupo con un rasgo común, una acción y un momento: las cafeterías que hicieron su primer pedido en marzo y llegaron desde LinkedIn.

La matriz de retención pone las cohortes en filas y los meses desde la acción en columnas. Cada celda dice qué porcentaje de la cohorte sigue activo. Se lee por filas (una cohorte que envejece) y por columnas (cohortes distintas a la misma edad). Las celdas que aún no han llegado van en blanco, no en cero.

La forma de la curva dice más que el número. Si cae hacia cero, el cliente no encuentra valor. Si se aplana, tienes una base que se queda. Si vuelve a subir, recuperas clientes que se habían ido.

En captación de leads hay dos cohortes útiles. La de cuentas, por mes del primer pedido, dice cuánto se quedan los clientes. La de leads, por mes del lead, dice cuánto tardan en cerrar y qué parte cierra a 30, 60 y 90 días.

Sin contrato, «activo» hay que definirlo. Una cafetería puede saltarse un mes y volver. Por eso hay tres retenciones. La bruta cuenta solo a quien sigue sin interrupción. La neta cuenta a quien está activo en ese mes, aunque se saltara alguno antes. La de ingresos compara lo que factura la cohorte en el mes k con lo que facturaba al principio: puede pasar del 100 % si las cuentas crecen.

## Cómo se hace

1. Define la acción que crea la cohorte: el primer pedido, o el lead.
2. Define el momento: el mes de esa acción.
3. Elige el rasgo para comparar: el canal de captación de las UTMs.
4. Define «activo»: pedido en el mes, o pedido en los últimos N días.
5. Monta la matriz. En una hoja de cálculo: tabla dinámica con el mes del primer pedido en filas, `meses_desde_alta` en columnas y el recuento distinto de cuentas en valores. Divide cada celda entre la columna del mes 0.
6. Repite la matriz por canal.
7. Calcula la retención neta y la de ingresos con los importes en lugar de las cuentas.
8. Monta la cohorte de leads: mes del lead en filas y días hasta el cierre en columnas.
9. Cada mes, añade la cohorte nueva y una columna más. No recalcules las antiguas salvo que cambie la definición.

### Con tu asistente de IA

Usa el prompt de `prompts/s2-b1-cohortes.md` con tu export de pedidos. Pide la matriz por canal, con celdas sin llegar en blanco, y la retención neta y la de ingresos. Pide también que diga cuántas cuentas tiene cada cohorte: una celda con cuatro cuentas no permite conclusiones.

### Cómo comprobarlo

Elige una cohorte y un mes. Con un filtro, cuenta las cuentas de esa cohorte y cuántas pidieron ese mes. Divide. Tiene que salir la cifra de la celda.

## Ejemplo con Fandango para cafeterías

*Ejemplo 11.1. Definiciones*

| Campo | Fandango para cafeterías |
| --- | --- |
| Rasgo | Red de captación (UTM del lead) |
| Acción | Primer pedido |
| Momento | Mes del primer pedido |
| Activo | Pedido en el mes. Para el informe, cliente activo = pedido en los últimos 60 días |
| Meses que se miran | 3, 6 y 12 |
| Cuidado | En agosto las cafeterías piden menos: no es una baja |

*Ejemplo 11.2. Cuentas que siguen pidiendo en el mes 6*

| Red | Pedido mensual medio | Cuentas que piden en el mes 6 | Cuentas con 6 meses |
| --- | --- | --- | --- |
| Instagram | 206 € | 27 % | 11 |
| LinkedIn | 401 € | 75 % | 48 |
| Google | 388 € | 50 % | 8 |
| Directo | 274 € | 75 % | 4 |

LinkedIn trae cuentas que piden casi el doble y que se quedan casi tres veces más. El 75 % de Directo sale de 4 cuentas: no se puede concluir nada. De las 122 cafeterías captadas, 85 están activas.

*Ejemplo 11.3. Cohorte de leads*

| Campo | Fandango para cafeterías |
| --- | --- |
| Acción | Envío del formulario |
| Momento | Mes del lead |
| Celdas | % de leads que ya son cliente a los 30, 60 y 90 días |
| Para qué | Saber cuándo un lead está resuelto y cuándo calcular la tasa de cierre |
| Datos | `fecha_lead` y `fecha_cliente` de `leads.csv` |
| Resultado | Se calcula con tus datos |

## Tu proyecto

*Plantilla 11.1. Tus definiciones*

| Campo | Tu proyecto |
| --- | --- |
| Rasgo | |
| Acción | |
| Momento | |
| Activo | |
| Meses que se miran | |
| Cuidado (temporada, pausas) | |

*Plantilla 11.2. Tu matriz de retención*

| Cohorte | Cuentas | Mes 1 | Mes 3 | Mes 6 | Mes 12 |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Plantilla 11.3. Retención por canal en el mes 6*

| Canal | Cuentas con 6 meses | Retención bruta | Retención neta | Retención de ingresos |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 11.4. Tu cohorte de leads*

| Mes del lead | Leads | Clientes a 30 días | Clientes a 60 días | Clientes a 90 días |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 11.5. Rutina mensual*

| Tarea | Quién | Día del mes |
| --- | --- | --- |
| Exportar pedidos y leads con identificadores seudónimos | | |
| Añadir la cohorte nueva y una columna | | |
| Comprobar una celda a mano | | |
| Comentar la curva en el informe | | |

## Errores frecuentes

- Poner un cero en las celdas que aún no han llegado. Hunde la media de las columnas de la derecha.
- Comparar cohortes de tamaño muy distinto sin decirlo.
- Mezclar modelos de negocio. Si tienes clientes con contrato y sin contrato, haz dos matrices.
- Tomar un mes flojo de temporada por una baja. Mira el mismo mes del año anterior.
- Usar la exploración de cohortes de GA4 para clientes B2B. Va por dispositivo, no ve los pedidos del CRM y no incluye los datos modelados por consentimiento.

## Antes de seguir

- [ ] «Activo» tiene una definición escrita, con su ventana.
- [ ] La matriz tiene las celdas sin llegar en blanco.
- [ ] Cada cohorte dice cuántas cuentas tiene.
- [ ] Tienes retención bruta, neta y de ingresos por canal.
- [ ] Sabes cuántos días tarda un lead en cerrar.
- [ ] Has comprobado una celda a mano.
