# Recursos

Estas son las fuentes de la plantilla, agrupadas por los pasos que apoyan, con lo que aporta cada una. Los artículos y el libro dan el método. La documentación oficial da los menús, los requisitos y los umbrales de GA4, Google Ads, Meta, WooCommerce y la AEPD, que cambian a menudo: compruébala antes de cada proyecto.

## Pasos 0 a 2. El marco: del like al euro

- Dave McClure, *Startup Metrics for Pirates*, 2007. Paso 1: las cinco etapas del embudo AARRR y la pregunta de cada una.
- Ubaldo Hervás, *Experimentación online*. Paso 1: la columna de etapa AARRR en cada punto de mejora. Paso 2: métricas estratégicas, que tardan, frente a operativas, que avisan.
- Brandon Schwartz, «The Dashboard Delusion», Growth Notebook. Paso 2: pocas métricas ligadas a decisiones, métricas adelantadas y retrasadas con umbrales de acción y niveles del informe. https://growthnotebook.substack.com/p/the-dashboard-delusion-why-most-marketing
- Kendall Dickieson, «How to Make Social Media Actually Drive Results». Paso 0: por qué un informe de redes medido solo por métricas de plataforma no convence a la dirección. https://kendalldickieson.substack.com/p/how-to-make-social-media-actually
- Rachel Goulet en la newsletter de Lia Haberman, «5 Steps to (Finally) Proving Organic Social ROI». Pasos 0 y 2: conectar el contenido con el resto del embudo y comunicar el resultado a la dirección. https://liahaberman.substack.com/p/icymi-5-steps-to-finally-proving
- WooCommerce, «Order Attribution Tracking». Pasos 2, 3 y 7: el origen, la fuente, la campaña y el medio de cada pedido. https://woocommerce.com/document/order-attribution-tracking/

## Paso 3. UTMs de redes

- Ayuda de Google Analytics, grupo de canales predeterminado. Las reglas de Organic Social, Paid Social, Paid Other y Direct, y la lista de fuentes sociales. https://support.google.com/analytics/answer/9756891?hl=es
- Ayuda de Google Analytics, parámetros UTM. Qué parámetros reconoce GA4, que distingue mayúsculas y las prácticas recomendadas. https://support.google.com/analytics/answer/10917952?hl=es

## Pasos 4 y 5. Objetivos y su valor

- Brandon Schwartz, «The Dashboard Delusion». Paso 4: un OKR de captación en redes con resultados clave medibles.
- Ubaldo Hervás, *Experimentación online*. Paso 4: el contrapeso; optimizar el coste por adquisición con descuentos capta clientes que no se quedan.
- Sprout Social, Owned Media Value. Paso 5: el valor de las impresiones orgánicas con el CPM de los anuncios. https://sproutsocial.com/insights/owned-media-value/

## Pasos 6 a 8. GA4, ROI y análisis con IA

- Ayuda de Google Analytics, diferencia entre Adquisición de usuarios y Adquisición de tráfico. Paso 6. https://support.google.com/analytics/answer/14731736?hl=es
- Ayuda de Google Analytics, exploración de rutas. Paso 6. https://support.google.com/analytics/answer/9317498?hl=es
- Ayuda de Google Analytics, rutas de atribución y modelos disponibles. Paso 6: qué modelos quedan en GA4. https://support.google.com/analytics/answer/10595568?hl=es
- Brandon Schwartz, «The Dashboard Delusion». Paso 7: ROAS frente a MER y la sobreatribución de las plataformas.
- Ubaldo Hervás, *Experimentación online*. Paso 7: ROI atribuido frente a ROI causado y el caso de la campaña reactivada por una causa que era otra.
- `prompts/` y `AGENTS.md` del kit. Paso 8: los prompts de cada práctica y las reglas del asistente de IA.

## Pasos 10 a 12. Escalera, cohortes y churn

- Ubaldo Hervás, *Experimentación online*. Paso 10: la escalera de madurez que termina en la analítica predictiva y pide un año de histórico fiable.
- Ayuda de Google Analytics, métricas predictivas. Pasos 10 y 12: probabilidad de compra y de abandono, y el requisito de 1.000 usuarios que cumplen la condición y 1.000 que no. https://support.google.com/analytics/answer/9846734?hl=es
- Jens Tonberg Larsson, «Unlocking User Retention Insights». Paso 11: la cohorte como rasgo, acción y momento, y la retención bruta frente a la neta. https://anddata.substack.com/p/unlocking-user-retention-insights
- Olga Berezovsky, «How to measure cohort retention». Paso 11: cómo definir activo, no mezclar tipos de cliente y presentar la matriz. https://www.lennysnewsletter.com/p/measuring-cohort-retention
- Pierre-Jean Hillion, «Is your retention great, good or bad?». Paso 11: las curvas mala, buena y sonriente. https://thegrowthmind.substack.com/p/is-your-retention-great-good-or-bad
- Ross Andrews, «Segment vs. Cohort». Paso 11: la diferencia entre cohorte y segmento. https://talkinsaasy.substack.com/p/segment-vs-cohort
- Formo, «How to Use Cohort Analysis in DeFi». Pasos 11 y 12: celdas pendientes en blanco, umbral de inactividad según el ciclo de uso y reenganche antes del hueco. https://formo.so/blog/defi-cohort-analysis
- Ayuda de Google Analytics, exploración de cohortes. Paso 11: criterios, tipos de cálculo y límites. https://support.google.com/analytics/answer/9670133?hl=es
- WooCommerce, estados de las suscripciones. Pasos 11 y 12: qué estado cuenta como activo. https://woocommerce.com/document/subscriptions/statuses/
- Eric Coyle, «Churn Prediction». Paso 12: la definición de churn y sus tres tipos. https://theericcoyleventure.substack.com/p/churn-prediction-using-data-to-predict
- ML Pills, «DIY #23 Predict Customer Lifetime Value». Paso 12: solo señales observables antes, partición por fechas, tendencias frente a totales y lift por deciles. https://mlpills.substack.com/p/diy-23-predict-customer-lifetime

## Pasos 13 y 14. LTV y demanda

- Eric Coyle, «Customer Lifetime Value». Paso 13: las fórmulas de LTV histórico y con margen y churn. https://theericcoyleventure.substack.com/p/customer-lifetime-value-clv-use-predictive
- ML Pills, «DIY #24 Calculate Expected LTV». Paso 13: LTV esperado = probabilidad de seguir activo × ingreso si sigue, y el aviso del doble conteo. https://mlpills.substack.com/p/diy-24-calculate-expected-ltv-from
- ML Pills, «DIY #23». Paso 13: LTV/CAC por canal y por qué ordenar importa más que acertar la cifra exacta.
- Ayuda de Google Ads, pujas por valor. Paso 13: qué valor enviar y los requisitos de conversiones y valores distintos. https://support.google.com/google-ads/answer/14792795?hl=es
- Ayuda de Google Ads, objetivos de ciclo de vida del cliente. Pasos 13 y 15: adquisición de clientes nuevos y reenganche. https://support.google.com/google-ads/answer/12080169?hl=es
- Meta for Developers, estrategias de puja. Paso 13: optimización por valor y ROAS mínimo. https://developers.facebook.com/docs/marketing-api/bidding/overview/bid-strategy
- Jason Branin, «Beyond the Hockey Stick». Paso 14: rangos y escenarios en lugar de una sola línea. https://romulusstrategy.substack.com/p/beyond-the-hockey-stick-why-most

## Pasos 15 a 17. Activar, experimentar y riesgos

- Ayuda de Google Analytics, audiencias predictivas. Paso 15: plantillas, requisitos y cómo pasan a Google Ads. https://support.google.com/analytics/answer/9805833?hl=es
- Ayuda de Google Ads, Customer Match. Paso 15: consentimiento, caducidad a los 540 días y mínimo de actualizaciones. https://support.google.com/google-ads/answer/6379332?hl=es
- Meta for Developers, audiencias similares. Paso 15: tamaño mínimo de la fuente. https://developers.facebook.com/docs/marketing-api/audiences/guides/lookalike-audiences
- ML Pills, «DIY #23». Pasos 15 y 17: tramos de valor con acción por tramo, decisiones por segmento y grupo de control porque el modelo cambia los datos futuros.
- Ubaldo Hervás, *Experimentación online* (método APPA). Paso 16: las cuatro fases, los tres backlogs, la hipótesis «Si…, entonces…», ICE y la confianza según la evidencia, test frente a implementación directa, métricas primarias, secundarias y contrapesos, el tamaño de muestra con efecto absoluto y relativo, el riesgo de muchas métricas, el grupo de control persistente y el seguimiento con serie temporal.
- Evan Miller, calculadora de tamaño de muestra. Paso 16. https://www.evanmiller.org/ab-testing/sample-size.html
- AB Testguide, calculadora de tamaño de muestra. Paso 16. https://abtestguide.com/abtestsize/
- Ayuda de Google Analytics, exploración de tiempo de vida del usuario y datos modelados. Paso 17: lo que GA4 no ve sin consentimiento. https://support.google.com/analytics/answer/9947257?hl=es
- AEPD, guía sobre el uso de las cookies. Paso 17: consentimiento para analítica y publicidad. https://www.aepd.es/guias/guia-cookies.pdf
- Google for Developers, modo de consentimiento. Paso 17. https://developers.google.com/tag-platform/security/concepts/consent-mode?hl=es-419

## Material del kit

- `datos/` y `datos/diccionario.md`. Los CSV de Café Fandango, de los que salen todas las cifras del ejemplo.
- `chuleta.md`. Las fórmulas de AARRR, ROI, cohortes, churn, LTV y APPA en una página.
- `prompts/`. Un prompt por práctica, que adaptas a tus archivos en los pasos 3, 5, 7 y 11 a 15.
- `plan/objetivos.csv`, `plan/costes.csv` y `plan/backlog-appa.csv`. Donde copias tus objetivos (pasos 4 y 5), costes (pasos 0 y 7) y experimentos (paso 16).
- `AGENTS.md` y `brain/`. Las reglas y la memoria de tu asistente de IA.
- De la clase 1: [plan/matriz.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/matriz.csv) (paso 1) y [plan/utms.csv](https://github.com/hulavalle/windup-kit-medicion/blob/main/plan/utms.csv) (paso 3).
