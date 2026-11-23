# Paso 11. Cohorte y cliente activo

**Qué te llevas.** La definición de cohorte y de cliente activo de tu tienda, la matriz de retención por canal, la retención bruta, neta y de ingresos, y la rutina para montar la matriz cada mes.

## Por qué importa

La media mezcla a los que se quedan con los que se van; la cohorte los separa. Un churn medio del 8,6 % no dice si los clientes de Instagram y los de TikTok se comportan igual. La matriz de cohortes sí.

Una **cohorte** es un grupo con un rasgo común, una acción y un momento: los suscriptores que se dieron de alta en marzo desde Instagram. Un segmento es otra cosa: un grupo con una característica, sin fecha de entrada. La cohorte dice cuándo entraron; el segmento, qué tienen en común.

La **matriz de retención** pone las cohortes en filas y los meses desde el alta en columnas. Cada celda es el porcentaje de la cohorte que sigue activo ese mes. Las celdas que aún no han llegado van en blanco, no en cero: un blanco es un dato pendiente; un cero sería decir que se fueron todos.

Se lee de dos formas. Por filas, ves envejecer a una cohorte. Por columnas, comparas cohortes a la misma edad: si el mes 3 mejora de una cohorte a la siguiente, el producto o la captación mejoran.

La forma de la curva importa más que el número:

- **Mala**: cae hacia cero. Los clientes no encuentran motivo para quedarse.
- **Buena**: cae al principio y se aplana. La meseta es tu base real de clientes.
- **Sonriente**: se aplana y vuelve a subir, porque vuelven clientes que se habían ido.

Antes de calcular nada hay que definir **activo**. En una suscripción, es la suscripción sin baja al cierre del mes. En compra suelta no hay baja: activo es «ha comprado en el mes» o «ha comprado en los últimos N días». Y no mezcles modelos: la retención de la suscripción y la de la compra suelta van en matrices distintas.

## Ejemplo con Café Fandango

*Ejemplo 11.1. La cohorte de la tienda*

| Campo | Café Fandango |
| ------ | ------ |
| Rasgo | Red de captación (UTM de la primera compra) |
| Acción | Alta de la suscripción |
| Momento | Mes de alta |
| Activo | Suscripción sin baja al cierre del mes |
| Meses que se miran | 1, 3, 6, 9 y 12 |
| Fuente | `suscripciones.csv`: una fila por suscripción y mes |

*Ejemplo 11.2. Retención de la suscripción por red*

| Red | Suscripciones | Mes 1 | Mes 3 | Mes 6 | Mes 9 | Mes 12 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Instagram | 742 | 84 % | 64 % | 58 % | 56 % | 57 % |
| TikTok | 189 | 51 % | 28 % | 19 % | 16 % | 16 % |
| Newsletter | 101 | 83 % | 68 % | 49 % | | |
| Google | 76 | 84 % | 69 % | 58 % | | |
| Directo | 58 | 88 % | 69 % | | | |
| Facebook | 51 | 89 % | | | | |

Solo entran las cohortes que ya han cumplido cada mes: por eso hay celdas en blanco. Instagram se aplana en torno al 57 %. TikTok pierde la mitad en el primer mes y se queda en el 16 %.

*Ejemplo 11.3. Por grupo de canal*

| Grupo | Mes 1 | Mes 3 | Mes 6 | Mes 9 | Mes 12 |
| ------ | ------ | ------ | ------ | ------ | ------ |
| Instagram orgánico e influencer | 86 % | 66 % | 59 % | 58 % | 61 % |
| Meta Ads (Instagram y Facebook) | 82 % | 59 % | 52 % | 51 % | 47 % |
| TikTok | 51 % | 28 % | 19 % | 16 % | 16 % |

*Ejemplo 11.4. Por descuento de entrada*

| Descuento del primer mes | Mes 1 | Mes 3 | Mes 6 | Mes 12 |
| ------ | ------ | ------ | ------ | ------ |
| 0 % | 87 % | 69 % | 60 % | 55 % |
| 20 % | 84 % | 62 % | 54 % | 57 % |
| 50 % | 43 % | 20 % | 14 % | |

El Instagram orgánico tiene una curva sonriente: del 58 % en el mes 9 al 61 % en el mes 12. Los que entran con el 50 % de descuento se van casi tan rápido como los de TikTok.

Para comprobar a mano: la cohorte de junio de 2025 (50 altas) tiene un 56,0 % activo en el mes 6; la de enero de 2026 (67 altas), un 55,2 % en el mes 3.

## Tu proyecto

1. Define tu cohorte (plantilla 11.1): rasgo, acción, momento y qué es activo.
2. Si vendes en compra suelta, define activo con una ventana: «ha comprado en los últimos N días». Elige N mirando el tiempo habitual entre dos compras de tus clientes que repiten (paso 12).
3. Prepara los datos. Necesitas una fila por cliente (o suscripción) y mes, con si estaba activo ese mes y su rasgo. En WooCommerce Subscriptions, una suscripción está activa si su estado es activa o pendiente de cancelación (ya pagó el periodo); en espera, cancelada y caducada no cuentan.
4. Monta la matriz por mes de alta (plantilla 11.2) y otra por canal de captación. Deja en blanco las celdas que no han llegado.
5. Calcula las tres retenciones (plantilla 11.3):
   - **Bruta**: solo cuenta quien sigue activo sin interrupción. Si se va y vuelve, no vuelve a contar en su cohorte. Solo puede bajar.
   - **Neta**: cuenta a quien está activo ese mes, aunque se fuera entre medias. Puede subir: es la que da la curva sonriente.
   - **De ingresos**: ingresos de la cohorte en el mes k / ingresos de la cohorte en el mes de alta. Si los que se quedan compran más, puede superar a la de clientes.
6. Dibuja la curva de cada canal y escribe si es mala, buena o sonriente, y dónde se aplana.
7. Compara con GA4 si quieres: **Explorar** > **Exploración de cohortes**, con criterio de inclusión «transacción» y de retorno «transacción». Ten en cuenta sus límites: usa datos del dispositivo, no admite los datos modelados por consentimiento y llega a 60 cohortes como máximo. Para clientes y dinero, manda la tienda.
8. Pon la rutina mensual en el calendario (plantilla 11.4).

### Con tu asistente de IA

Adapta `prompts/s2-b1-cohortes.md`:

```text
Te adjunto [archivo de suscripciones o pedidos] y su diccionario. No hay datos personales.
Activo significa: [tu definición].
Con código, construye la matriz de retención: filas = mes de alta, columnas = meses
desde el alta (1, 3, 6, 9, 12), celdas = % de la cohorte activo ese mes.
Las celdas que aún no han llegado van vacías, no en cero. El último mes está incompleto:
no lo cuentes como cerrado.
Haz después la misma matriz por canal de captación, solo con cohortes que han cumplido
cada mes. Dame retención bruta y neta, y dime la forma de la curva de cada canal.
```

### Cómo comprobarlo

1. Elige una cohorte y un mes, como la de junio en el mes 6.
2. Filtra en tu hoja las altas de junio: cuéntalas.
3. De esas, cuenta cuántas siguen activas al cierre del mes 6.
4. Divide. Debe dar la celda de la matriz.

*Plantilla 11.1. Tu cohorte*

| Campo | Tu proyecto |
| ------ | ------ |
| Rasgo | |
| Acción | |
| Momento | |
| Activo | |
| Meses que se miran | |
| Fuente | |

*Plantilla 11.2. Tu matriz de retención*

| Cohorte (mes de alta) | Altas | Mes 1 | Mes 3 | Mes 6 | Mes 9 | Mes 12 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

*Plantilla 11.3. Tus tres retenciones*

| Medida | Definición en tu tienda | Fórmula | Mes 3 | Mes 12 |
| ------ | ------ | ------ | ------ | ------ |
| Retención bruta | | | | |
| Retención neta | | | | |
| Retención de ingresos | | | | |

*Plantilla 11.4. Tu rutina mensual*

| Tarea | Cuándo | Quién | Archivo |
| ------ | ------ | ------ | ------ |
| Exportar suscripciones o pedidos con seudónimos | | | |
| Añadir el mes cerrado a la matriz | | | |
| Comprobar una celda a mano | | | |
| Comparar la nueva cohorte con las anteriores en el mes 1 | | | |
| Anotar cambios de precio o promociones del mes | | | |

## Errores frecuentes

- Poner ceros en las celdas que no han llegado. La retención parece desplomarse.
- Contar el mes en curso como cerrado.
- Mezclar suscripción y compra suelta en la misma matriz.
- Mirar solo la media de todas las cohortes. Esconde que un canal trae clientes que se van.
- Usar la exploración de cohortes de GA4 como fuente de clientes. Cuenta dispositivos, no clientes.

## Antes de seguir

- [ ] Tu definición de activo está escrita y sirve para tu modelo de venta.
- [ ] La matriz tiene las celdas pendientes en blanco.
- [ ] Tienes la matriz por canal de captación.
- [ ] Sabes si tu retención bruta, neta y de ingresos difieren, y por qué.
- [ ] Comprobaste una celda a mano.
- [ ] La rutina mensual tiene responsable.
