# Paso 13. LTV

**Qué te llevas.** El LTV de la cuenta por canal con sus tres fórmulas, el ROI de la sesión 1 recalculado con el LTV, el LTV/CAC de cada canal y el valor que enviarás a Google Ads o a Meta para las pujas por valor.

## Para qué sirve

El LTV es el margen que deja un cliente mientras sigue. En un negocio con pedido recurrente, el primer pedido es una parte pequeña del valor. Si juzgas las redes por la primera conversión, premias a la que trae clientes que piden una vez y se van.

Hay tres formas de calcularlo, de menos a más fina:

- **Histórico.** Ingreso medio × vida media. Fácil, pero solo vale si los clientes ya han completado su vida.
- **Con churn.** (Ingreso mensual × margen) / churn mensual. Supone que el churn es constante.
- **Esperado.** La suma, mes a mes, de la probabilidad de seguir activo × el margen si sigue activo. Usa la curva de retención de la cohorte (paso 11).

En el esperado, el margen tiene que ser el de los clientes que siguen activos. Si usas el margen medio de todos, incluidos los que no pidieron, cuentas el riesgo dos veces.

Con el LTV puedes comparar lo que vale un cliente con lo que cuesta captarlo: el LTV/CAC. Y puedes decirle a Google Ads o a Meta cuánto vale cada conversión, para que pujen más por los leads que valen más.

## Cómo se hace

1. Elige el horizonte: 24 meses es razonable para pedidos mensuales.
2. Para cada canal, toma la curva de retención: qué porcentaje de cuentas sigue activo en cada mes desde el primer pedido.
3. Para cada mes, calcula el margen medio de las cuentas activas.
4. Multiplica probabilidad × margen mes a mes y suma. Para los meses que aún no has visto, prolonga la caída media de los últimos meses observados y dilo.
5. Recalcula el ROI: (clientes × LTV esperado − coste completo) / coste completo.
6. Calcula el LTV/CAC: LTV / coste por cliente.
7. Decide el valor que enviarás a las plataformas.

### Del LTV a las pujas por valor

Las pujas por valor de Google Ads (maximizar el valor de conversión o ROAS objetivo) y la optimización por valor de Meta necesitan un valor en cada conversión. Ese valor puede ser el valor del lead, la puntuación de leads convertida en euros o el valor de vida previsto.

- Si optimizas con el lead: valor = probabilidad de cierre (paso 12) × LTV esperado del canal o del tipo de cliente.
- Si optimizas con el cliente: envía la conversión desde el CRM (importación de conversiones sin conexión en Google Ads) con el LTV esperado como valor.
- Elige una etapa con volumen y poco retraso: Google Ads recomienda al menos 15 conversiones al mes y valores distintos entre sí. Si captas pocos clientes al mes, optimiza con el lead o con el lead cualificado.
- Evita las conversiones con valor 0 y mantén los valores al menos cuatro semanas antes de cambiar la estrategia.
- En LinkedIn Ads, comprueba en su ayuda si tu tipo de campaña admite optimizar por valor.

### Con tu asistente de IA

Usa el prompt de `prompts/s2-b3-ltv.md` con tus pedidos y tus costes. Pide la curva por canal, el margen si activo de cada mes, el LTV esperado y el ROI recalculado, con la fórmula y el supuesto de los meses no observados. Pregunta: «¿He contado el riesgo dos veces?».

### Cómo comprobarlo

Comprueba un canal a mano: toma la probabilidad de seguir activo y el margen si activo del mes 6 y multiplícalos. Tiene que dar la contribución de ese mes al LTV.

## Ejemplo con Fandango para cafeterías

*Ejemplo 13.1. LTV esperado de la cuenta, a 24 meses*

| Red | Cuentas | Siguen activas en el mes 6 | Margen si activa, mes 6 | LTV observado (meses 0 a 11) | LTV esperado a 24 meses |
| --- | --- | --- | --- | --- | --- |
| Instagram | 18 | 27 % | 80,06 € | 315 € | 315 € |
| LinkedIn | 81 | 75 % | 130,27 € | 1.316 € | 2.488 € |
| Google y directo | 23 | 58 % | 119,30 € | 940 € | 1.180 € |

Los meses 0 a 11 son observados. Del 12 en adelante se prolonga la caída media de los meses 6 a 11. En Instagram, el esperado coincide con el observado: después del primer año ya no queda casi nadie.

*Ejemplo 13.2. El ROI de la sesión 1, recalculado*

| Red | ROI 1.ª conversión | Valor con LTV | ROI con LTV | LTV/CAC |
| --- | --- | --- | --- | --- |
| Instagram | +473 % | 5.044 € | +282 % | 3,8 |
| LinkedIn | −43 % | 191.595 € | +3.575 % | 36,7 |

Con la primera conversión, LinkedIn perdía dinero. Con el LTV, es de lejos la red más rentable. El canal barato era el caro.

*Ejemplo 13.3. El valor para las pujas*

| Campo | Fandango para cafeterías |
| --- | --- |
| Etapa con la que se optimiza | Lead (`generate_lead`): se captan pocos clientes al mes para optimizar con el cliente |
| Valor de la conversión | Tasa de cierre de la red × LTV esperado de la red: fórmula, se calcula con tus datos |
| Mejora cuando haya puntuación de leads | Puntuación del lead × LTV esperado de su tipo de cuenta |
| Plataformas | Google Ads para búsqueda; en LinkedIn Ads, comprobar si admite valor |

## Tu proyecto

*Plantilla 13.1. Tus tres LTV*

| Fórmula | Datos | De dónde sale | Resultado |
| --- | --- | --- | --- |
| Histórico: ingreso medio × vida media | | | |
| Con churn: (ingreso mensual × margen) / churn mensual | | | |
| Esperado: Σ P(activo en el mes k) × margen si activo | | | |

*Plantilla 13.2. LTV esperado por canal*

| Canal | Clientes | P(activo) mes 6 | Margen si activo, mes 6 | LTV esperado | Horizonte |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Plantilla 13.3. ROI con LTV y LTV/CAC*

| Canal | Coste completo | Clientes | CAC | ROI 1.ª conversión | ROI con LTV | LTV/CAC |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |
| | | | | | | |
| | | | | | | |

*Plantilla 13.4. Tu valor para las pujas*

| Campo | Tu proyecto |
| --- | --- |
| Etapa con la que optimizas | |
| Conversiones al mes en esa etapa | |
| Valor de la conversión (fórmula) | |
| Cómo llega el valor a la plataforma (etiqueta o importación) | |
| Plataformas | |
| Fecha de revisión del valor | |

## Errores frecuentes

- Usar el ingreso en lugar del margen.
- Contar el riesgo dos veces: multiplicar la probabilidad de seguir por un margen medio que ya incluye a los que no pidieron.
- Prolongar la curva sin decirlo. Los meses no observados son un supuesto, y va en el informe.
- Pujar por valor con muy pocas conversiones. El algoritmo no aprende; sube a una etapa con más volumen.
- Enviar a las plataformas un valor fijo para todos. Si todos valen lo mismo, la puja por valor no aporta nada.

## Antes de seguir

- [ ] El LTV usa margen, no ingreso.
- [ ] El margen es el de los clientes que siguen activos.
- [ ] Los meses no observados tienen su supuesto escrito.
- [ ] Tienes el ROI con LTV y el LTV/CAC por canal.
- [ ] La etapa con la que optimizas tiene volumen suficiente.
