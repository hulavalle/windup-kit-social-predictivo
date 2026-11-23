# Paso 17. Ficha de riesgos

**Qué te llevas.** Los riesgos de tu modelo y de tus datos con su mitigación y responsable, el consentimiento que necesita cada uso del dato, lo que le cuentas al cliente y la revisión periódica del modelo.

## Por qué importa

¿Nos podemos fiar del modelo, y podemos usarlo? Un modelo honesto dice cuánto no sabe. Hay cuatro familias de riesgo:

- **Sesgo.** Un modelo aprende del pasado, y sus decisiones cambian los datos del futuro. Si solo das descuentos a los clientes de TikTok, el modelo aprende que los de TikTok se van, porque los cazadescuentos se van. Y si contactas a todos los de riesgo alto, dentro de seis meses no sabrás qué habría pasado sin contacto. Por eso se mantiene siempre un grupo de control.
- **Incertidumbre.** Una probabilidad no es una certeza. Del 10 % con más riesgo se van cuatro de cada diez, no todos. Se decide por segmento, no por persona, y se dan rangos. Cuando cambian los precios, las promociones o el tipo de cliente que captas, el modelo pierde calibración.
- **Datos que faltan.** Sin cookies faltan datos: rechazos de consentimiento, Safari, bloqueadores. Los datos modelados por el modo de consentimiento no entran en las exploraciones de cohortes de GA4. La base es el dato propio con consentimiento: la cuenta de cliente, los pedidos, el email.
- **Datos personales.** A ningún asistente de IA se le suben nombres, emails ni teléfonos. Las listas de clientes para publicidad, como Customer Match, solo con consentimiento. Y si una decisión automática tiene efectos importantes sobre una persona, el RGPD pide garantías: no dejes que el modelo decida solo esas cosas.

También hay que contarlo. Si usas los datos de compra para calcular el riesgo de cada cliente y personalizar ofertas o anuncios, la política de privacidad de la tienda tiene que decirlo con palabras claras.

## Ejemplo con Café Fandango

*Ejemplo 17.1. Riesgos de la tienda*

| Riesgo | En Café Fandango | Mitigación | Responsable |
| ------ | ------ | ------ | ------ |
| Sesgo | Si solo se dan descuentos a TikTok, el modelo aprende que TikTok se va | Grupo de control del 20 % en cada acción y revisión de las señales cada trimestre | Responsable del dato |
| Incertidumbre | Del 10 % con más riesgo se van 4 de cada 10, no todos | Decidir por segmento; enseñar siempre el lift y el rango | Responsable del dato |
| Fuga de datos | Con `fecha_baja` como señal, el modelo daba un 100 % de exactitud | Prueba de la fuga antes de cada versión del modelo (paso 12) | Responsable del dato |
| Sin cookies | GA4 pierde cerca del 8 % de las compras | Contar clientes e ingresos con la tienda; GA4 solo para canal y comportamiento | Responsable del dato |
| Datos personales en la IA | Las exportaciones de WooCommerce traen emails y direcciones | Identificadores seudónimos antes de subir nada | Quien exporta |
| Consentimiento | Customer Match con todos los clientes | Solo clientes con la casilla de publicidad marcada | Marketing |
| Calibración | Un cambio de precio cambia el riesgo de todos | Revalidar el modelo después de cada cambio de precio o promoción grande | Responsable del dato |

*Ejemplo 17.2. Consentimiento por uso del dato*

| Uso del dato | Consentimiento necesario | Dónde se recoge | Cómo se comprueba |
| ------ | ------ | ------ | ------ |
| Medir con GA4 y píxeles | Cookies de analítica y de publicidad | Banner de cookies con modo de consentimiento v2 | Tag Assistant: las etiquetas esperan al consentimiento |
| Emails de reenganche | Comunicaciones comerciales | Casilla en el pago, sin marcar por defecto | Campo en el cliente de WooCommerce |
| Customer Match y audiencias de Meta | Publicidad personalizada | La misma casilla o una aparte | Solo se exportan clientes con el campo marcado |
| Puntuación de riesgo | Información clara en la política de privacidad | Política de privacidad, enlazada en el pago | Revisión del texto cada vez que cambia el uso |

## Tu proyecto

1. Escribe tus riesgos (plantilla 17.1). Al menos uno de cada familia: sesgo, incertidumbre, datos que faltan y datos personales.
2. Ponles probabilidad e impacto (alto, medio, bajo) y una mitigación concreta con responsable.
3. Para cada uso del dato, escribe qué consentimiento necesita y dónde se recoge (plantilla 17.2):
   - **Cookies**: una plataforma de gestión del consentimiento con el modo de consentimiento v2 de Google. Las etiquetas de GA4, Google Ads y Meta esperan a la respuesta del usuario.
   - **Email**: la casilla de comunicaciones comerciales en el pago o en el alta de la cuenta.
   - **Publicidad con listas de clientes**: el consentimiento para publicidad personalizada. Con usuarios del Espacio Económico Europeo, Google Ads exige enviar las señales de consentimiento con la lista.
4. Escribe lo que le cuentas al cliente (plantilla 17.3): qué haces con sus datos de compra, para qué y cómo puede oponerse. Que lo revise quien lleve la parte legal de la tienda: esta plantilla no sustituye su revisión.
5. Define qué decisiones no se automatizan. Una oferta de reenganche puede salir sola; cerrar una cuenta o negar un servicio, no.
6. Monta la revisión del modelo (plantilla 17.4) y ponla en el calendario.
7. Apunta en `brain/decisiones.md` las reglas que decidas, para que tu asistente de IA las siga.

### Con tu asistente de IA

```text
Te describo el modelo de riesgo de baja de mi tienda: [señales, datos, uso].
No te paso datos de clientes.
1. Dime qué sesgos puede tener: qué grupos de clientes podrían salir con más riesgo
   por cómo los tratamos en el pasado y no por cómo son.
2. Dime qué pasaría con el modelo si cambio el precio o lanzo una promoción grande.
3. Propón una revisión trimestral con comprobaciones y umbrales de alarma.
No me des consejo legal: señala qué debería revisar alguien con formación jurídica.
```

### Cómo comprobarlo

- Abre la tienda en una ventana de incógnito, rechaza las cookies y comprueba en Tag Assistant que GA4 y Meta no envían datos con cookies.
- Exporta la lista de Customer Match y comprueba que todos tienen el campo de consentimiento marcado.
- Cada trimestre, repite el lift por deciles con los dos últimos meses. Si el decil de más riesgo ya no destaca, el modelo necesita revisión.

*Plantilla 17.1. Tus riesgos*

| Riesgo | En tu proyecto | Probabilidad e impacto | Mitigación | Responsable |
| ------ | ------ | ------ | ------ | ------ |
| Sesgo | | | | |
| Incertidumbre | | | | |
| Datos que faltan | | | | |
| Datos personales | | | | |
| | | | | |

*Plantilla 17.2. Tu consentimiento por uso*

| Uso del dato | Consentimiento necesario | Dónde se recoge | Cómo se comprueba |
| ------ | ------ | ------ | ------ |
| | | | |
| | | | |
| | | | |
| | | | |

*Plantilla 17.3. Lo que le cuentas al cliente*

| Qué haces con su dato | Para qué | Dónde se lo dices | Cómo puede oponerse |
| ------ | ------ | ------ | ------ |
| | | | |
| | | | |
| | | | |

*Plantilla 17.4. Tu revisión del modelo*

| Comprobación | Cada cuánto | Umbral de alarma | Qué haces si salta |
| ------ | ------ | ------ | ------ |
| Lift del decil de más riesgo con los meses nuevos | | | |
| Churn real frente al previsto por segmento | | | |
| Señales: ¿alguna ha cambiado de efecto? | | | |
| Grupo de control: ¿sigue siendo al azar y sin acción? | | | |
| Cambios de precio, producto o promoción desde la última revisión | | | |

## Errores frecuentes

- Retirar el grupo de control cuando la acción parece funcionar. Pierdes la forma de medir.
- Presentar una probabilidad como una certeza sobre una persona.
- Fiarse del modelo después de un cambio de precio sin revalidarlo.
- Subir listas a Customer Match o a Meta sin consentimiento.
- Copiar una política de privacidad genérica que no dice que calculas riesgos.
- Pedir consejo legal a la IA y aplicarlo sin revisión.

## Antes de seguir

- [ ] Tienes al menos un riesgo de cada familia con su mitigación y responsable.
- [ ] Cada uso del dato tiene su consentimiento y dónde se recoge.
- [ ] La política de privacidad explica el uso, y alguien con formación jurídica la ha revisado.
- [ ] Sabes qué decisiones no se automatizan.
- [ ] La revisión del modelo está en el calendario.
