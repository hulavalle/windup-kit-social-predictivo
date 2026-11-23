# Paso 10. Escalera de preguntas

**Qué te llevas.** Una pregunta por peldaño (descriptivo, diagnóstico, predictivo y prescriptivo) con la decisión que permite tomar, los datos que necesita cada una, el histórico mínimo y si tu proyecto puede responderla hoy.

## Para qué sirve

Descriptivo: qué pasó. Diagnóstico: por qué pasó. Predictivo: qué va a pasar. Prescriptivo: qué hacer. Cada peldaño pide más datos y más histórico que el anterior, y da una decisión más útil.

La sesión 1 se quedó en los dos primeros peldaños: cuántos leads trajo cada red y por qué unas cierran más que otras. La sesión 2 sube a los dos últimos: qué cuentas van a dejar de pedir, qué leads van a cerrar y a quién llamar primero.

Subir de peldaño sin datos suficientes es peligroso. Un modelo predictivo con pocos casos da cifras con aspecto de precisión que no lo son. Antes de pedir una predicción, comprueba que tienes el histórico y el volumen que necesita. Como referencia, el análisis predictivo pide al menos un año de datos fiables, y un modelo necesita bastantes casos del suceso que predice: si solo dejan de pedir tres cuentas al mes, un modelo estadístico tiene muy poco de dónde aprender.

## Cómo se hace

1. Escribe una pregunta por peldaño sobre el mismo problema de tu negocio.
2. Para cada una, escribe la decisión que permite tomar. Si el peldaño descriptivo no lleva a ninguna, está bien: solo informa.
3. Escribe los datos que necesita: tabla, columnas y fuente.
4. Escribe el histórico mínimo: cuántos meses y cuántos casos del suceso.
5. Marca si tu proyecto puede responderla hoy. Si no, qué tendrías que empezar a guardar.

### Con tu asistente de IA

Pega tu escalera y tu diccionario de datos y pide: «Para cada pregunta, dime qué columnas necesitaría y si con estos datos se puede responder. Si no se puede, dime qué falta». Comprueba que no te propone usar columnas que solo se conocen después del suceso, como la fecha en que se perdió un lead.

### Cómo comprobarlo

Cuenta los casos del suceso que quieres predecir: cuentas que dejaron de pedir, leads que cerraron. Si son unas pocas decenas, el peldaño predictivo será una regla sencilla, no un modelo.

## Ejemplo con Fandango para cafeterías

*Ejemplo 10.1. La escalera de cafeterías*

| Peldaño | Pregunta | Decisión |
| --- | --- | --- |
| Descriptivo | ¿Cuántas cafeterías dejaron de pedir el mes pasado? | Ninguna: solo informa |
| Diagnóstico | ¿Por qué se pierden tantos leads de Instagram? | Cambiar el mensaje o el formulario de Instagram |
| Predictivo | ¿Qué cafeterías van a dejar de pedir? ¿Qué leads van a cerrar? | A quién llama el comercial esta semana |
| Prescriptivo | ¿Qué acción evita que dejen de pedir las cuentas de más valor? | Qué hacer y cómo comprobar que funciona |

*Ejemplo 10.2. Datos e histórico que pide cada peldaño*

| Peldaño | Datos | Histórico mínimo | ¿Se puede hoy? |
| --- | --- | --- | --- |
| Descriptivo | `cuentas_b2b.csv`: pedidos por cuenta y mes | Un mes cerrado | Sí |
| Diagnóstico | `leads.csv`: red, estado y motivo de pérdida | Varios meses de leads resueltos | Sí: 113 leads de Instagram perdidos porque no eran una cafetería |
| Predictivo, cuentas | Pedidos de cada cuenta, con su tamaño | Un año, por la temporada de agosto | Con una regla: pocas cuentas dejan de pedir, 3,3 al mes |
| Predictivo, leads | Lo que se sabe al llegar el lead: red, contenido, número de locales | Leads resueltos de un año | Sí, con cuidado: 782 leads de junio de 2025 a octubre de 2026 |
| Prescriptivo | La acción, quién la recibió y un grupo de control | Varios ciclos de la acción | No: con 8 cuentas en riesgo no hay test posible |

## Tu proyecto

*Plantilla 10.1. Tu escalera*

| Peldaño | Pregunta | Decisión |
| --- | --- | --- |
| Descriptivo | | |
| Diagnóstico | | |
| Predictivo | | |
| Prescriptivo | | |

*Plantilla 10.2. Datos e histórico de cada peldaño*

| Peldaño | Datos (tabla y columnas) | Histórico mínimo | Casos del suceso | ¿Se puede hoy? |
| --- | --- | --- | --- | --- |
| Descriptivo | | | | |
| Diagnóstico | | | | |
| Predictivo | | | | |
| Prescriptivo | | | | |

*Plantilla 10.3. Qué empiezas a guardar hoy*

| Dato | Dónde se guardará | Desde cuándo | Responsable |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

## Errores frecuentes

- Saltar al predictivo sin el diagnóstico. Si no sabes por qué se pierden los leads, la predicción no te dirá qué hacer.
- Pedir un modelo con un puñado de casos. Con pocas bajas, una regla clara y revisada vale más.
- Olvidar la temporada. Si tu negocio baja en verano, necesitas al menos un año para no confundir el verano con una caída.
- Guardar solo el estado actual del lead. Sin el historial de fechas no hay predicción posible.

## Antes de seguir

- [ ] Cada peldaño tiene pregunta y decisión.
- [ ] Cada pregunta dice qué datos y cuánto histórico necesita.
- [ ] Sabes cuántos casos del suceso tienes.
- [ ] Lo que no puedes responder hoy tiene un plan para empezar a guardarlo.
