# Paso 0. Tu modelo y tu pregunta sobre redes

**Qué te llevas.** La ficha de tu tienda con la pregunta sobre redes que hay que responder, el inventario de redes, el presupuesto mensual y quién decide con cada cifra.

## Por qué importa

Un informe de redes que nadie usa para decidir es un informe de vanidad. El de Café Fandango de octubre de 2026 decía +2.300 seguidores nuevos, un 4,1 % de engagement y 180.000 de alcance. Todo subía respecto a septiembre. La fundadora lo leyó y preguntó: «¿Y esto cuánto café vende?». Nadie supo responder.

La pregunta buena lleva a una decisión. «¿Cómo van las redes?» no lleva a ninguna. «¿Qué red trae clientes que compran y repiten?» decide cómo repartir el presupuesto del mes que viene. Si nadie haría nada distinto con la respuesta, cambia la pregunta.

Antes de medir nada necesitas tres cosas que el cuaderno de clase no pedía: en qué redes estás y para qué, cuánto te cuesta estar y quién toma cada decisión. Sin el inventario no sabrás qué enlaces etiquetar en el paso 3. Sin el presupuesto no hay ROI en el paso 7. Sin saber quién decide, el informe del paso 9 no llega a nadie.

## Ejemplo con Café Fandango

*Ejemplo 0.1. Ficha de la tienda*

| Campo | Café Fandango, tienda |
| ------ | ------ |
| Qué vende | Café en grano en compra suelta y suscripción mensual de 24 € (dos bolsas de 250 g) |
| Conversión en la web | `purchase`; la suscripción es un `purchase` con `item_category` = Suscripción |
| Margen bruto | Café suelto 45 %, suscripción 40 % |
| Pregunta sobre redes | ¿Qué red trae clientes que compran y repiten? |
| Decisión que permite tomar | Cómo repartir el presupuesto de redes del mes que viene |
| Problema de partida | El informe mensual solo trae seguidores, engagement y alcance |

*Ejemplo 0.2. Inventario de redes de la tienda*

| Red | Cuenta o formato | Uso | Quién la lleva | ¿Enlaces con UTM? |
| ------ | ------ | ------ | ------ | ------ |
| Instagram | Cuenta de la marca: reels, carruseles e imágenes | Orgánico | Community manager | Sí, salvo errores (paso 3) |
| Instagram | Publicaciones de una microinfluencer (`laura-cafe`) | Influencer, con cuota mensual | Fundadora y community manager | Sí, con `utm_content` = `laura-cafe` |
| Instagram y Facebook | Anuncios de Meta | Anuncios | Community manager | Sí, con macros de Meta |
| TikTok | Vídeos de la marca | Orgánico | Community manager | Sí |
| LinkedIn | Cuenta para cafeterías | Fuera de este carril: es la captación de leads | Comercial | Sí |

*Ejemplo 0.3. Presupuesto mensual medio de la tienda*

| Concepto | Red | € al mes | Fuente del dato |
| ------ | ------ | ------ | ------ |
| Anuncios | Instagram | 355 € | Facturas de Meta |
| Anuncios | Facebook | 200 € | Facturas de Meta |
| Influencer | Instagram | 250 € | Factura de la creadora |
| Horas de community | Instagram | 156 € | Registro de horas a 20 €/h |
| Horas de community | TikTok | 156 € | Registro de horas a 20 €/h |

Con las cafeterías, el coste medio en redes de Café Fandango es de 1.502 € al mes.

*Ejemplo 0.4. Quién decide*

| Decisión | Quién decide | Cada cuánto | Qué cifra necesita |
| ------ | ------ | ------ | ------ |
| Reparto del presupuesto de redes | Fundadora | Cada mes | ROI por red con el valor de vida del cliente |
| Qué contenidos se repiten | Community manager | Cada semana | Compras y altas por contenido |
| Si se renueva a la influencer | Fundadora | Cada trimestre | ROI del canal influencer |
| A quién se contacta para que no se dé de baja | Atención al cliente | Cada semana | Lista de suscriptores con riesgo alto |

## Tu proyecto

1. Rellena la ficha (plantilla 0.1). La pregunta sobre redes empieza por «¿Qué red…?», «¿Qué contenido…?» o «¿Cuánto…?» y termina en dinero o en clientes.
2. Escribe al lado la decisión. Si no hay decisión, tacha la pregunta y escribe otra.
3. Haz el inventario de redes (plantilla 0.2). Mira las cuentas de la marca, los perfiles que publican por ti (influencers, embajadores), los anuncios y los enlaces fijos, como la bio o los destacados.
4. Apunta el presupuesto de un mes normal (plantilla 0.3). Incluye las horas de quien lleva las redes, aunque sea alguien de la empresa: valóralas en euros por hora. Si no inviertes en anuncios, el coste son esas horas.
5. Escribe quién decide con cada cifra (plantilla 0.4). Pregúntalo: el que decide no siempre es el que pide el informe.
6. Copia los conceptos de coste a `plan/costes.csv`, una fila por mes, red y concepto.

### Con tu asistente de IA

Si tienes el informe de redes que se presenta hoy, pídele que lo critique. Así sale la pregunta que falta:

```text
Te adjunto el informe mensual de redes de mi tienda online. No tiene datos personales.
Para cada métrica, dime qué decisión de negocio permite tomar.
Después propón tres preguntas sobre redes que lleven a una decisión de presupuesto,
y para cada una di qué datos haría falta cruzar (plataforma, GA4, tienda).
No inventes cifras: si un dato no está en el informe, dilo.
```

Elige tú la pregunta. La IA propone; quien conoce el negocio eres tú.

*Plantilla 0.1. Ficha de tu tienda*

| Campo | Tu proyecto |
| ------ | ------ |
| Qué vendes (compra suelta, suscripción, packs) | |
| Conversión en la web (evento de GA4) | |
| Margen bruto por tipo de producto | |
| Tu pregunta sobre redes | |
| Decisión que permite tomar | |
| Problema de partida | |

*Plantilla 0.2. Tu inventario de redes*

| Red | Cuenta o formato | Uso (orgánico, anuncios, influencer) | Quién la lleva | ¿Enlaces con UTM? |
| ------ | ------ | ------ | ------ | ------ |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 0.3. Tu presupuesto mensual*

| Concepto | Red | € al mes | Fuente del dato |
| ------ | ------ | ------ | ------ |
| Anuncios | | | |
| Influencers | | | |
| Horas de redes (horas × €/hora) | | | |
| Herramientas (programación, diseño, enlaces) | | | |
| Producción (fotos, vídeo, producto regalado) | | | |
| Total | | | |

*Plantilla 0.4. Quién decide*

| Decisión | Quién decide | Cada cuánto | Qué cifra necesita |
| ------ | ------ | ------ | ------ |
| | | | |
| | | | |
| | | | |
| | | | |

## Errores frecuentes

- Una pregunta que ya responde la plataforma, como «¿qué post tuvo más alcance?». No cambia ningún presupuesto.
- Dejar fuera las horas. Una red «gratis» cuesta las horas de quien la lleva.
- Olvidar lo que publican otros por ti. La influencer es un canal con su propio coste y sus propios enlaces.
- Escribir «marketing» en quién decide. Pon una persona o un puesto.

## Antes de seguir

- [ ] Tu pregunta sobre redes termina en clientes o en dinero.
- [ ] Al lado de la pregunta hay una decisión.
- [ ] El inventario incluye cuentas propias, influencers, anuncios y enlaces fijos.
- [ ] El presupuesto incluye las horas valoradas en euros.
- [ ] Cada decisión tiene una persona o un puesto.
- [ ] Los costes están en `plan/costes.csv`.
