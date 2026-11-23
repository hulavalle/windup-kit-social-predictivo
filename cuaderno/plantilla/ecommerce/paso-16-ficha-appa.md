# Paso 16. Ficha del experimento (APPA)

**Qué te llevas.** El backlog de puntos de mejora de tu tienda con su etapa AARRR y su ICE, la ficha del experimento con grupo de control, el tamaño de muestra calculado y el seguimiento después de lanzar.

## Por qué importa

Una predicción no es un resultado. Si llamas a los suscriptores con riesgo y la mitad se queda, ¿se habrían quedado igual sin la llamada? Sin grupo de control, solo sabes que hiciste algo, no que funcionó.

APPA ordena el trabajo en cuatro fases:

1. **Analysis.** Dónde duele y por qué. Cada punto de mejora se describe sin solución, con su evidencia, su etapa AARRR y su métrica. Separa el síntoma (lo que ve la analítica) de la causa.
2. **Plan.** Qué cambiamos y cómo lo sabremos. Cada punto de mejora da una o varias hipótesis con la forma «Si [cambio], entonces [efecto en la métrica]». Cada hipótesis da una o varias iniciativas, y cada iniciativa es un test o una implementación directa.
3. **Practice.** La acción con grupo de control, métricas, tamaño de muestra y la decisión escrita antes de empezar.
4. **Action.** Lanzar lo que funciona y vigilar que el efecto se mantiene. Lo que no se lanza es gasto.

Para priorizar, **ICE** = impacto × confianza × facilidad, de 1 a 10 cada uno. La confianza depende de la evidencia: una opinión vale poco; los datos de tus clientes, bastante; un experimento anterior, mucho. Conviene que puntúe alguien distinto de quien propuso el punto.

**¿Test o implementación directa?** Se testea lo que tiene impacto desconocido o riesgo. Lo previsible y reversible se implanta directamente y se vigila. También se implanta directamente cuando no hay volumen para un test: con pocos clientes, el test no tiene potencia y no dirá nada.

El **grupo de control (holdout)** es una parte del segmento, sorteada al azar, que no recibe la acción. Comparar «antes y después» no vale: en medio cambian la temporada, los precios y las campañas. Se comparan dos grupos al mismo tiempo.

El **tamaño de muestra** se calcula antes, con una calculadora de tamaño de muestra para tests A/B. Pide cuatro datos: la tasa actual de la métrica, el efecto mínimo que quieres detectar, el nivel de significación (0,05) y la potencia (80 %). Ojo con el efecto absoluto y el relativo: pasar del 10 % al 12 % (2 puntos absolutos) pide unos 3.600 por grupo; un 2 % relativo (del 10 % al 10,2 %) pide más de 350.000. Y no pares el test antes de llegar a la muestra.

## Ejemplo con Café Fandango

*Ejemplo 16.1. El backlog de la tienda*

| ID | Punto de mejora (sin solución) | Etapa AARRR | Evidencia | I | C | E | ICE | Estado |
| ------ | ------ | ------ | ------ | -- | -- | -- | ------ | ------ |
| retencion-001 | Los suscriptores de riesgo alto se van sin que nadie lo sepa | Retención | Del decil de más riesgo se va el 41,8 % frente al 8,3 % de media | 8 | 5 | 7 | 280 | Aprobado |
| retencion-002 | Los que entran con el 50 % de descuento se van pronto | Retención | 37,2 % de bajas en el mes frente al 7,1 % sin descuento | 6 | 7 | 6 | 252 | Backlog |
| retencion-003 | Una incidencia de soporte dispara la baja | Retención | 62,3 % de bajas con incidencia frente al 8,6 % sin ella | 6 | 6 | 5 | 180 | Backlog |
| adquisicion-001 | TikTok trae suscriptores que no se quedan | Adquisición | 16 % activos en el mes 12 frente al 57 % de Instagram | 6 | 6 | 6 | 216 | Backlog |
| aarrr-001 | Hay una etapa del embudo que no medimos | La que salga del paso 1 | La etapa sin evento de la matriz (paso 1) | 5 | 3 | 6 | 90 | Analizando |

Las puntuaciones de I, C y E son juicio del equipo. Las evidencias salen de los datos.

*Ejemplo 16.2. Hipótesis e iniciativas de retencion-001*

| ID | Hipótesis | Iniciativa | Tipo |
| ------ | ------ | ------ | ------ |
| retencion-001-1 | Si contactamos a los suscriptores de alto valor con riesgo, entonces baja su churn a 60 días | retencion-001-1-1: llamada o email personal de atención al cliente, sin descuento | Test con grupo de control |
| retencion-001-2 | Si ofrecemos saltar un mes en lugar de darse de baja, entonces baja el churn a 60 días | retencion-001-2-1: botón «saltar un mes» en la página de baja | Implementación directa, reversible |

*Ejemplo 16.3. La ficha del experimento*

| Campo | Café Fandango |
| ------ | ------ |
| Punto de mejora | retencion-001: los suscriptores de riesgo alto se van sin que nadie lo sepa |
| Hipótesis | Si contactamos a los suscriptores de alto valor con riesgo, entonces baja su churn a 60 días |
| Hipótesis nula | El contacto no cambia el churn a 60 días |
| Iniciativa | Llamada o email personal, sin descuento |
| A quién | Suscriptores con riesgo de baja ≥ 13,6 % |
| Grupo de control | 20 % del segmento, al azar y persistente, sin contacto |
| Métrica primaria | Churn a 60 días |
| Métrica secundaria | Entregas saltadas en los 60 días |
| Contrapeso | Margen perdido en descuentos: si alguien ofrece descuento, se apunta |
| Significación y potencia | 0,05 y 80 % |
| Muestra y duración | Unos 39 suscriptores de riesgo al mes: hay que acumular varios meses |
| Decisión, escrita antes | Si el churn del grupo contactado baja frente al de control, se lanza al CRM; si no, se descarta |

Para las cafeterías no hay test: ocho cuentas con pedidos decrecientes no dan para un grupo de control. Ahí la acción se implanta directamente y se sigue con la serie temporal.

## Tu proyecto

1. Haz el backlog (plantilla 16.1). Sale de los pasos 11 a 15: cada patrón que encontraste en cohortes, churn y LTV es un punto de mejora. Ponle ID, etapa AARRR, evidencia y estado (analizando, backlog, presentado, aprobado, no aprobado, solucionado).
2. Puntúa I, C y E. Que puntúe otra persona. Presenta como mucho cinco puntos por reunión.
3. Para el punto con más ICE, escribe hipótesis e iniciativas (plantilla 16.2). Decide si cada iniciativa es test o implementación directa.
4. Rellena la ficha del experimento (plantilla 16.3). La decisión se escribe antes de empezar.
5. Calcula el tamaño de muestra (plantilla 16.4):
   - Tasa actual: el churn a 60 días del segmento, de tu validación del paso 12.
   - Efecto mínimo: la bajada más pequeña que haría rentable la acción. Escríbelo en puntos absolutos.
   - Significación 0,05 y potencia 80 %.
   - Mete los datos en una calculadora de tamaño de muestra (en «Recursos» tienes dos) y apunta la muestra por grupo.
   - Divide por los clientes que entran al segmento cada mes: son los meses que tardarás.
6. Si los meses salen demasiados, tienes tres salidas: buscar un efecto mayor, ampliar el segmento o pasar a implementación directa con seguimiento.
7. Sortea el grupo de control y guárdalo en el CRM (`grupo_experimento`, paso 15). El sorteo es una vez por cliente: no cambia de grupo cada mes.
8. Lanza y sigue el experimento cada mes (plantilla 16.5). No mires el resultado para decidir antes de llegar a la muestra.
9. Al terminar, aplica la decisión que escribiste. Si lanzas, mantén un grupo de control pequeño y persistente (un 10 %) para ver si el efecto dura.
10. Si no hubo test, sigue la métrica con una serie temporal: compara la tendencia de antes y después del lanzamiento, no solo el valor.
11. Copia cada experimento a `plan/backlog-appa.csv`, también los que no funcionaron.

### Con tu asistente de IA

```text
Te adjunto el resultado de un experimento: una fila por cliente con su grupo
(contacto o control) y si se dio de baja en los 60 días. No hay datos personales.
Hipótesis nula: el contacto no cambia el churn a 60 días.
Con código:
1. Churn a 60 días de cada grupo y la diferencia en puntos.
2. Una prueba de dos proporciones con su p-valor y el intervalo de confianza
   de la diferencia al 95 %.
3. Si la muestra llegó a la que habíamos calculado: [muestra por grupo].
No me digas si funcionó: dame las cifras y yo aplico la decisión escrita antes.
```

### Cómo comprobarlo

- El grupo de control y el de contacto deberían parecerse antes de empezar: mismo riesgo medio, mismo valor medio. Si no, el sorteo falló.
- Cuenta a mano las bajas de cada grupo en tu hoja.
- Comprueba que nadie del grupo de control recibió el contacto.

*Plantilla 16.1. Tu backlog*

| ID | Punto de mejora (sin solución) | Etapa AARRR | Evidencia | I | C | E | ICE | Estado |
| ------ | ------ | ------ | ------ | -- | -- | -- | ------ | ------ |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

*Plantilla 16.2. Tus hipótesis e iniciativas*

| ID | Hipótesis (Si…, entonces…) | Iniciativa | Tipo (test o implementación directa) |
| ------ | ------ | ------ | ------ |
| | | | |
| | | | |
| | | | |

*Plantilla 16.3. Tu ficha del experimento*

| Campo | Tu proyecto |
| ------ | ------ |
| Punto de mejora | |
| Hipótesis (Si…, entonces…) | |
| Hipótesis nula | |
| Iniciativa | |
| A quién | |
| Grupo de control | |
| Métrica primaria | |
| Métrica secundaria | |
| Contrapeso, con umbral | |
| Significación y potencia | |
| Muestra y duración | |
| Decisión, escrita antes | |

*Plantilla 16.4. Tu tamaño de muestra*

| Dato | Valor | De dónde sale |
| ------ | ------ | ------ |
| Tasa actual de la métrica primaria | | |
| Efecto mínimo a detectar (puntos absolutos) | | |
| Significación | 0,05 | |
| Potencia | 80 % | |
| Reparto entre grupos | | |
| Muestra por grupo (calculadora) | | |
| Clientes que entran al segmento al mes | | |
| Meses necesarios | | |

*Plantilla 16.5. Tu seguimiento*

| Mes | Clientes en contacto | Clientes en control | Métrica primaria, contacto | Métrica primaria, control | Contrapeso | Acción |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

## Errores frecuentes

- Comparar antes y después en lugar de dos grupos a la vez.
- Escribir la decisión después de ver el resultado.
- Parar el test en cuanto parece que funciona.
- Mirar diez métricas y quedarse con la que salió bien. Con cinco métricas, la probabilidad de un falso positivo pasa del 20 %.
- Confundir efecto absoluto y relativo en la calculadora.
- Un reparto desigual sin saber que pide más muestra.
- Testear sin volumen. Si la muestra tarda años, implanta y vigila.
- Guardar solo los experimentos que ganaron.

## Antes de seguir

- [ ] Tu backlog tiene ID, etapa AARRR, evidencia e ICE en cada punto.
- [ ] Cada hipótesis sigue la forma «Si…, entonces…».
- [ ] Sabes si cada iniciativa es test o implementación directa, y por qué.
- [ ] La ficha tiene grupo de control, métrica primaria, contrapeso y decisión escrita antes.
- [ ] El tamaño de muestra está calculado y sabes cuántos meses tarda.
- [ ] El seguimiento tiene fecha cada mes.
- [ ] El experimento está en `plan/backlog-appa.csv`.
