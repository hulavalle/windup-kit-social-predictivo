# Paso 6. Pregunta y exploración en GA4

**Qué te llevas.** Una pregunta sobre redes con la exploración de forma libre que la responde, una exploración de rutas, la comparación de modelos de atribución y la comprobación de que tus cifras cuadran con el informe estándar y con la tienda.

## Por qué importa

Primero la pregunta, después GA4. Si abres GA4 sin pregunta, acabas mirando el informe que sale por defecto y no decides nada.

Antes de montar nada, conviene tener claras tres diferencias:

- **Adquisición de usuarios** dice con qué canal llegó cada usuario la primera vez. **Adquisición de tráfico** dice el canal de cada sesión. Un usuario que llega por Instagram y vuelve diez veces escribiendo la URL cuenta para Instagram en el primer informe y sobre todo para Direct en el segundo. Las dos cifras no se comparan.
- **Informes y exploraciones.** Los informes estándar responden preguntas fijas. Una exploración cruza las dimensiones y métricas que tú eliges, como el contenido del enlace con las compras.
- **Atribución.** GA4 reparte el mérito de cada evento clave con el modelo basado en datos o con el último clic. Los modelos de primer clic y lineal ya no existen. El último clic infravalora las redes: el post que despertó el interés casi nunca es el último clic antes de pagar.

GA4 no lo ve todo. En Café Fandango falta cerca del 8 % de las compras por rechazo de cookies, y no ve ninguna renovación de la suscripción. Para contar clientes e ingresos manda la tienda. GA4 sirve para saber de dónde llegan y qué hacen en la web.

## Ejemplo con Café Fandango

*Ejemplo 6.1. Exploración de forma libre*

| Campo | Café Fandango |
| ------ | ------ |
| Pregunta | ¿Qué contenido de Instagram trae compras? |
| Decisión | Qué formatos repite la community manager el mes que viene |
| Técnica | Exploración de forma libre |
| Filas | Contenido manual de la sesión |
| Valores | Sesiones, compras, ingresos |
| Filtro | Fuente de la sesión = instagram |

*Ejemplo 6.2. Lo que dice la tienda por contenido de Instagram*

| Contenido | Clientes | Ingresos 1.ª compra | Altas de suscripción |
| ------ | ------ | ------ | ------ |
| `reel` | 238 | 4.835 € | 151 |
| `laura-cafe` | 219 | 3.988 € | 131 |
| `carrusel` | 193 | 4.020 € | 119 |
| `reel-v60` | 174 | 3.137 € | 86 |
| `video-suscripcion` | 134 | 2.725 € | 69 |
| `imagen` | 129 | 2.551 € | 79 |
| `carrusel-origenes` | 126 | 2.473 € | 63 |

Los reels traen más clientes y más altas. El contenido de la influencer trae casi tantos clientes como los reels, pero el paso 7 dirá si cubren su cuota.

*Ejemplo 6.3. GA4 frente a la tienda, de junio de 2025 a octubre de 2026*

| Red | Compras en GA4 | Ingresos en GA4 | Clientes en la tienda | Ingresos 1.ª compra en la tienda |
| ------ | ------ | ------ | ------ | ------ |
| Instagram | 1.106 | 21.630 € | 1.213 | 23.729 € |
| Facebook | 177 | 3.288 € | 194 | 3.600 € |
| TikTok | 927 | 10.991 € | 1.007 | 11.960 € |

GA4 se queda algo por debajo en las tres redes, por las compras sin consentimiento. El orden de las redes no cambia: GA4 sirve para comparar canales, aunque no para contar el dinero.

## Tu proyecto

1. Escribe la pregunta y la decisión (plantilla 6.1). La técnica viene después.
2. Monta la exploración de forma libre: en GA4, **Explorar** > **Exploración de forma libre**. Importa las dimensiones (por ejemplo, **Fuente de la sesión**, **Contenido manual de la sesión**, **Grupo de canales predeterminado de la sesión**) y las métricas (**Sesiones**, **Eventos clave**, **Ingresos totales** o el recuento de `purchase`).
3. Arrastra las dimensiones a **Filas** y las métricas a **Valores**. Añade el filtro de la pregunta.
4. Monta una exploración de rutas (plantilla 6.2): **Explorar** > **Exploración de rutas**. Empieza por el final: pon `purchase` como nodo final y mira qué páginas y eventos vienen antes. Responde preguntas como «¿los compradores que llegan de Instagram pasan por la guía de V60?».
5. Compara modelos de atribución (plantilla 6.3). En **Publicidad**, los informes de atribución dejan ver las conversiones por canal con el modelo basado en datos y con el último clic, y las rutas de conversión con los toques de cada canal. Apunta la diferencia de las redes entre un modelo y otro.
6. Comprueba que la exploración cuadra con el informe estándar y con la tienda (plantilla 6.4).
7. Guarda la exploración con un nombre que diga la pregunta, como «¿Qué contenido de Instagram trae compras?».

### Con tu asistente de IA

Exporta la exploración a CSV (icono de descarga arriba a la derecha) y pídele que la lea:

```text
Te adjunto una exportación de GA4: contenido manual de la sesión, sesiones, compras
e ingresos, solo fuente instagram. No hay datos personales.
Pregunta: ¿qué contenido trae más compras y más ingresos por sesión?
Decisión: qué formatos repetimos el mes que viene.
Calcula con código la tasa de compra por sesión y el ingreso por sesión de cada contenido.
Ordena de mayor a menor. Marca los contenidos con menos de 100 sesiones:
con tan pocas, la diferencia puede ser azar.
```

### Cómo comprobarlo

- El total de la exploración para un filtro debe coincidir con el informe estándar con el mismo filtro y las mismas fechas. Si no cuadra, revisa el ámbito: usuario, sesión o evento.
- Las compras de GA4 de un mes deben quedarse algo por debajo de los pedidos de WooCommerce del mismo mes. Si GA4 da más, tienes compras duplicadas (por ejemplo, la página de gracias recargada). Si da mucho menos, revisa el consentimiento y la etiqueta.

*Plantilla 6.1. Tu exploración de forma libre*

| Campo | Tu proyecto |
| ------ | ------ |
| Pregunta | |
| Decisión que tomarías con la respuesta | |
| Técnica | |
| Filas | |
| Valores | |
| Filtro | |
| Fechas | |

*Plantilla 6.2. Tu exploración de rutas*

| Campo | Tu proyecto |
| ------ | ------ |
| Pregunta | |
| Nodo inicial o final | |
| Evento o página del nodo | |
| Segmento (por ejemplo, sesiones de Instagram) | |
| Qué esperas ver | |
| Qué has visto | |

*Plantilla 6.3. Tu comparación de atribución*

| Canal | Eventos clave con el modelo basado en datos | Con el último clic | Diferencia | Lectura |
| ------ | ------ | ------ | ------ | ------ |
| Organic Social | | | | |
| Paid Social | | | | |
| Email | | | | |
| Organic Search | | | | |
| Direct | | | | |

*Plantilla 6.4. Tu comprobación*

| Cifra | Exploración | Informe estándar | Tienda | ¿Cuadra? |
| ------ | ------ | ------ | ------ | -- |
| Sesiones del filtro | | | No aplica | |
| Compras | | | | |
| Ingresos | | | | |

## Errores frecuentes

- Comparar Adquisición de usuarios con Adquisición de tráfico.
- Mezclar dimensiones de ámbitos distintos, como fuente del primer usuario con eventos de la sesión, y no entender el resultado.
- Decidir con contenidos de pocas sesiones.
- Contar los ingresos con GA4 en lugar de con la tienda.
- Juzgar las redes solo con el último clic.

## Antes de seguir

- [ ] Escribiste la pregunta y la decisión antes de abrir GA4.
- [ ] La exploración está guardada con el nombre de la pregunta.
- [ ] Tienes una exploración de rutas con su lectura.
- [ ] Sabes cuánto cambian las redes entre el modelo basado en datos y el último clic.
- [ ] La cifra de la exploración cuadra con el informe estándar.
- [ ] Sabes cuánto se queda GA4 por debajo de la tienda.
