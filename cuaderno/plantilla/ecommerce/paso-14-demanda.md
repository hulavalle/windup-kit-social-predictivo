# Paso 14. Demanda

**Qué te llevas.** La previsión de demanda de tu tienda con su rango, la decisión que alimenta, la serie mínima que necesitas, el calendario de eventos y la revisión mensual de la previsión.

## Por qué importa

¿Cuántos kilos tostamos en diciembre? Si la tienda se queda corta, pierde ventas en su mejor mes. Si se pasa, el café pierde frescura en el almacén. Una tienda necesita prever para comprar stock, planificar envíos y repartir el presupuesto de campañas.

Una serie de ventas tiene tres partes:

- **Tendencia**: hacia dónde va. Si la tienda crece, cada año vende más.
- **Temporada**: lo que se repite cada año. Navidad y Black Friday suben; agosto baja.
- **Ruido**: lo que no se explica. Una semana con un envío retrasado, un post que se hizo viral.

Dos reglas. Una previsión sin rango es una opinión: prever no es acertar el número, es saber entre qué números vas a estar. Y una previsión se valida contra semanas que guardaste sin enseñárselas al modelo, igual que el churn del paso 12.

El método más simple funciona bien en muchas tiendas: la misma semana del año anterior, multiplicada por el crecimiento reciente. Se llama ingenuo estacional con crecimiento. Si un método complejo no mejora el error de este en las semanas guardadas, quédate con el simple.

## Ejemplo con Café Fandango

*Ejemplo 14.1. La previsión de la tienda*

| Campo | Café Fandango |
| ------ | ------ |
| Qué prevemos | Kilos por semana, tienda y cafeterías por separado |
| Para qué decisión | Cuánto café verde comprar y cuánto tostar |
| Horizonte | 8 semanas |
| Método | La misma semana del año anterior × el crecimiento de las últimas 8 semanas frente a las mismas del año anterior |
| Crecimiento usado en la tienda | × 1,31 |
| Rango | ± 11,9 %, el rango del 80 % de los errores en las semanas guardadas |
| Cómo se validó | 13 semanas guardadas (17 de agosto a 9 de noviembre de 2026): error medio del 6,0 % y el 85 % de las semanas reales dentro del rango |
| Resultado para diciembre | 2.010 kg entre tienda y cafeterías, entre 1.771 y 2.249 kg |

*Ejemplo 14.2. Previsión semanal de la tienda, en kilos*

| Semana que empieza | Tienda | Total con cafeterías | Rango del total |
| ------ | ------ | ------ | ------ |
| 16 de noviembre de 2026 | 88 | 476 | 419–532 |
| 23 de noviembre de 2026 | 177 | 581 | 512–650 |
| 30 de noviembre de 2026 | 146 | 583 | 514–652 |
| 7 de diciembre de 2026 | 148 | 594 | 523–664 |
| 14 de diciembre de 2026 | 158 | 603 | 531–674 |
| 21 de diciembre de 2026 | 128 | 466 | 410–521 |
| 28 de diciembre de 2026 | 82 | 348 | 306–389 |
| 4 de enero de 2027 | 89 | 489 | 431–547 |

La semana del 23 de noviembre es la de Black Friday: la previsión de la tienda dobla la de la semana anterior.

## Tu proyecto

1. Decide qué prevés y para qué decisión (plantilla 14.1). En una tienda: unidades o pedidos por semana, por producto o familia. La decisión: stock, compras al proveedor, turnos de preparación de pedidos o presupuesto de campañas.
2. Elige la granularidad. Semanas si tus compras al proveedor son semanales o quincenales; meses si son mensuales.
3. Comprueba la serie mínima (plantilla 14.2). Para ver la temporada necesitas al menos un año completo; con dos, la previsión es más estable. Si tienes menos de un año, prevé solo con la tendencia reciente y dilo.
4. Saca la serie de WooCommerce: el informe de **Análisis** de productos o de pedidos, por semana, con la descarga a CSV. Usa unidades vendidas, no ingresos: los precios y los descuentos cambian.
5. Escribe el calendario de eventos (plantilla 14.4): Black Friday, Navidad, rebajas, campañas grandes, roturas de stock del año pasado. Una rotura de stock del año anterior hace que la previsión salga baja: corrígela o quita esa semana.
6. Guarda las últimas 8 a 13 semanas, pide la previsión de esas semanas y mide el error. Después pide la previsión real con su rango.
7. Pon la revisión mensual en el calendario (plantilla 14.3).

### Con tu asistente de IA

Adapta `prompts/s2-b4-demanda.md`:

```text
Te adjunto una serie de [unidades o kilos] por semana de mi tienda y su diccionario.
No hay datos personales. Decisión: [stock, compras, envíos].
Con código:
1. Guarda las últimas 13 semanas sin usarlas.
2. Prevé esas 13 semanas con el método ingenuo estacional con crecimiento: la misma
   semana del año anterior × el crecimiento de las últimas 8 semanas frente a las mismas
   del año anterior. Dame el error medio absoluto en % y el rango del 80 %.
3. Con toda la serie, prevé las próximas 8 semanas con ese rango.
4. Marca las semanas de Black Friday, Navidad y agosto.
Enséñame las fórmulas y dime qué semanas raras has encontrado en la serie.
```

### Cómo comprobarlo

- Rehaz a mano la previsión de una semana: la misma semana del año anterior × el crecimiento.
- Cuenta en cuántas de las semanas guardadas el valor real cae dentro del rango. Si es mucho menos de ocho de cada diez, el rango es demasiado estrecho.
- Cada mes, compara la previsión con lo vendido.

*Plantilla 14.1. Tu previsión*

| Campo | Tu proyecto |
| ------ | ------ |
| Qué prevés (unidades, pedidos, kilos) | |
| Para qué decisión | |
| Granularidad y horizonte | |
| Método | |
| Datos que usas | |
| Cómo lo validas (semanas guardadas y error) | |
| Resultado con su rango | |

*Plantilla 14.2. Tu serie*

| Campo | Tu proyecto |
| ------ | ------ |
| Unidad | |
| Granularidad | |
| Desde cuándo | |
| Semanas o meses completos disponibles | |
| ¿Cubre al menos un año completo? | |
| Semanas raras (roturas de stock, cambios de precio) | |
| Fuente | |

*Plantilla 14.3. Tu revisión mensual*

| Semana | Previsión | Rango | Real | Error % | ¿Dentro del rango? |
| ------ | ------ | ------ | ------ | ------ | -- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Plantilla 14.4. Tu calendario de eventos*

| Fecha | Evento | Efecto esperado | ¿Está en el histórico? |
| ------ | ------ | ------ | -- |
| | | | |
| | | | |
| | | | |
| | | | |

## Errores frecuentes

- Dar una cifra sin rango.
- Validar con las mismas semanas con las que se calculó.
- Prever ingresos en lugar de unidades.
- Copiar la Navidad del año pasado sin mirar si hubo rotura de stock.
- Un método complejo que no mejora al simple.

## Antes de seguir

- [ ] Tu previsión dice qué decisión alimenta.
- [ ] Tienes al menos un año de serie, o dices que la temporada no está.
- [ ] La previsión tiene rango y se validó con semanas guardadas.
- [ ] Tu calendario de eventos está escrito.
- [ ] La revisión mensual tiene fecha y responsable.
