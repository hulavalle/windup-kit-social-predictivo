# Paso 16. Ficha del experimento (APPA)

**Qué te llevas.** El backlog de APPA de tu proyecto con su etapa AARRR y su ICE, la ficha del experimento prioritario, el cálculo del tamaño de muestra, la decisión honesta entre test e implementación directa y el plan de seguimiento después de lanzar. El backlog lo copias a `plan/backlog-appa.csv`.

## Para qué sirve

Una predicción no es un resultado. Si llamas a las cuentas en riesgo y siguen pidiendo, no sabes si siguieron por la llamada o habrían seguido igual. Sin grupo de control, solo sabes que hiciste algo, no que funcionó.

APPA ordena el trabajo en cuatro fases:

- **Analysis.** Dónde duele y por qué. Distingue el síntoma (lo que ve la analítica) de la causa. Cada punto de mejora entra en el backlog con su etapa AARRR.
- **Plan.** La hipótesis «Si…, entonces…», con su métrica, priorizada con ICE: impacto × confianza × facilidad, de 1 a 10 cada uno. La confianza depende de la evidencia que tienes, no de lo que te apetece. Mejor si prioriza alguien distinto de quien detectó el problema.
- **Practice.** La acción con un grupo de control: una parte del segmento, al azar, no la recibe. Métrica primaria, contrapeso, tamaño de muestra, duración y la decisión escrita antes de empezar.
- **Action.** Lanzar lo que funciona y vigilar que el efecto se mantiene.

No todo se testea. Se testea lo de impacto desconocido o con riesgo. Lo previsible y fácil de deshacer se implanta directamente y se vigila.

Y en captación de leads hay que ser honesto con el volumen. Un test necesita muestra. Si entran 30 leads al mes, un test sobre la tasa de cierre puede tardar años. Entonces se implanta directamente y se sigue con la serie temporal: la tendencia antes frente a la tendencia después. Es una prueba más débil que un test, y se dice.

## Cómo se hace

1. Escribe los puntos de mejora del backlog. Un punto de mejora es algo que daña una métrica; una oportunidad, algo que falta. Describe el problema sin la solución.
2. Pon a cada uno su etapa AARRR, su evidencia y su métrica.
3. Puntúa el ICE y ordena.
4. Para el primero, escribe la hipótesis «Si…, entonces…».
5. Decide test o implementación directa.
6. Si es test: calcula la muestra con una calculadora de tamaño de muestra (significación del 5 %, potencia del 80 %, el efecto mínimo que te importa). Divide entre el volumen mensual: así sabes cuánto durará.
7. Si la duración no es razonable, pasa a implementación directa con seguimiento.
8. Escribe la decisión antes de lanzar: qué harás con cada resultado.
9. Después de lanzar, revisa la métrica cada mes frente a la serie anterior.

### Con tu asistente de IA

Pega tu backlog y pide: «Revisa cada hipótesis. ¿Tiene una métrica que se pueda medir? ¿El ICE está justificado por la evidencia?». Para la muestra, pide: «Calcula con código el tamaño de muestra por grupo para pasar de [tasa actual] a [tasa objetivo] con significación del 5 % y potencia del 80 %. Después dime cuántos meses tardaría con [volumen] al mes». Comprueba la cifra con una calculadora de tamaño de muestra en línea.

### Cómo comprobarlo

Pide a otra persona del equipo que lea la ficha. Si no sabe qué decidirás con cada resultado, la ficha no está terminada.

## Ejemplo con Fandango para cafeterías

*Ejemplo 16.1. Backlog de APPA*

| ID | Etapa AARRR | Punto de mejora | Evidencia | I | C | E | ICE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cafeterias-001 | Retención | Cafeterías con pedidos decrecientes dejan de pedir sin que nadie lo sepa | El 40 % de las cuentas con la señal deja de pedir; hoy hay 8 | 8 | 7 | 8 | 448 |
| cafeterias-002 | Ingresos | Muchos leads de Instagram no son cafeterías | 113 leads perdidos por ese motivo | 6 | 7 | 7 | 294 |
| cafeterias-003 | Ingresos | Leads que solo quieren precios consumen llamadas | 88 leads de Instagram perdidos por ese motivo | 5 | 6 | 8 | 240 |
| cafeterias-004 | Ingresos | Leads que no responden a la llamada | 94 en Instagram y 27 en LinkedIn | 5 | 4 | 6 | 120 |
| cafeterias-005 | La que salga del paso 1 | Hay una etapa del embudo de cafeterías que no medimos | La etapa sin fila en la matriz (paso 1) | 4 | 3 | 9 | 108 |

El ICE es la valoración del equipo, con la evidencia de la columna de al lado.

*Ejemplo 16.2. Ficha del experimento*

| Campo | Fandango para cafeterías |
| --- | --- |
| ID | cafeterias-001-1 |
| Punto de mejora | Cafeterías con pedidos decrecientes dejan de pedir sin que nadie lo sepa |
| Etapa AARRR | Retención |
| Hipótesis | Si el comercial llama a las cafeterías con un pedido por debajo del 80 % de su media, entonces menos cafeterías dejan de pedir en los dos meses siguientes |
| ICE | Impacto 8 × confianza 7 × facilidad 8 = 448 |
| Test o implementación directa | Implementación directa: con 8 cuentas en riesgo no hay test posible |
| Grupo de control | No hay. Se compara con la serie anterior |
| Métrica primaria | Cafeterías que dejan de pedir al mes |
| Contrapeso | Descuentos concedidos en esas llamadas |
| Muestra y duración | Todas las cuentas con la señal, durante seis meses |
| Decisión, escrita antes | Si la media baja de 3,3 al mes sin subir los descuentos, se mantiene; si no, se revisa el guion de la llamada |

*Ejemplo 16.3. Cuándo sí habría test*

| Campo | Fandango para cafeterías |
| --- | --- |
| Iniciativa | Pregunta obligatoria «¿Tienes una cafetería o un restaurante?» en el formulario de Instagram (cafeterias-002) |
| Métrica primaria | Tasa de cualificación de Instagram, hoy del 31 % |
| Efecto mínimo que importa | Llegar al 40 % |
| Muestra | Más de 400 leads por grupo, con significación del 5 % y potencia del 80 % |
| Volumen | Instagram trajo 462 leads en 17 meses |
| Conclusión | Un test duraría años. Se implanta directamente y se sigue la tasa de cualificación mes a mes |

*Ejemplo 16.4. Seguimiento después de lanzar*

| Mes | Cafeterías que dejan de pedir | Media anterior | Descuentos concedidos | Nota |
| --- | --- | --- | --- | --- |
| Antes de lanzar | | 3,3 al mes (marzo a agosto de 2026) | | Línea de partida |
| Mes 1 | | | | Se rellena con tus datos |
| Mes 2 | | | | |
| Mes 3 | | | | |

## Tu proyecto

*Plantilla 16.1. Tu backlog de APPA*

| ID | Etapa AARRR | Punto de mejora | Evidencia | I | C | E | ICE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

*Plantilla 16.2. Tu ficha del experimento*

| Campo | Tu proyecto |
| --- | --- |
| ID | |
| Punto de mejora | |
| Etapa AARRR | |
| Hipótesis (Si…, entonces…) | |
| ICE | |
| Test o implementación directa | |
| Grupo de control | |
| Métrica primaria | |
| Métrica secundaria | |
| Contrapeso | |
| Muestra y duración | |
| Decisión, escrita antes | |

*Plantilla 16.3. Tu tamaño de muestra*

| Dato | Valor |
| --- | --- |
| Tasa actual | |
| Tasa que quieres alcanzar | |
| Significación y potencia | 5 % y 80 % |
| Muestra por grupo | |
| Volumen al mes | |
| Duración | |
| ¿Es razonable? Si no, qué haces | |

*Plantilla 16.4. Tu seguimiento*

| Mes | Métrica primaria | Línea de partida | Contrapeso | Nota |
| --- | --- | --- | --- | --- |
| Antes de lanzar | | | | |
| Mes 1 | | | | |
| Mes 2 | | | | |
| Mes 3 | | | | |
| Mes 6 | | | | |

## Errores frecuentes

- Comparar antes y después y llamarlo test. Sin grupo simultáneo, cualquier cambio de temporada parece un efecto.
- Lanzar un test sin calcular la muestra. Acabarás parando cuando el resultado te guste.
- Parar antes de tiempo. Deja correr el test hasta la muestra que calculaste, en semanas completas.
- Mirar diez métricas y quedarte con la que sale. Una métrica primaria, decidida antes.
- Llamar test a algo que no tiene volumen. Si no hay muestra, dilo y haz seguimiento.

## Antes de seguir

- [ ] Cada punto del backlog tiene etapa AARRR, evidencia e ICE.
- [ ] La hipótesis tiene la forma «Si…, entonces…» y una métrica.
- [ ] Has calculado la muestra y su duración.
- [ ] La elección entre test e implementación directa está justificada.
- [ ] La decisión está escrita antes de lanzar.
- [ ] El seguimiento tiene su línea de partida.
- [ ] `plan/backlog-appa.csv` tiene las mismas filas que la plantilla 16.1.
