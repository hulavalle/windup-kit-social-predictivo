# Paso 15. Plan de activación

**Qué te llevas.** Dos matrices con una acción por cuadrante (cuentas por riesgo y valor, leads por puntuación y valor), los campos que añades al CRM, el orden de llamada del comercial, los flujos automáticos y la configuración de las audiencias de paid media, con su consentimiento.

## Para qué sirve

Una predicción que se queda en una hoja de cálculo no cambia nada. Hay que llevarla a donde se trabaja: el CRM, donde el comercial decide a quién llama, y las plataformas de anuncios, donde se decide a quién se enseña cada campaña.

La matriz de riesgo y valor ordena el esfuerzo. Riesgo alto y valor alto: contacto personal. Riesgo alto y valor bajo: un mensaje automático. Riesgo bajo y valor alto: pedir una recomendación o proponer más. Riesgo bajo y valor bajo: nada. En captación de leads hay una segunda matriz, la de leads: puntuación de cierre por valor potencial. Decide en qué orden llama el comercial y qué leads reciben solo un email.

En el CRM, la puntuación va como campo del contacto o de la cuenta, y cada cuadrante tiene su flujo: una tarea para el comercial, un email automático, una lista.

En paid media hay cuatro piezas:

- **Customer Match** de Google Ads (y las listas de clientes de Meta y LinkedIn): subes tu lista de clientes, con su consentimiento, para excluirlos de las campañas de captación o para buscar empresas parecidas. En el Espacio Económico Europeo hay que enviar las señales de consentimiento.
- **Pujas por valor** con el valor del lead o del cliente del paso 13.
- **Audiencias similares por valor** en Meta, a partir de una lista de clientes con una columna de valor.
- **Audiencias predictivas de GA4**, que pasan solas a Google Ads. Piden que la propiedad sea apta para las métricas predictivas: al menos 1.000 usuarios que cumplen la condición y 1.000 que no en un periodo reciente. Un negocio B2B pequeño casi nunca llega.

## Cómo se hace

1. Pon cada cuenta activa en un cuadrante de riesgo (paso 12) y valor (paso 13). Fija el corte de cada eje: por ejemplo, la mediana del valor y el umbral del decil de más riesgo.
2. Escribe una acción de CRM y una de paid media por cuadrante.
3. Haz lo mismo con los leads nuevos: puntuación de cierre por valor potencial (tamaño del negocio).
4. Escribe el orden de llamada del comercial.
5. Añade los campos al CRM y escribe cada flujo: qué lo dispara, qué hace y quién lo recibe.
6. Configura las audiencias: fuente, criterio, uso (incluir o excluir), consentimiento y cada cuánto se actualiza.
7. Deja un grupo de control en cada flujo nuevo (paso 16).

### Con tu asistente de IA

Usa el prompt de `prompts/s2-b5-activacion.md`. Pide que asigne cada cuenta a un cuadrante con los cortes que tú le das y que cuente cuántas hay en cada uno. Después pide un borrador de cada flujo en pasos. El texto de los emails lo revisas tú: la IA no conoce el tono de tu cliente.

### Cómo comprobarlo

Suma las cuentas de los cuatro cuadrantes: tienen que dar el total de cuentas activas. Comprueba dos cuentas a mano: su riesgo, su valor y su cuadrante.

## Ejemplo con Fandango para cafeterías

*Ejemplo 15.1. Matriz de cuentas*

| Cuadrante | CRM | Paid media |
| --- | --- | --- |
| Valor alto, riesgo alto | Llamada del comercial esta semana | Excluir de las campañas de captación |
| Valor bajo, riesgo alto | Email automático con el pedido habitual y una prueba de un café nuevo | Ninguna |
| Valor alto, riesgo bajo | Pedir que recomienden a otra cafetería; proponer más locales | Lista para audiencia similar por valor |
| Valor bajo, riesgo bajo | Nada | Excluir de captación |

Riesgo alto = pedido por debajo del 80 % de su media (paso 12). Hoy son 8 cafeterías. Con tan pocas, el comercial las llama a todas; el email automático queda para cuando haya más.

*Ejemplo 15.2. Matriz de leads y orden de llamada*

| Cuadrante | Qué hace el comercial | Flujo automático |
| --- | --- | --- |
| Puntuación alta, varios locales | Llama primero | Ninguno |
| Puntuación alta, un local | Llama después | Ninguno |
| Puntuación baja, varios locales | Llama si queda tiempo en la semana | Email con tarifas y casos de cliente |
| Puntuación baja, un local | No llama | Email con tarifas y enlace para pedir la prueba |

El email con tarifas responde a los 88 leads de Instagram que se perdieron porque solo querían precios. Así no consumen una llamada.

*Ejemplo 15.3. Campos del CRM*

| Campo | Tipo | De dónde sale | Se actualiza |
| --- | --- | --- | --- |
| `puntuacion_lead` | Número de 0 a 100 | Modelo del paso 12 | Al llegar el lead |
| `tramo_lead` | Alta o baja | `puntuacion_lead` | Al llegar el lead |
| `riesgo_cuenta` | Alto o bajo | Regla del pedido decreciente | Cada semana |
| `valor_cuenta` | Euros | LTV esperado de su red | Cada trimestre |
| `grupo_control` | Sí o no | Sorteo al entrar en el flujo | Una vez |
| `consentimiento_publicidad` | Sí o no, con fecha | Formulario o contrato | Cuando cambia |
| `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` | Texto | Campos ocultos del formulario | Al llegar el lead |

*Ejemplo 15.4. Audiencias de paid media*

| Audiencia | Plataforma | Fuente | Uso | Consentimiento | Actualización |
| --- | --- | --- | --- | --- | --- |
| Cafeterías cliente | Google Ads (Customer Match) y LinkedIn | CRM, cuentas activas | Excluir de captación | Solo las que lo aceptaron | Mensual |
| Cafeterías de alto valor | Meta | CRM, con columna de valor | Origen de una audiencia similar por valor | Solo las que lo aceptaron | Trimestral |
| Probables compradores | GA4 a Google Ads | Audiencia predictiva | No se usa | | |

La audiencia predictiva no se usa: el carril de cafeterías está muy lejos de los 1.000 usuarios que piden las métricas predictivas de GA4.

## Tu proyecto

*Plantilla 15.1. Tu matriz de clientes*

| Cuadrante | Clientes | CRM | Paid media |
| --- | --- | --- | --- |
| Valor alto, riesgo alto | | | |
| Valor bajo, riesgo alto | | | |
| Valor alto, riesgo bajo | | | |
| Valor bajo, riesgo bajo | | | |

*Plantilla 15.2. Tu matriz de leads*

| Cuadrante | Qué hace el comercial | Flujo automático |
| --- | --- | --- |
| Puntuación alta, valor alto | | |
| Puntuación alta, valor bajo | | |
| Puntuación baja, valor alto | | |
| Puntuación baja, valor bajo | | |

*Plantilla 15.3. Tus campos del CRM*

| Campo | Tipo | De dónde sale | Se actualiza |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

*Plantilla 15.4. Tus flujos*

| Flujo | Qué lo dispara | Qué hace | Quién lo recibe | Grupo de control |
| --- | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |

*Plantilla 15.5. Tus audiencias*

| Audiencia | Plataforma | Fuente | Uso | Consentimiento | Actualización |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |

## Errores frecuentes

- Llamar a todos los de riesgo alto. Si el valor es bajo, un email cuesta menos que la llamada que intentas evitar.
- Subir listas sin consentimiento. Customer Match y las listas de Meta y LinkedIn exigen que el cliente haya aceptado el uso publicitario.
- Seguir pagando por captar a quien ya es cliente. Excluye a tus clientes de las campañas de captación.
- Contar con las audiencias predictivas de GA4 sin comprobar si tu propiedad es apta.
- Lanzar un flujo sin grupo de control. Sabrás que lo hiciste, no que funcionó.

## Antes de seguir

- [ ] Cada cuadrante tiene una acción de CRM y una de paid media, o «ninguna» a propósito.
- [ ] El comercial tiene un orden de llamada escrito.
- [ ] Cada campo nuevo del CRM dice de dónde sale y cuándo se actualiza.
- [ ] Cada audiencia dice qué consentimiento necesita.
- [ ] Cada flujo nuevo tiene un grupo de control o el motivo por el que no lo tiene.
