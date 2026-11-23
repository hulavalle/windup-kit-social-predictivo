# Paso 15. Plan de activación

**Qué te llevas.** La matriz riesgo × valor de tus clientes con una acción de CRM y una de paid media por cuadrante, los campos que añades al CRM, los flujos de cada segmento y la configuración de las audiencias.

## Por qué importa

Una predicción que se queda en una hoja de cálculo no cambia nada. Para que sirva, el riesgo y el valor de cada cliente tienen que llegar a donde se actúa: la herramienta de email o CRM y las plataformas de anuncios.

La **matriz riesgo × valor** cruza las dos predicciones: el riesgo de baja del paso 12 y el valor del paso 13. Cada cuadrante tiene su acción:

- **Valor alto, riesgo alto**: contacto personal. Es donde más se pierde si se van.
- **Valor bajo, riesgo alto**: email automático de reenganche. Barato y a escala.
- **Valor alto, riesgo bajo**: pedir una recomendación o proponer subir de plan.
- **Valor bajo, riesgo bajo**: nada. No gastes en quien no lo necesita.

En el **CRM**, la puntuación va como campo del contacto y cada cuadrante tiene su flujo. El reenganche funciona antes del hueco: si un cliente suele comprar cada 30 días, el email va antes del día 30, no después.

En **paid media** hay cuatro piezas:

- **Audiencias predictivas de GA4.** GA4 crea audiencias como «usuarios con probable abandono en 7 días» o «probables compradores en 7 días» y las comparte solas con Google Ads si las cuentas están vinculadas. Exigen que la propiedad cumpla el requisito de 1.000 usuarios que cumplen la condición y 1.000 que no. Si deja de cumplirlo, la audiencia deja de crecer.
- **Customer Match.** Subes a Google Ads una lista de clientes (emails o teléfonos, que se cifran al subir) para incluirlos o excluirlos de campañas. Solo entran los que dieron su consentimiento para publicidad, y con usuarios del Espacio Económico Europeo hay que enviar las señales de consentimiento. Cada miembro caduca a los 540 días, y una lista solo sigue activa si añades o actualizas al menos 100 miembros en ese plazo.
- **Pujas por valor** con el LTV como valor de conversión (paso 13).
- **Exclusión de los clientes fieles** de las campañas de captación. Pagar por traer a quien ya compra cada mes es tirar el presupuesto.

En Meta, las audiencias personalizadas a partir de una lista de clientes funcionan de forma parecida, y una audiencia similar parte de al menos 100 personas. Si añades una columna de valor, Meta busca personas parecidas a tus clientes de más valor.

## Ejemplo con Café Fandango

*Ejemplo 15.1. La matriz de la tienda*

| Cuadrante | Umbral | Suscriptores | CRM | Paid media |
| ------ | ------ | ------ | ------ | ------ |
| Valor alto, riesgo alto | Riesgo ≥ 13,6 % y valor ≥ 108,69 € | 5 | Llamada o email personal | Excluir de captación |
| Valor bajo, riesgo alto | Riesgo ≥ 13,6 % y valor < 108,69 € | 34 | Email automático de reenganche | Ninguna |
| Valor alto, riesgo bajo | Riesgo < 13,6 % y valor ≥ 108,69 € | 298 | Pedir recomendación o subir de plan | Audiencia similar por valor; excluir de captación |
| Valor bajo, riesgo bajo | Riesgo < 13,6 % y valor < 108,69 € | 235 | Nada | Ninguna |

Se puntuaron los 572 suscriptores activos el 21 de noviembre que se dieron de alta antes de noviembre, con su riesgo de baja en noviembre. El umbral de riesgo alto es el del decil de más riesgo en la validación (el riesgo medio es del 5,6 %). El valor es el margen esperado de los próximos 12 meses si sigue activo, sin descontar el riesgo para no contarlo dos veces, y el umbral es la mediana. En total, 39 suscriptores con riesgo alto.

Café Fandango no llega a los 1.000 usuarios que piden las audiencias predictivas de GA4. Por eso trabaja con sus propias puntuaciones y con listas de clientes.

*Ejemplo 15.2. Campos que añade a su herramienta de email*

| Campo | Tipo | Valores | De dónde sale | Cada cuánto se actualiza |
| ------ | ------ | ------ | ------ | ------ |
| `riesgo_baja` | Número | Probabilidad de baja el mes que viene | Modelo del paso 12 | Al empezar cada mes |
| `valor_12m` | Número | Margen esperado de los próximos 12 meses | Paso 13 | Al empezar cada mes |
| `segmento` | Lista | alto-alto, bajo-alto, alto-bajo, bajo-bajo | Cruce de los dos umbrales | Al empezar cada mes |
| `grupo_experimento` | Lista | contacto, control | Sorteo del paso 16 | Una vez, al entrar en el segmento |
| `fecha_puntuacion` | Fecha | Día del cálculo | Modelo | Al empezar cada mes |

## Tu proyecto

1. Fija los umbrales (plantilla 15.1). Riesgo alto: el umbral del decil de más riesgo de tu validación. Valor alto: la mediana del valor, o el corte que haga manejable el cuadrante de contacto personal.
2. Cuenta los clientes de cada cuadrante. Si el de valor alto y riesgo alto tiene más clientes de los que tu equipo puede llamar en un mes, sube el umbral.
3. Escribe una acción de CRM y una de paid media por cuadrante.
4. Crea los campos en tu herramienta de email o CRM (plantilla 15.2). Importa el CSV con el identificador del cliente. La correspondencia entre seudónimo y email se hace fuera de la IA, con tu tabla del paso 8.
5. Diseña un flujo por cuadrante (plantilla 15.3): qué lo dispara, qué mensajes y cuándo, cuándo sale el cliente del flujo y qué métrica lo mide.
6. Configura las audiencias (plantilla 15.4):
   - **GA4**: **Administrar** > **Audiencias** > **Nueva audiencia** > **Predictivas**. Si las plantillas salen como no disponibles, la propiedad no cumple los requisitos.
   - **Customer Match**: en Google Ads, **Herramientas** > **Gestor de audiencias** > segmentos de datos propios, o con Data Manager. Sube solo clientes con consentimiento.
   - **Exclusión**: añade la lista de clientes activos como exclusión en las campañas de captación.
   - **Meta**: audiencia personalizada desde la lista de clientes, y audiencia similar con columna de valor si tienes al menos 100 clientes en la lista.
7. Revisa el consentimiento de cada lista (plantilla 15.5). En WooCommerce, añade en el pago una casilla para recibir comunicaciones y publicidad personalizada, sin marcar por defecto, y guarda el valor en el pedido o en el cliente.
8. Antes de lanzar, define el grupo de control en el paso 16. Sin él, no sabrás si el plan funciona.

### Con tu asistente de IA

Adapta `prompts/s2-b5-activacion.md`:

```text
Te adjunto un CSV con una fila por cliente activo: identificador seudónimo,
probabilidad de baja el mes que viene y valor esperado de los próximos 12 meses
si sigue activo. No hay datos personales.
Con código:
1. Marca riesgo alto si la probabilidad es ≥ [umbral] y valor alto si el valor es ≥ [umbral].
2. Cuenta los clientes de cada cuadrante.
3. Devuélveme un CSV con id, segmento y una columna grupo_experimento con un 20 %
   de cada segmento de riesgo alto sorteado al azar como control (fija la semilla).
4. Propón un flujo de email por cuadrante con mensajes y plazos.
```

### Cómo comprobarlo

- Cuenta los clientes por segmento en tu herramienta de email después de importar: deben coincidir con el CSV.
- Comprueba en Google Ads el tamaño de la lista de Customer Match. Una lista pequeña puede no usarse en algunas redes hasta que crece.
- Mira una campaña de captación y comprueba que la lista de clientes aparece como exclusión.

*Plantilla 15.1. Tu matriz*

| Cuadrante | Umbral | Clientes | CRM | Paid media |
| ------ | ------ | ------ | ------ | ------ |
| Valor alto, riesgo alto | | | | |
| Valor bajo, riesgo alto | | | | |
| Valor alto, riesgo bajo | | | | |
| Valor bajo, riesgo bajo | | | | |

*Plantilla 15.2. Tus campos del CRM*

| Campo | Tipo | Valores | De dónde sale | Cada cuánto se actualiza |
| ------ | ------ | ------ | ------ | ------ |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 15.3. Tus flujos*

| Flujo | Entrada | Mensajes y plazos | Salida | Métrica |
| ------ | ------ | ------ | ------ | ------ |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 15.4. Tus audiencias*

| Audiencia | Plataforma | Definición | Origen (GA4, lista de clientes) | Uso (incluir, excluir, similar) | Requisito y si lo cumples |
| ------ | ------ | ------ | ------ | ------ | ------ |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

*Plantilla 15.5. El consentimiento de tus listas*

| Lista | Consentimiento necesario | Dónde se recoge | Cómo se actualiza |
| ------ | ------ | ------ | ------ |
| | | | |
| | | | |
| | | | |

## Errores frecuentes

- Subir a Customer Match todos los clientes, tengan o no consentimiento.
- Lanzar el plan a todo el segmento sin grupo de control.
- Ofrecer descuento a todos los de riesgo. Se acostumbran, y el margen se va.
- Un cuadrante de contacto personal con más clientes de los que se pueden atender.
- Puntuaciones que no se actualizan: el riesgo de hace tres meses no sirve.
- Seguir pagando por captar a clientes que ya compran cada mes.

## Antes de seguir

- [ ] Cada cuadrante tiene umbral, número de clientes y una acción de CRM y otra de paid media.
- [ ] Los campos están creados en tu herramienta de email o CRM y se actualizan cada mes.
- [ ] Cada flujo tiene entrada, plazos, salida y métrica.
- [ ] Sabes si tu propiedad de GA4 cumple los requisitos de las audiencias predictivas.
- [ ] Tus listas solo tienen clientes con consentimiento.
- [ ] Los clientes fieles están excluidos de las campañas de captación.
