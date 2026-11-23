# Plantilla para proyectos de captación de leads

Máster Técnico en Marketing Digital & IA · Análisis de datos con IA y análisis predictivo · 2026

Si estuviste en clase, ya tienes el cuaderno rellenado; si no, empieza aquí por el paso 0. Esta plantilla repite los mismos 19 pasos en versión completa, para un negocio real que capta contactos y los convierte en clientes: servicios profesionales, B2B, clínicas, academias de formación. Sirve para aplicar el método fuera del máster, con tus datos. Si tu proyecto vende en la web, usa la plantilla de e-commerce.

El ejemplo de cada paso es Fandango para cafeterías, el carril B2B de Café Fandango. Una cafetería rellena el formulario de `/empresas.html` (evento `generate_lead`), el comercial la llama y le manda una prueba, y si le convence pasa a ser cliente con un pedido cada mes. Llega desde Instagram, LinkedIn, Google y tráfico directo. Las cifras salen de los datos del caso (carpeta `datos/` del kit): son sintéticas, pero todas cuadran entre sí.

La sesión 1 responde a «¿Y esto cuánto café vende?»: qué red trae leads, cuánto vale cada uno y qué devuelve cada euro. La sesión 2 responde a «Me entero cuando ya se han ido»: qué cuentas van a dejar de pedir, qué leads van a cerrar, cuánto vale cada cliente y cómo demostrar que lo que haces funciona.

*Plantilla A. Datos del proyecto*

| Campo | Tu respuesta |
| ---- | ------ |
| Proyecto | |
| Cliente o empresa | |
| Qué vende (servicio, producto B2B, tratamiento, curso) | |
| Equipo | |
| Responsable del dato | |
| CRM o herramienta donde viven los leads | |
| Asistente de IA que usáis (ChatGPT, Claude o Gemini) | |
| Fecha de entrega | |

## Cómo se usa

1. Sigue los pasos en orden. Cada uno usa lo que sale del anterior: el ROI necesita el valor del lead, el LTV necesita la cohorte y la activación necesita el riesgo y el valor.
2. Lee el ejemplo de Fandango para cafeterías antes de rellenar tu plantilla. Las plantillas tienen las mismas columnas que el ejemplo.
3. Si tu proyecto todavía no tiene datos, escribe la fórmula y de dónde saldrá cada dato. Rellena la cifra cuando la tengas.
4. Cada análisis trae un apartado «Con tu asistente de IA». Funciona igual en ChatGPT, Claude y Gemini. La IA calcula; tú compruebas dos cifras a mano antes de usar el resultado.
5. Pasa el control de «Antes de seguir» al final de cada paso. Si una casilla queda sin marcar, vuelve atrás.
6. Rellena las tablas de este documento. Si te falta espacio, añade filas en Word.

## Los pasos

| Paso | Qué te llevas | Cuándo se revisa |
| --- | --- | --- |
| 0. Tu modelo y tu pregunta sobre redes | Ficha del negocio, inventario de redes, presupuesto y quién decide | Al empezar |
| 1. Tu AARRR | La matriz de conversiones con su etapa AARRR y la etapa que priorizas | Trimestral |
| 2. La cadena de valor social | La cadena del post al pedido mensual, con fuentes, métricas adelantadas y retrasadas, y el informe mensual | Mensual |
| 3. Convención de UTMs de redes | Lista cerrada de valores, UTMs que llegan al CRM y auditoría mensual | Mensual |
| 4. Objetivos por campaña | OKR trimestrales con contrapesos y métricas adelantadas | Trimestral |
| 5. Valor de cada objetivo | Valor del lead, del cualificado y del cliente, con su tabla de versiones | Trimestral |
| 6. Pregunta y exploración en GA4 | Exploraciones de forma libre, de rutas y de atribución, comprobadas | Mensual |
| 7. Costes y ROI | Coste por lead, por cualificado y por cliente, ROI, MER, incrementalidad e informe para la dirección | Mensual |
| 8. Tu prompt de 4 pasos | Biblioteca de prompts del proyecto y reglas de datos personales | Cuando cambie un dato |
| 9. Checklist de la sesión 1 | Checklist del informe de ROI social | Mensual |
| 10. Escalera de preguntas | Las preguntas por peldaño, con los datos y el histórico que pide cada una | Semestral |
| 11. Cohorte y cliente activo | Cohortes de cuentas y de leads, retención bruta, neta y de ingresos | Mensual |
| 12. Churn y señales | Churn de cuentas con umbral de inactividad, puntuación de leads y su validación | Mensual y trimestral |
| 13. LTV | LTV de la cuenta por canal, LTV/CAC y valor para las pujas | Trimestral |
| 14. Demanda | Previsión de leads o de pedidos con rango y su revisión mensual | Mensual |
| 15. Plan de activación | Campos del CRM, orden de llamada, flujos y audiencias de paid media | Mensual |
| 16. Ficha del experimento (APPA) | Backlog con etapa AARRR e ICE, ficha, muestra y seguimiento | Cada ciclo |
| 17. Ficha de riesgos | Sesgo, incertidumbre, consentimiento, transparencia y revisión del modelo | Trimestral |
| 18. Checklist de la sesión 2 | Checklist del informe completo y calendario de revisión | Al entregar |

Las ideas de cada paso salen de libros y artículos de analítica, experimentación y análisis predictivo, y de la documentación oficial de GA4, Google Ads, Meta y la AEPD. Las tienes en «Recursos», al final, con lo que aporta cada fuente a cada paso.

## Vocabulario

| Término | Qué significa | Dónde se ve |
| --- | --- | --- |
| Lead | Contacto de alguien que puede ser cliente: un formulario, una llamada, un WhatsApp | GA4: `generate_lead`. CRM: estado «nuevo» |
| Lead cualificado | Lead que el comercial ha revisado y encaja: es del perfil, tiene necesidad y se puede atender | CRM: estado «cualificado» |
| Cliente | Lead que ha comprado por primera vez | CRM: estado «cliente», fecha del primer pedido |
| Ingreso recurrente | Lo que el cliente paga cada mes mientras sigue | CRM o facturación |
| Tasa de cualificación | Cualificados / leads | CRM |
| Tasa de cierre | Clientes / leads ya resueltos | CRM |
| Etapa AARRR | Adquisición, Activación, Retención, Recomendación o Ingresos | Matriz de conversiones |
| Cohorte | Grupo con un rasgo, una acción y un momento comunes: las cafeterías que hicieron su primer pedido en marzo desde LinkedIn | Matriz de retención |
| Churn o baja | Cliente que deja de serlo. Sin contrato, el que supera el umbral de inactividad | CRM |
| Puntuación de leads | Probabilidad de que un lead acabe siendo cliente, calculada con lo que se sabe al recibirlo | Campo del CRM |
| LTV | Valor de vida: margen que deja un cliente mientras sigue | Hoja de cálculo o CRM |
| CAC | Coste de captar un cliente | Coste completo / clientes |
| Grupo de control (holdout) | Parte del segmento, elegida al azar, que no recibe la acción, para comparar | Ficha del experimento |
| ICE | Impacto × Confianza × Facilidad, de 1 a 10 cada uno | Backlog de APPA |
