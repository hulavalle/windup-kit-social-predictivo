# Paso 6. Pregunta y exploración en GA4

**Qué te llevas.** Tres exploraciones de GA4 para tu proyecto (forma libre, rutas y atribución), cada una con la pregunta que responde, comprobada contra el informe estándar, y la lista de lo que GA4 no puede responder porque vive en el CRM.

## Para qué sirve

Primero la pregunta, después GA4. Si abres GA4 sin pregunta, sales con gráficos y sin decisión.

GA4 tiene dos formas de mirar el canal. Adquisición de usuarios dice con qué canal llegó cada usuario la primera vez. Adquisición de tráfico dice el canal de cada sesión. En un negocio de leads, la primera visita suele venir de una red y el formulario se envía días después, desde Google o en directo. Las dos vistas cuentan historias distintas.

GA4 reparte el mérito de cada evento clave con dos modelos: atribución basada en datos o último clic. El último clic da todo el mérito al último canal y por eso infravalora las redes, que suelen estar al principio del recorrido.

En captación de leads, GA4 llega hasta el formulario. Lo que pasa después (cualificado, cliente, pedido) no lo ve, salvo que se lo mandes. GA4 tiene eventos recomendados para eso, como `qualify_lead` y `close_convert_lead`, que se pueden enviar desde el CRM. Si no los envías, esas preguntas se responden en el CRM.

## Cómo se hace

1. Escribe la pregunta y la decisión que tomarías con la respuesta.
2. Decide si la responde GA4 (hasta el lead) o el CRM (después del lead).
3. **Forma libre.** En **Explorar**, crea una exploración de forma libre. Filas: Fuente/medio de la sesión o Contenido manual de la sesión. Valores: Sesiones, Sesiones con interacción y el recuento de `generate_lead`.
4. **Rutas.** Crea una exploración de rutas. Pon `generate_lead` como punto final y mira hacia atrás qué páginas vieron antes. Responde qué contenido acerca al formulario.
5. **Atribución.** En **Publicidad**, abre **Rutas de conversión** con el evento clave `generate_lead`. Mira en qué posición aparecen las redes: al principio, en medio o al final. Compara después los dos modelos de atribución.
6. Comprueba la cifra de la exploración contra el informe estándar con el mismo filtro y las mismas fechas.
7. Apunta lo que GA4 no puede responder y en qué campo del CRM está.

### Con tu asistente de IA

Si exportas la exploración en CSV, adjúntala y pide: «Resume qué fuentes traen más `generate_lead` y qué contenidos tienen mejor proporción de leads por sesión. Calcula con código y dime qué filas tienen tan pocas sesiones que no conviene sacar conclusiones». También puedes pedirle que te diga, paso a paso, cómo montar una exploración concreta en GA4: compara su respuesta con la interfaz, porque los menús cambian.

### Cómo comprobarlo

El número de `generate_lead` de Instagram en tu exploración coincide con el de **Adquisición de tráfico** filtrado por la misma fuente y fechas. Si no coincide, revisa el filtro, el intervalo y si la exploración usa dimensiones de usuario o de sesión.

## Ejemplo con Fandango para cafeterías

*Ejemplo 6.1. Exploración de forma libre*

| Campo | Fandango para cafeterías |
| --- | --- |
| Pregunta | ¿Qué red y qué contenido traen leads de cafeterías? |
| Decisión | Qué piezas repetir en Instagram y LinkedIn |
| Técnica | Exploración de forma libre |
| Filas | Fuente/medio de la sesión y Contenido manual de la sesión |
| Valores | Sesiones, Sesiones con interacción, `generate_lead` |
| Filtro | Página de destino contiene `/empresas` |

*Ejemplo 6.2. Exploración de rutas*

| Campo | Fandango para cafeterías |
| --- | --- |
| Pregunta | ¿Qué páginas ven antes de enviar el formulario? |
| Decisión | Qué enlazar desde los reels y los posts |
| Técnica | Exploración de rutas, hacia atrás desde `generate_lead` |
| Punto final | Evento `generate_lead` |
| Nodos | Título de página y nombre del evento |

*Ejemplo 6.3. Atribución*

| Campo | Fandango para cafeterías |
| --- | --- |
| Pregunta | ¿Aparece LinkedIn al principio de recorridos que terminan en un lead desde Google? |
| Decisión | No recortar LinkedIn Ads solo por su último clic |
| Informe | **Publicidad** > **Rutas de conversión**, evento clave `generate_lead` |
| Comparación | Modelo basado en datos frente a último clic |

*Ejemplo 6.4. Lo que GA4 no responde*

| Pregunta | Por qué GA4 no la responde | Dónde está |
| --- | --- | --- |
| ¿Qué red trae cafeterías que piden? | GA4 no ve el primer pedido | `leads.csv`: `red` y `estado` |
| ¿Por qué se pierden los leads? | El motivo lo apunta el comercial | `leads.csv`: `motivo_perdida` |
| ¿Cuánto pide cada cuenta al mes? | Los pedidos no pasan por la web | `cuentas_b2b.csv` |

## Tu proyecto

*Plantilla 6.1. Tu exploración de forma libre*

| Campo | Tu proyecto |
| --- | --- |
| Pregunta | |
| Decisión | |
| Filas | |
| Valores | |
| Filtro | |
| Comprobada contra el informe estándar | |

*Plantilla 6.2. Tu exploración de rutas*

| Campo | Tu proyecto |
| --- | --- |
| Pregunta | |
| Decisión | |
| Punto de inicio o final | |
| Nodos | |
| Qué has visto | |

*Plantilla 6.3. Tu análisis de atribución*

| Campo | Tu proyecto |
| --- | --- |
| Pregunta | |
| Decisión | |
| Evento clave | |
| Posición de las redes en las rutas | |
| Diferencia entre modelos | |

*Plantilla 6.4. Lo que GA4 no responde*

| Pregunta | Por qué GA4 no la responde | Campo del CRM |
| --- | --- | --- |
| | | |
| | | |
| | | |

## Errores frecuentes

- Mezclar dimensiones de usuario y de sesión en la misma exploración. Primer canal del usuario y canal de la sesión no se suman.
- Sacar conclusiones de filas con pocas sesiones. Con diez sesiones, un lead más cambia la tasa por completo.
- Juzgar las redes solo por el último clic. Aparecen antes en el recorrido y el último clic se lo lleva otro.
- Pedir a GA4 lo que está en el CRM. GA4 no sabe quién ha comprado si no se lo envías.

## Antes de seguir

- [ ] Cada exploración tiene su pregunta y su decisión escritas antes.
- [ ] La cifra de la forma libre coincide con la del informe estándar.
- [ ] Has mirado la posición de las redes en las rutas de conversión.
- [ ] Sabes qué preguntas responde el CRM y no GA4.
- [ ] Has decidido si enviarás a GA4 los eventos de cualificado y cliente.
