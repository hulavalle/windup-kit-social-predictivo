# Paso 13. LTV

**Qué te llevas.** La fórmula de LTV de tu tienda, el LTV esperado por canal, la relación LTV/CAC, el ROI de la sesión 1 recalculado con el LTV y la configuración de las pujas por valor.

## Por qué importa

¿Cuánto vale un cliente de cada canal? Depende de cuánto se quede. El ROI de la sesión 1 miraba la primera compra, y en una tienda que vende suscripción o donde los clientes repiten, eso es una parte pequeña del valor.

Hay tres formas de calcular el LTV, de más simple a más fiable:

- **Histórico**: ingreso medio por cliente y mes × vida media en meses. Fácil, pero solo vale si los clientes de hoy se comportan como los de ayer.
- **Con churn**: (ingreso mensual × margen) / churn mensual. Supone que el churn es constante, y casi nunca lo es: se van más al principio.
- **Esperado**: la suma, mes a mes, de la probabilidad de seguir activo ese mes × el margen que deja si sigue activo. Usa la curva de retención de cada canal (paso 11).

Un aviso en el LTV esperado: el margen tiene que ser **el de los clientes que siguen activos**, no la media de todos. Si usas la media de todos, que ya incluye a los que se fueron con margen cero, y después multiplicas por la probabilidad de seguir, cuentas el riesgo dos veces y el LTV sale bajo.

Con el LTV, el **LTV/CAC** dice cuánto vale un cliente frente a lo que cuesta captarlo. Y el ROI de la sesión 1 se recalcula con el LTV en lugar de la primera compra.

La Recomendación también suma: un cliente que trae a otro vale más que su ticket. Si mides el código de amigo (paso 1), puedes añadir al LTV de cada cliente el margen de los clientes que trajo.

Y el LTV sirve para pujar. Google Ads y Meta pueden optimizar por **valor**, no solo por número de compras. Si les das el valor de vida en lugar del ticket, buscan clientes que se quedan.

## Ejemplo con Café Fandango

*Ejemplo 13.1. LTV esperado a 24 meses por red*

| Red | Clientes | Activos en el mes 6 | Margen si activo, mes 6 | Activos en el mes 11 | LTV observado (meses 0 a 11) | LTV esperado a 24 meses |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Instagram | 1.285 | 37 % | 9,27 € | 34 % | 48 € | 82 € |
| Google | 278 | 24 % | 10,50 € | 23 % | 32 € | 59 € |
| Newsletter | 248 | 24 % | 9,15 € | 19 % | 35 € | 47 € |
| Directo | 186 | 24 % | 8,79 € | 12 % | 34 € | 40 € |
| Facebook | 205 | 15 % | 9,27 € | 10 % | 25 € | 32 € |
| TikTok | 1.076 | 5 % | 9,02 € | 3 % | 11 € | 13 € |

Activo en la tienda es tener la suscripción sin baja o haber hecho una compra suelta en el mes. Los meses 0 a 11 están observados; del 12 al 23 se prolonga la caída media de los meses 6 a 11.

*Ejemplo 13.2. ROI recalculado con el LTV*

| Red | Coste completo | Valor con LTV | ROI 1.ª compra | ROI con LTV | LTV/CAC |
| ------ | ------ | ------ | ------ | ------ | ------ |
| Instagram | 12.943 € | 99.683 € | −23 % | +670 % | 7,7 |
| Facebook | 3.401 € | 6.174 € | −54 % | +82 % | 1,8 |
| TikTok | 2.660 € | 13.375 € | +97 % | +403 % | 5,0 |

Valor con LTV = clientes captados × LTV esperado. Con el LTV gana Instagram: el canal barato era el caro.

*Ejemplo 13.3. El LTV con churn de la suscripción*

| Dato | Valor | De dónde sale |
| ------ | ------ | ------ |
| Ingreso mensual por suscriptor | 24 € | Precio de la suscripción |
| Margen | 40 % | Diccionario de datos |
| Churn mensual | 8,6 % (últimos seis meses) | Suscripciones |
| LTV = (ingreso × margen) / churn | (24 € × 40 %) / 8,6 % | Calcúlalo tú y compáralo con el LTV esperado |

## Tu proyecto

1. Calcula el LTV con churn (plantilla 13.1). Es la cifra rápida para empezar.
2. Calcula el LTV esperado por canal (plantilla 13.2):
   - Toma la curva de retención de cada canal del paso 11 (probabilidad de seguir activo en cada mes desde el alta).
   - Calcula el margen medio de los clientes activos en cada mes: solo de los que siguen.
   - Multiplica mes a mes y suma. Elige un horizonte: 12 o 24 meses. Si no tienes tantos meses observados, prolonga la caída de los últimos meses y dilo.
3. Saca el CAC de cada canal del paso 7 y calcula el LTV/CAC.
4. Recalcula el ROI de la sesión 1 (plantilla 13.3): (clientes × LTV esperado − coste completo) / coste completo.
5. Escribe qué cambia en el reparto del presupuesto.
6. Configura las pujas por valor (plantilla 13.4), en el apartado de abajo.

### Las pujas por valor

**En Google Ads.** La compra de tu tienda llega con su `value` desde GA4 o desde la etiqueta de conversión. Para que el algoritmo busque clientes que se quedan:

1. Decide qué valor envías. Lo más simple: un valor distinto según el tipo de primera compra. El alta de suscripción lleva el LTV esperado de un suscriptor; la compra suelta, el de un comprador suelto. Calcúlalos como en este paso, separando los clientes por tipo de primera compra.
2. Envía ese valor con la conversión: en la etiqueta de GTM, con una variable que cambia según `item_category`, o con la importación de conversiones si calculas el valor fuera de la web.
3. Comprueba los requisitos que pide la ayuda de Google Ads: al menos 15 conversiones al mes en la acción que optimizas, con al menos dos valores distintos de cero, y nada de conversiones con valor 0.
4. Cambia la estrategia a **Maximizar el valor de conversión**, con o sin ROAS objetivo. Deja al menos dos semanas de aprendizaje y unas cuatro semanas, o tres ciclos de conversión, antes de cambiar nada.
5. Si te interesa captar clientes nuevos, el objetivo de adquisición de clientes de Google Ads permite pujar más por un cliente nuevo que por uno que ya compró. Necesita tu lista de clientes (paso 15).

**En Meta Ads.** La optimización por valor pide que el píxel o la API de conversiones envíen el evento de compra con `value` y `currency`, con valores distintos entre compras. Revisa en la ayuda de Meta los requisitos actuales antes de activarla.

### Con tu asistente de IA

Adapta `prompts/s2-b3-ltv.md`:

```text
Te adjunto [clientes, pedidos y suscripciones] y su diccionario. No hay datos personales.
Activo significa: [definición]. Margen: [margen por tipo de producto].
Con código, por canal de captación:
1. Probabilidad de seguir activo en cada mes desde el alta (0 a 11), solo con cohortes
   que ya han cumplido ese mes.
2. Margen medio en cada mes de los clientes que siguen activos (solo de ellos,
   para no contar el riesgo dos veces).
3. LTV esperado a [12 o 24] meses = suma de probabilidad × margen. Si faltan meses,
   prolonga la caída media de los últimos y dime cómo.
4. Con este coste completo por canal [tabla], el LTV/CAC y el ROI con LTV.
Enséñame las fórmulas y los supuestos.
```

### Cómo comprobarlo

- Rehaz a mano el LTV de un canal con sus probabilidades y márgenes de los tres primeros meses: la suma parcial debe cuadrar.
- El LTV esperado nunca puede ser menor que el margen de la primera compra.
- Pide a la IA el margen medio de los activos en un mes y compruébalo con un filtro: si se parece al margen medio de todos los clientes de la cohorte, ha incluido a los que se fueron.

*Plantilla 13.1. Tu LTV con churn*

| Dato | Valor o supuesto | De dónde sale |
| ------ | ------ | ------ |
| Ingreso mensual por cliente | | |
| Margen | | |
| Churn mensual | | |
| LTV = (ingreso × margen) / churn | | |
| Coste de captar un cliente | | |
| LTV / coste de captación | | |

*Plantilla 13.2. Tu LTV esperado por canal*

| Canal | Clientes | Activos en el mes 6 | Margen si activo, mes 6 | LTV esperado | CAC | LTV/CAC |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

*Plantilla 13.3. Tu ROI recalculado*

| Canal | Coste completo | Clientes × LTV esperado | ROI 1.ª compra | ROI con LTV | ¿Cambia el ganador? |
| ------ | ------ | ------ | ------ | ------ | ------ |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Plantilla 13.4. Tus pujas por valor*

| Campo | Google Ads | Meta Ads |
| ------ | ------ | ------ |
| Conversión que optimizas | | |
| Valor que envías (y cómo se calcula) | | |
| Cómo llega (etiqueta, importación, API) | | |
| Conversiones al mes | | |
| Valores distintos de cero | | |
| Estrategia de puja | | |
| Fecha de inicio y de primera revisión | | |

## Errores frecuentes

- Contar el riesgo dos veces: margen medio de todos × probabilidad de seguir.
- Usar ingresos en lugar de margen.
- LTV sin horizonte. «El valor de vida» sin plazo no se puede comparar.
- Prolongar la curva sin decirlo.
- Pasar a pujas por valor con pocas conversiones al mes, o cambiar la estrategia antes de que termine el aprendizaje.
- Enviar a Google Ads el mismo valor para todas las compras: no hay nada que optimizar.

## Antes de seguir

- [ ] Tienes el LTV con churn y el LTV esperado por canal.
- [ ] El margen del LTV esperado es el de los clientes que siguen activos.
- [ ] Tienes el LTV/CAC y el ROI con LTV de cada canal.
- [ ] Sabes si el ganador de la sesión 1 cambia.
- [ ] Sabes qué valor enviarías a Google Ads y Meta, y si cumples sus requisitos.
