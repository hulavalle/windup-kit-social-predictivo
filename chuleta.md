# Chuleta · Analítica social y predictiva

Una página para consultar.

## AARRR: el mapa

| Etapa | Pregunta | Tienda (ecommerce) | Captación de leads |
| --- | --- | --- | --- |
| Adquisición | ¿De dónde llegan? | Sesión con UTM | Sesión con UTM |
| Activación | ¿Tienen una primera experiencia de valor? | Ficha, guía, carrito | Página de servicio, clic en el CTA |
| Retención | ¿Vuelven? | Segunda compra, renovación | El cliente sigue pidiendo |
| Recomendación | ¿Traen a otros? | Código de amigo, compartir | Un cliente recomienda a otro |
| Ingresos | ¿Pagan, y cuánto con el tiempo? | Compra, LTV | Lead → cliente → pedidos |

## UTMs de redes

- Todo en minúsculas, sin espacios ni tildes. Campaña `AAAA-MM_nombre`.
- `utm_source` = la red (`instagram`, `facebook`, `tiktok`, `linkedin`), nunca la herramienta.
- Orgánico: `utm_medium=social` → Organic Social. Anuncios: `utm_medium=paid_social` → Paid Social.
- Influencer: `instagram / social` con `utm_content` = nombre de la creadora.

## Fórmulas

| Qué | Fórmula |
| --- | --- |
| ROAS | Ingresos atribuidos / gasto en anuncios |
| ROI | (Ingresos atribuidos × margen − coste completo) / coste completo |
| MER | Ingresos totales / gasto total de marketing |
| Coste completo | Anuncios + influencers + horas × €/hora |
| Valor de un lead | Tasa de cierre × primer pedido (o valor anual) × margen |
| Owned Media Value | Impresiones orgánicas / 1.000 × CPM de paid social |
| Churn mensual | Bajas del mes / clientes activos al empezar el mes |
| Retención en el mes k | Activos en el mes k / tamaño de la cohorte |
| LTV histórico | Ingreso medio × vida media |
| LTV con churn | (Ingreso mensual × margen) / churn mensual |
| LTV esperado | Σ P(seguir activo en el mes k) × margen si sigue activo |
| LTV/CAC | LTV / coste de captar un cliente |

Ojo al doble conteo: en el LTV esperado, el margen es el de los clientes que siguen activos.

## Cohortes

- Cohorte = rasgo común + acción + momento.
- Matriz: filas = cohortes, columnas = meses desde el alta. Celdas sin llegar en blanco, no en cero.
- Curvas: mala (cae a cero), buena (se aplana), sonriente (vuelve a subir).
- Bruta: solo cuenta quien sigue sin interrupción. Neta: cuenta a quien vuelve, en su cohorte original.

## Churn y modelos

- Con contrato: la baja. Sin contrato: umbral de inactividad según el tiempo habitual entre pedidos.
- Solo valen señales que se conocen antes de predecir (nada de fecha de baja).
- Valida con meses guardados, no al azar. Mide el lift por deciles: el 10 % con más riesgo frente a la media.
- La exactitud engaña: si casi nadie se va, decir «nadie se va» ya acierta mucho.

## Del dato a la acción: APPA

1. **Analysis.** Dónde duele: cohortes, churn, síntoma frente a causa.
2. **Plan.** Hipótesis «Si…, entonces…», priorizada con ICE (impacto × confianza × facilidad, de 1 a 10).
3. **Practice.** La acción con grupo de control (holdout): una parte al azar no la recibe. Métrica primaria, contrapeso, tamaño de muestra, decisión escrita antes.
4. **Action.** Lanzar lo que funciona y vigilar que el efecto se mantiene.

Sin volumen para un test, implementación directa y seguimiento con la serie temporal.

## Analizar con IA en 4 pasos

1. Pregunta y decisión, antes de abrir los datos.
2. Datos con diccionario y sin datos personales.
3. Prompt: rol, datos, pregunta, formato, «calcula con código y enséñame fórmula y supuestos».
4. Verificar dos cifras a mano y preguntar qué no sabe.
