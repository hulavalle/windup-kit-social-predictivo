# Paso 7. Costes y ROI

**Qué te llevas.** El coste completo de tus redes, el ROI por red y por canal, el MER de la tienda, el diseño de una prueba de incrementalidad y el informe de ROI para la dirección.

## Por qué importa

Hay tres cifras que se confunden a menudo:

- **ROAS** = ingresos atribuidos / gasto en anuncios. No resta nada ni aplica el margen. Un ROAS de 2 puede perder dinero.
- **ROI** = (ingresos atribuidos × margen − coste completo) / coste completo. Es la que dice si ganas o pierdes.
- **MER** = ingresos totales de la tienda / gasto total en marketing. No atribuye nada a ningún canal. Sirve de control: si el ROI de cada red sube y el MER baja, algo está mal atribuido.

El **coste completo** incluye anuncios, influencers, herramientas y horas. Si tu tienda no invierte en anuncios, el coste son las horas dedicadas a redes valoradas en euros.

Y una advertencia que vale para todo el paso: **ROI atribuido no es ROI causado**. Que una venta llegue por un enlace de Instagram no prueba que sin Instagram no se habría hecho. Un caso típico: una tienda pausa una campaña en redes, las ventas caen y la reactiva convencida de que la campaña vendía. La causa era otra: una página de destino lenta. Para saber cuánto causa un canal hace falta un grupo que no lo vea. Es la incrementalidad.

## Ejemplo con Café Fandango

*Ejemplo 7.1. Coste completo mensual de la tienda*

| Concepto | Red | Cálculo | € al mes |
| ------ | ------ | ------ | ------ |
| Anuncios | Instagram | Facturas de Meta | 355 € |
| Anuncios | Facebook | Facturas de Meta | 200 € |
| Influencer | Instagram | Cuota de la creadora | 250 € |
| Horas | Instagram | Horas × 20 €/h | 156 € |
| Horas | TikTok | Horas × 20 €/h | 156 € |

*Ejemplo 7.2. ROI por primera compra, junio de 2025 a octubre de 2026*

| Red | Clientes | Ingresos 1.ª compra | Coste completo | CAC | ROAS | ROI |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Instagram | 1.213 | 23.729 € | 12.943 € | 10,67 € | 3,93 | −23 % |
| Facebook | 194 | 3.600 € | 3.401 € | 17,53 € | 1,06 | −54 % |
| TikTok | 1.007 | 11.960 € | 2.660 € | 2,64 € | Sin anuncios | +97 % |

Instagram tiene un ROAS de 3,93 y un ROI negativo. Por primera compra, gana TikTok.

*Ejemplo 7.3. ROI por canal de captación*

| Canal | Clientes | Margen 1.ª compra | Coste | ROI |
| ------ | ------ | ------ | ------ | ------ |
| Instagram orgánico | 560 | 4.750 € | 2.660 € | +79 % |
| Instagram influencer | 219 | 1.667 € | 4.250 € | −61 % |
| Instagram anuncios | 434 | 3.525 € | 6.033 € | −42 % |
| Facebook anuncios | 194 | 1.572 € | 3.401 € | −54 % |
| TikTok orgánico | 1.007 | 5.236 € | 2.660 € | +97 % |

Separar por canal cambia la lectura: el Instagram orgánico sí sale a cuenta; lo que hunde a Instagram son la influencer y los anuncios.

El MER de la tienda en el mismo periodo es de 6,98: 178.303 € de ingresos totales frente al gasto total en redes. Todas estas cifras miran solo la primera compra. El paso 13 las rehace con el valor de vida.

## Tu proyecto

1. Rellena el coste completo de un mes (plantilla 7.1). Las horas, a un precio por hora: el coste de empresa de quien lleva las redes o la tarifa de la agencia.
2. Junta los costes de todo el periodo que analizas desde `plan/costes.csv`.
3. Saca de WooCommerce los clientes nuevos y los ingresos de su primera compra por red. Con la atribución de pedidos activada, cada pedido trae su origen. Si no la tienes, usa las compras de GA4 por fuente y escribe que es una cifra por debajo de la real.
4. Calcula, por red y por canal, el CAC, el ROAS (solo si hay anuncios) y el ROI con el margen del paso 5 (plantilla 7.2).
5. Calcula el MER de cada mes (plantilla 7.3). Si el MER baja mientras el ROI de las redes sube, revisa la atribución.
6. Elige un canal con dudas y diseña una prueba de incrementalidad (plantilla 7.4). Tres formas, de más a menos fiable:
   - **Grupo de control de audiencia.** Una parte de la audiencia, al azar, no ve los anuncios. Meta Ads tiene estudios de conversión incremental para esto; revisa en su ayuda si tu cuenta tiene acceso.
   - **Prueba geográfica.** Apagas el canal en unas provincias y lo mantienes en otras parecidas, y comparas las ventas.
   - **Apagado con serie temporal.** Apagas el canal unas semanas y comparas con la tendencia de antes. Es la más débil: cualquier otro cambio se confunde con el efecto.
7. Prepara el informe para la dirección (plantilla 7.5). Una página, la decisión que pides arriba.

### Con tu asistente de IA

Usa el prompt de `prompts/s1-b5-roi.md` con tus archivos. La parte clave es esta:

```text
Te adjunto clientes.csv (un cliente por fila con su red de captación e importe de la
primera compra), costes.csv (mes, red, concepto, euros) y el diccionario de columnas.
No hay datos personales. Mi margen bruto es [margen] %.
Calcula con código, por red:
clientes, ingresos de la primera compra, coste completo (anuncios + influencer + horas),
CAC = coste / clientes, ROAS = ingresos / gasto solo en anuncios,
ROI = (ingresos × margen − coste completo) / coste completo.
Enséñame la fórmula de cada columna. Usa solo meses completos.
```

Si la IA te da un «ROI» de 3,93, te está dando el ROAS.

### Cómo comprobarlo

- Clientes de una red: filtra la red en tu hoja de clientes y cuenta filas.
- Coste de una red: tabla dinámica de la hoja de costes con la red en filas y la suma de euros.
- Rehaz un ROI a mano con esas dos cifras y el margen.

*Plantilla 7.1. Tu coste completo al mes*

| Concepto | Red | Cálculo | € al mes |
| ------ | ------ | ------ | ------ |
| Anuncios | | | |
| Influencers | | | |
| Horas en redes | | horas × €/hora | |
| Herramientas | | | |
| Producción | | | |
| Total | | | |

*Plantilla 7.2. Tu ROI por red o canal*

| Red o canal | Clientes | Ingresos 1.ª compra | Coste completo | CAC | ROAS | ROI |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

*Plantilla 7.3. Tu MER mensual*

| Mes | Ingresos totales de la tienda | Gasto total en marketing | MER |
| ------ | ------ | ------ | ------ |
| | | | |
| | | | |
| | | | |

*Plantilla 7.4. Tu prueba de incrementalidad*

| Campo | Tu proyecto |
| ------ | ------ |
| Canal o campaña | |
| Pregunta (¿cuántas ventas se pierden sin él?) | |
| Diseño (grupo de control, geográfica o apagado) | |
| Grupo de control | |
| Métrica | |
| Duración | |
| Decisión, escrita antes | |

*Plantilla 7.5. Tu informe de ROI para la dirección*

| Bloque | Qué dice | Cifra | Decisión que pides |
| ------ | ------ | ------ | ------ |
| Resumen | | | |
| ROI por red | | | |
| ROI por canal y contenido | | | |
| MER del periodo | | | |
| Qué no sabemos todavía | | | |

## Errores frecuentes

- Llamar ROI al ROAS.
- Dejar las horas fuera del coste. TikTok parecería gratis.
- Usar ingresos en lugar de margen.
- Mezclar meses completos con el mes en curso.
- Presentar el ROI atribuido como si fuera causado.
- Quedarse en la primera compra cuando vendes suscripción. Lo arreglas en el paso 13.

## Antes de seguir

- [ ] Tu coste completo incluye anuncios, influencers, herramientas y horas.
- [ ] El ROI usa el margen y el coste completo.
- [ ] Tienes el ROI por red y por canal.
- [ ] Tienes el MER de cada mes.
- [ ] Hay una prueba de incrementalidad diseñada para un canal.
- [ ] El informe para la dirección cabe en una página y pide una decisión.
