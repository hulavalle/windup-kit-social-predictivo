# Paso 7. Costes y ROI

**Qué te llevas.** El coste completo de cada red, el coste por lead, por cualificado y por cliente, el ROI con el valor del paso 5, el MER del carril, una propuesta para medir la incrementalidad y el informe de ROI para la dirección. Los costes los apuntas en `plan/costes.csv`.

## Para qué sirve

ROAS = ingresos atribuidos / gasto en anuncios. ROI = (ingresos atribuidos × margen − coste completo) / coste completo. El ROAS no resta lo que cuesta ni aplica el margen: un ROAS alto puede esconder pérdidas.

El coste completo incluye anuncios, influencers y horas. Una red sin anuncios cuesta las horas de quien la lleva. En captación de leads hay un coste más que suele olvidarse: el tiempo del comercial. Un lead que no encaja también se llama, se cualifica y se descarta.

El embudo da tres costes. El coste por lead dice cuánto cuesta un contacto. El coste por cualificado, cuánto cuesta uno que encaja. El coste por cliente, cuánto cuesta uno que paga. Ordenan las redes de forma distinta, y el que manda es el último.

El MER (ingresos totales / gasto total de marketing) no atribuye nada: mira el negocio entero. Sirve de control. Si el ROI de cada red sube y el MER baja, la atribución está contando dos veces.

Y un ROI atribuido no es un ROI causado. Que un lead llegue desde LinkedIn no demuestra que sin LinkedIn no habría llegado. Para saberlo hace falta un grupo que no vea la campaña.

## Cómo se hace

1. Suma el coste completo por red y mes: anuncios, influencers y horas × €/hora. Apúntalo en `plan/costes.csv`.
2. Cuenta por red los leads, los cualificados y los clientes del mismo periodo.
3. Calcula el coste por lead, por cualificado y por cliente.
4. Calcula el ROI dos veces: con el valor por primera conversión y con el valor del primer año (paso 5).
5. Calcula el MER del carril.
6. Elige cómo medirías la incrementalidad: pausar una campaña en una zona y compararla con otra, o apagar y encender por semanas y mirar la serie.
7. Escribe el informe para la dirección: respuesta, tabla, decisión y lo que no sabes.

### Con tu asistente de IA

Usa el prompt de `prompts/s1-b5-roi.md` con tu export de leads y tu archivo de costes. Pide la tabla por red con leads, cualificados, clientes, sus tasas, los tres costes y el ROI con la fórmula escrita. Exige que diga qué meses ha usado y que deje fuera el mes en curso.

### Cómo comprobarlo

Comprueba dos cifras con una tabla dinámica: los leads de una red y su coste total. Revisa que el «ROI» que te devuelve resta el coste y aplica el margen. Si no lo hace, es un ROAS.

## Ejemplo con Fandango para cafeterías

*Ejemplo 7.1. El embudo por red, de junio de 2025 a octubre de 2026*

| Red | Leads | Cualificados | Clientes | Tasa de cualificación | Tasa de cierre |
| --- | --- | --- | --- | --- | --- |
| Instagram | 462 | 141 | 16 | 31 % | 4 % |
| LinkedIn | 182 | 129 | 77 | 72 % | 47 % |
| Google | 103 | 58 | 16 | 60 % | 18 % |
| Directo | 35 | 22 | 6 | 65 % | 19 % |

*Ejemplo 7.2. Costes y ROI por red*

| Red | Coste | Coste por lead | Coste por cualificado | Coste por cliente | ROI 1.ª conversión | ROI con valor anual del lead |
| --- | --- | --- | --- | --- | --- | --- |
| Instagram | 1.320 € | 3 € | 9 € | 82 € | +473 % | +9.123 % |
| LinkedIn | 5.214 € | 29 € | 40 € | 68 € | −43 % | +820 % |

Google y Directo no tienen coste en redes. Instagram gana en coste por lead y en ROI por primera conversión. Pero LinkedIn es más barato por cliente: 68 € frente a 82 €. Y los dos ROI dan el mismo valor a todos los leads, aunque un lead de LinkedIn cierra mucho más. Es el error que destapa la sesión 2.

*Ejemplo 7.3. Por qué se pierden los leads de Instagram*

| Motivo de pérdida | Leads de Instagram | Leads de LinkedIn |
| --- | --- | --- |
| No es una cafetería | 113 | 4 |
| No responde | 94 | 27 |
| Solo quería precios | 88 | 14 |
| Precio | 36 | 16 |
| Ya tiene proveedor | 33 | 19 |

Cada uno de esos leads ha costado una llamada del comercial. Ese tiempo no está en el coste de la tabla 7.2.

*Ejemplo 7.4. El informe de ROI para la dirección*

| Parte | Fandango para cafeterías |
| --- | --- |
| Respuesta en una frase | Por cliente, LinkedIn es la red más barata; Instagram trae muchos leads que no encajan |
| Tabla | La 7.2, con coste por cliente en primer lugar |
| Decisión propuesta | Mantener LinkedIn Ads y cambiar el mensaje de Instagram para filtrar a quien no es una cafetería |
| Supuestos | Margen del 35 %, horas a 20 €/h, mismo valor del lead para todas las redes |
| Lo que no sabemos | Cuántas cafeterías habrían llegado sin anuncios, y cuánto vale un cliente según cuánto se quede (sesión 2) |
| MER del carril | Ingresos de cafeterías / gasto en redes de cafeterías: fórmula, se calcula con tus datos |

## Tu proyecto

*Plantilla 7.1. Tu coste completo al mes*

| Concepto | Cálculo | € al mes |
| --- | --- | --- |
| Horas en redes | horas × €/hora | |
| Anuncios | | |
| Influencers o colaboraciones | | |
| Herramientas | | |
| Horas del comercial con leads de redes | horas × €/hora | |
| Total | | |

*Plantilla 7.2. Tu embudo y tus costes por red*

| Red | Coste | Leads | Cualificados | Clientes | Coste por lead | Coste por cualificado | Coste por cliente |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

*Plantilla 7.3. Tu ROI por red*

| Red | Coste | Valor atribuido (paso 5) | ROI | ROAS (solo anuncios) |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 7.4. Tu prueba de incrementalidad*

| Campo | Tu proyecto |
| --- | --- |
| Campaña que pondrías a prueba | |
| Cómo crearías el grupo sin campaña (zona, semanas, audiencia) | |
| Métrica | |
| Duración | |
| Qué decidirías con cada resultado | |

*Plantilla 7.5. Tu informe de ROI para la dirección*

| Parte | Tu proyecto |
| --- | --- |
| Respuesta en una frase | |
| Tabla | |
| Decisión propuesta | |
| Supuestos | |
| Lo que no sabemos | |
| MER | |

## Errores frecuentes

- Llamar ROI al ROAS. Sin coste completo ni margen no es ROI.
- Comparar redes solo por coste por lead. La red más barata por lead puede ser la más cara por cliente.
- Contar el mes en curso. Los leads de las últimas semanas aún no han tenido tiempo de cerrar.
- Presentar el ROI atribuido como si fuera causal. Di siempre que es atribuido.

## Antes de seguir

- [ ] El coste de cada red incluye las horas valoradas en euros.
- [ ] Tienes los tres costes del embudo por red.
- [ ] El ROI resta el coste completo y aplica el margen.
- [ ] El informe dice qué no sabes.
- [ ] Tienes una propuesta para medir la incrementalidad, o el motivo por el que no se puede.
