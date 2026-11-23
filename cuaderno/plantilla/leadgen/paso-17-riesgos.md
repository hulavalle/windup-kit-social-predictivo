# Paso 17. Ficha de riesgos

**Qué te llevas.** La ficha de riesgos de tu modelo y de tus datos (sesgo, incertidumbre, datos que faltan sin cookies, datos personales), el registro del consentimiento que necesita cada uso, cómo explicas al cliente lo que haces con sus datos y el calendario de revisión del modelo.

## Para qué sirve

Un modelo aprende del pasado, y sus decisiones cambian los datos del futuro. Si el comercial solo llama a los leads con puntuación alta, los de puntuación baja nunca cierran, y el modelo aprende que tenía razón aunque no la tuviera. Para evitarlo se mantiene un grupo de control: una parte de los leads de puntuación baja también recibe llamada, al azar.

Un modelo da probabilidades, no certezas. Del grupo de más riesgo no se va todo el mundo. Se decide por segmentos, no por persona, y se dan rangos.

Sin cookies faltan datos. Hay quien rechaza el consentimiento, navegadores que limitan las cookies y bloqueadores. En el caso, GA4 pierde cerca del 8 % de las conversiones. La base fiable es el dato propio con consentimiento: el CRM.

En B2B también hay datos personales. El nombre de la persona de contacto, su email profesional y su teléfono son datos personales. A ningún asistente de IA se le suben nombres, emails ni teléfonos.

Y hay que poder explicar lo que haces. Si una puntuación decide a quién se llama y a quién no, el cliente tiene derecho a saber que se usan sus datos para eso. Cuando una decisión automática tiene efectos importantes sobre una persona, la normativa de protección de datos pide garantías, como que pueda pedir que la revise una persona.

## Cómo se hace

1. Para cada riesgo (sesgo, incertidumbre, datos que faltan, datos personales), escribe cómo aparece en tu proyecto y una mitigación concreta.
2. Para cada uso de los datos (análisis, flujos de email, Customer Match, audiencias similares), escribe qué consentimiento necesita y dónde queda registrado.
3. Revisa tu política de privacidad: tiene que decir que usas los datos para priorizar contactos y para publicidad, si lo haces.
4. Escribe el calendario de revisión del modelo: cada cuánto comparas lo predicho con lo real y qué haces si se desvía.
5. Escribe quién es el responsable de cada mitigación.

### Con tu asistente de IA

Pega tu plan de activación (paso 15) y pide: «Hazme de abogado del diablo. ¿Qué sesgos puede crear este plan? ¿Qué datos personales toca? ¿Qué consentimiento necesita cada audiencia?». Usa la respuesta como lista para revisar con quien lleve la protección de datos de tu cliente, no como asesoría legal.

### Cómo comprobarlo

Elige una audiencia y una persona de la lista. Busca en el CRM cuándo y cómo dio su consentimiento. Si no lo encuentras, esa lista no se sube.

## Ejemplo con Fandango para cafeterías

*Ejemplo 17.1. Riesgos de cafeterías*

| Riesgo | En Fandango para cafeterías | Mitigación |
| --- | --- | --- |
| Sesgo | Si el comercial solo llama a los leads de LinkedIn, los de Instagram nunca cierran y el modelo lo confirma | Llamar cada semana a una parte de los leads de puntuación baja, al azar, y revisar las señales cada trimestre |
| Incertidumbre | Las tasas de Directo salen de 35 leads y la retención del mes 6, de 4 cuentas | Dar siempre el número de casos junto a la tasa; no decidir con menos de unas decenas |
| Sin cookies | GA4 pierde cerca del 8 % de las conversiones y algunos leads llegan sin UTM | Contar los leads en el CRM y preguntar «¿Cómo nos has conocido?» |
| Datos personales en la IA | El CRM guarda nombre, email y teléfono de la persona de contacto | Exportar con identificadores seudónimos y sin notas del comercial |

*Ejemplo 17.2. Consentimiento por uso*

| Uso | Qué consentimiento necesita | Dónde queda registrado |
| --- | --- | --- |
| Llamar al lead que pidió información | La solicitud del formulario | CRM, fecha del lead |
| Email de reenganche a una cuenta cliente | Relación comercial y posibilidad de darse de baja en cada email | CRM |
| Customer Match y listas de Meta y LinkedIn | Aceptación del uso publicitario, con señales de consentimiento en el EEE | Campo `consentimiento_publicidad` con fecha |
| Análisis con IA | Ninguno extra si los datos van seudonimizados | Regla del paso 8 |

*Ejemplo 17.3. Revisión del modelo*

| Qué | Cada cuánto | Qué se mira | Qué se hace si se desvía |
| --- | --- | --- | --- |
| Regla del pedido decreciente | Trimestral | Qué % de cuentas con la señal dejó de pedir, frente al 40 % de partida | Ajustar el 80 % del umbral |
| Puntuación de leads | Trimestral | Tasa de cierre real por decil | Volver a entrenar con los leads nuevos |
| Valor del lead | Trimestral | Tasa de cierre y pedido medio | Nueva versión en el paso 5 |

## Tu proyecto

*Plantilla 17.1. Tus riesgos*

| Riesgo | En tu proyecto | Mitigación | Responsable |
| --- | --- | --- | --- |
| Sesgo | | | |
| Incertidumbre | | | |
| Sin cookies | | | |
| Datos personales | | | |

*Plantilla 17.2. Consentimiento por uso*

| Uso | Qué consentimiento necesita | Dónde queda registrado |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

*Plantilla 17.3. Transparencia con el cliente*

| Pregunta | Tu respuesta |
| --- | --- |
| ¿La política de privacidad dice que priorizas contactos con sus datos? | |
| ¿Dice que usas sus datos para publicidad? | |
| ¿Puede pedir que una persona revise una decisión? | |
| ¿Puede darse de baja de cada flujo? | |
| ¿Quién lleva la protección de datos? | |

*Plantilla 17.4. Revisión del modelo*

| Qué | Cada cuánto | Qué se mira | Qué se hace si se desvía |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

## Errores frecuentes

- Creer que en B2B no hay datos personales. El email de una persona en su empresa lo es.
- Subir listas de clientes a las plataformas sin comprobar el consentimiento de cada uno.
- Dejar que el modelo decida solo. Revisa sus resultados y mantén un grupo de control.
- Dar una probabilidad como si fuera una certeza. «Riesgo alto» no es «se va».
- No revisar nunca el modelo. Los precios, el mercado y el equipo cambian.

## Antes de seguir

- [ ] Cada riesgo tiene una mitigación y un responsable.
- [ ] Cada uso de los datos tiene su consentimiento y su registro.
- [ ] La política de privacidad cubre lo que haces.
- [ ] El modelo tiene fecha de revisión.
- [ ] Ningún export que llega a la IA lleva nombres, emails ni teléfonos.
