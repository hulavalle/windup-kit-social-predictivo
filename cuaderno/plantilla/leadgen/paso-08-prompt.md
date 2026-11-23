# Paso 8. Tu prompt de 4 pasos

**Qué te llevas.** El prompt que usaste con sus dos cifras verificadas, la biblioteca de prompts de tu proyecto y las reglas de datos personales que sigue todo el equipo antes de subir nada a un asistente de IA.

## Para qué sirve

Analizar con IA en 4 pasos: pregunta, datos, prompt y verificación. La IA calcula en segundos; tú respondes de que la cifra es cierta. El método funciona igual en ChatGPT, Claude y Gemini.

1. **Pregunta.** La pregunta de negocio y la decisión que permite tomar, escritas antes de abrir los datos.
2. **Datos.** El CSV con su diccionario de columnas y sin datos personales.
3. **Prompt.** Rol, datos, pregunta, formato de salida, «calcula con código, no de memoria» y «enséñame la fórmula y los supuestos».
4. **Verificación.** Dos cifras comprobadas a mano y una pregunta a la IA sobre lo que no sabe.

Un prompt que funcionó es un activo. Si lo guardas con su pregunta, sus datos y su verificación, el mes que viene repites el análisis en cinco minutos y con los mismos criterios.

En captación de leads, el CRM está lleno de datos personales: nombre de la persona de contacto, email, teléfono, notas del comercial. Nada de eso hace falta para analizar. Antes de subir un export, se quita.

## Cómo se hace

1. Escribe la pregunta y la decisión.
2. Exporta del CRM solo las columnas que necesitas. Cambia los identificadores por códigos seudónimos (`LEAD-0001`, `CAF-0031`) y guarda la tabla de equivalencias fuera del asistente.
3. Escribe el diccionario de columnas: nombre, tipo y significado. Sin él, la IA adivina.
4. Escribe el prompt con las seis piezas: rol, datos, pregunta, formato, cálculo con código y supuestos.
5. Comprueba dos cifras a mano con una tabla dinámica.
6. Pregunta: «¿Qué supuestos has hecho? ¿Qué no puedes saber con estos datos?».
7. Guarda el prompt en la biblioteca con su fecha y lo que falló.

### Prompt de ejemplo

```text
Eres analista de datos de un negocio B2B que capta clientes con un formulario.
Te adjunto leads.csv, costes.csv y el diccionario de columnas.

Pregunta: ¿qué red tiene el menor coste por cliente? Quiero decidir dónde
invertir el presupuesto de anuncios del trimestre.

Reglas:
- Calcula con código, no de memoria, y enséñame el código.
- Usa los meses completos de junio de 2025 a octubre de 2026. El mes en curso, fuera.
- Para la tasa de cierre, usa solo leads ya resueltos y dime cuáles has dejado fuera.
- ROI = (valor atribuido × margen − coste completo) / coste completo. No me des ROAS.

Devuélveme una tabla por red con leads, cualificados, clientes, tasa de cualificación,
tasa de cierre, coste, coste por lead, coste por cualificado y coste por cliente.
Después, los supuestos que has hecho y lo que no puedes saber con estos datos.
```

### Cómo comprobarlo

Antes de calcular nada, pide a la IA que liste las columnas que ha leído y el número de filas de cada archivo. Si no coinciden con tu diccionario, para.

## Ejemplo con Fandango para cafeterías

*Ejemplo 8.1. El prompt de cafeterías*

| Paso | Qué hicimos |
| --- | --- |
| Pregunta | ¿Qué red tiene el menor coste por cliente? Decidir dónde invertir en anuncios y horas del comercial |
| Datos | `leads.csv`, `costes.csv` y `diccionario.md`, con identificadores seudónimos |
| Prompt | El del recuadro de arriba |
| Verificación | Leads de Instagram (462) y coste de LinkedIn (5.214 €) con una tabla dinámica |
| Qué vigilar | Que no llame ROI al ROAS, que deje fuera noviembre y que la tasa de cierre use leads resueltos |

*Ejemplo 8.2. Biblioteca de prompts de cafeterías*

| Nombre | Pregunta | Datos | Archivo | Última prueba |
| --- | --- | --- | --- | --- |
| ROI por red | ¿Qué red tiene el menor coste por cliente? | `leads.csv`, `costes.csv` | `prompts/s1-b5-roi.md` | Noviembre de 2026 |
| Cohortes de cuentas | ¿Qué red trae cuentas que siguen pidiendo? | `cuentas_b2b.csv` | `prompts/s2-b1-cohortes.md` | Noviembre de 2026 |
| Cuentas que dejan de pedir | ¿Qué cafeterías van a dejar de pedir? | `cuentas_b2b.csv` | `prompts/s2-b2-churn.md` | Noviembre de 2026 |
| LTV por red | ¿Cuánto vale una cuenta de cada red? | `cuentas_b2b.csv`, `costes.csv` | `prompts/s2-b3-ltv.md` | Noviembre de 2026 |

*Ejemplo 8.3. Reglas de datos personales*

| Regla | Cómo se cumple |
| --- | --- |
| Ni nombres, ni emails, ni teléfonos | Se borran del export antes de abrir el asistente |
| Identificadores seudónimos | `LEAD-0001`, `CAF-0031`; la tabla de equivalencias se queda en el CRM |
| Nada de texto libre | Las notas del comercial se quitan: pueden llevar nombres o teléfonos |
| El nombre del negocio también se quita | Una cafetería de un autónomo identifica a una persona |
| Cuenta del asistente | La de la empresa, con el entrenamiento con tus conversaciones desactivado si la herramienta lo permite |

## Tu proyecto

*Plantilla 8.1. Tu prompt*

| Paso | Qué hiciste |
| --- | --- |
| Pregunta | |
| Datos | |
| Prompt | |
| Verificación | |
| Qué falló la IA | |

*Plantilla 8.2. Tu biblioteca de prompts*

| Nombre | Pregunta | Datos | Archivo | Última prueba |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 8.3. Tus reglas de datos personales*

| Regla | Cómo se cumple | Quién lo comprueba |
| --- | --- | --- |
| | | |
| | | |
| | | |
| | | |

## Errores frecuentes

- Subir el export del CRM tal cual. Lleva nombres, emails y notas.
- No dar el diccionario. La IA interpreta `estado` o `fecha_cliente` a su manera.
- Aceptar la primera tabla. Comprueba dos cifras siempre, aunque el resultado te guste.
- Repetir el análisis cada mes con un prompt distinto. Las cifras dejan de ser comparables.

## Antes de seguir

- [ ] El prompt tiene las seis piezas.
- [ ] Has verificado dos cifras a mano.
- [ ] Has preguntado a la IA por sus supuestos.
- [ ] El export que subes no tiene datos personales ni texto libre.
- [ ] El prompt está guardado en la biblioteca con su fecha.

## Datos conectados (MCP)

Cuando tu proyecto tenga datos, la IA puede traerlos sin exportar: un conector MCP le da acceso a la herramienta. El prompt es el mismo; cambia solo el paso de los datos: di qué tiene que traer el conector y de qué periodo, y pide que te enseñe la tabla antes de calcular.

- Redes en orgánico: Metricool (casi todas las redes, también en el plan gratuito) o Buffer.
- Anuncios: los MCP oficiales de Meta Ads, TikTok Ads y Google Ads. Escriben: úsalos solo para leer.
- GA4: el MCP oficial de Google Analytics, de solo lectura.
- Histórico de clientes: BigQuery, tu tienda o tu CRM, en solo lectura o en una cuenta de prueba.

Antes de conectar nada, comprueba que tu asistente lo admite (Claude, en la web; ChatGPT, según el plan; Gemini, casi no) y sigue las ocho reglas de `mcp.md`: solo lectura, nada de datos personales y revisar cada llamada.
