# Sesión 1 · Bucle 2 · Auditoría de UTMs

**Pregunta:** ¿qué enlaces de la marca no llegan a GA4 con su red y su canal correctos?
**Adjunta:** `utms_auditoria.csv` y `diccionario.md`.

Busca tú cuatro a ojo; después la IA audita los veinte y comparáis.

```
Eres analista de marketing digital y conoces la agrupación de canales predeterminada de GA4.

Te adjunto utms_auditoria.csv (enlaces publicados por una tienda de café) y su diccionario.
Convención de la marca: todo en minúsculas, sin espacios ni tildes; utm_source es la red
(instagram, facebook, tiktok, linkedin, newsletter), nunca la herramienta; orgánico con
utm_medium=social; anuncios con utm_medium=paid_social; utm_campaign con el formato
AAAA-MM_nombre.

Para cada enlace:
1. Di si cumple la convención y, si no, qué falla.
2. Di en qué grupo de canales de GA4 caería tal como está y en cuál debería caer.
3. Propón el enlace corregido.

Devuélvelo en una tabla: id_enlace, error, canal tal como está, canal correcto, corrección.
Revisa los enlaces uno por uno; no resumas.
```

**Comprueba:** abre en tu hoja dos enlaces que la IA marque como correctos y dos que marque como erróneos y revísalos tú. ¿Se le ha escapado alguno? ¿Ha inventado alguno?

**Errores típicos de la IA:** dar por buena una fuente que es una herramienta intermedia y no la red de origen, o no ver un espacio codificado en la URL (`%20`).
