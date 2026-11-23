#!/usr/bin/env python3
"""Construye los tres documentos del cuaderno a partir de sus markdown.

- clase/ -> cuaderno-de-clase.docx: lo que se rellena en clase, un paso por página.
- plantilla/ecommerce/ -> plantilla-ecommerce.docx: versión completa para una tienda
  online. Ejemplo: la tienda de Café Fandango.
- plantilla/leadgen/ -> plantilla-leadgen.docx: versión completa para un negocio de
  captación de leads. Ejemplo: Fandango para cafeterías.

El markdown es la única fuente: edita los .md y vuelve a ejecutar este script.

Uso (desde la raíz del repositorio del kit):
	python3 -m venv .venv && .venv/bin/pip install python-docx    # una vez
	.venv/bin/python cuaderno/construir_docx.py [clase ...]

Sin argumentos construye los tres; con argumentos, solo esas carpetas (p. ej. «clase»).

Orden en cada carpeta: 00-indice.md, paso-*.md por nombre y 19-recursos.md.
El título de 00-indice.md da el título del documento y el texto del pie de página.

Markdown admitido:
- "# " título (en 00-indice.md, portada; en el resto, página nueva), "## " y "### ".
- El primer párrafo después de un "# " sale en un recuadro: es la línea de qué haces en el paso.
- Párrafos con **negrita**, *cursiva*, `código` y [texto](url).
- Listas "- ", "1. " y casillas "- [ ] ". Sangría de 3 espacios para un segundo nivel.
- Tablas con barras verticales. Una barra dentro de una celda se escribe "\\|".
  Si la fila separadora tiene guiones de distinta longitud ("| -- | -------- |"),
  esas longitudes fijan el ancho relativo de cada columna.
- Una línea "*Plantilla X. Título*" justo antes de una tabla la marca como plantilla
  para rellenar; "*Ejemplo X. Título*" la marca como ejemplo.
- Bloques de código entre ```.

Al terminar, el script abre cada .docx y comprueba que los títulos son "Paso 0." a
"Paso 18." en orden y después "Recursos", y que están todas las plantillas con sus
columnas y filas. Si falta algo, sale con código 1.
"""

import io
import re
import sys
import zipfile
from pathlib import Path

try:
	from docx import Document
	from docx.enum.table import WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT
	from docx.enum.text import WD_ALIGN_PARAGRAPH
	from docx.oxml import OxmlElement
	from docx.oxml.ns import qn
	from docx.shared import Cm, Pt, RGBColor
	from docx.table import Table
	from docx.text.paragraph import Paragraph
except ImportError:
	sys.exit("Falta python-docx. Instálalo con: python3 -m venv .venv && .venv/bin/pip install python-docx")

CARPETA = Path(__file__).resolve().parent
CUADERNOS = (
	("clase", "cuaderno-de-clase.docx"),
	("plantilla/ecommerce", "plantilla-ecommerce.docx"),
	("plantilla/leadgen", "plantilla-leadgen.docx"),
)
N_PASOS = 19
RECURSOS = "19-recursos.md"
TITULOS_ESPERADOS = [f"Paso {n}." for n in range(N_PASOS)] + ["Recursos"]

FUENTE = "Arial"
FUENTE_CODIGO = "Courier New"
ACENTO = "1E4D5C"
FONDO_CABECERA_EJEMPLO = "D5E3E7"
FONDO_EJEMPLO = "F1F6F7"
FONDO_ETIQUETA = "F2F2F2"
FONDO_CODIGO = "F4F4F4"
ANCHO_UTIL_CM = 17.0
ALTO_FILA_VACIA_CM = 0.85

PIE = re.compile(r"^\*((Plantilla|Ejemplo) ([0-9]+\.[0-9]+|[A-Z])\. .+)\*$")
TOKEN = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\)|\*[^*]+\*)")


# Lectura del markdown

def trozos(texto):
	"""Divide una línea en trozos (texto, estilo): '' normal, 'b' negrita, 'i' cursiva, 'c' código."""
	salida = []
	for parte in TOKEN.split(texto):
		if not parte:
			continue
		if parte.startswith("**") and parte.endswith("**"):
			salida.append((parte[2:-2], "b"))
		elif parte.startswith("`") and parte.endswith("`"):
			salida.append((parte[1:-1], "c"))
		elif parte.startswith("[") and parte.endswith(")"):
			m = re.match(r"\[([^\]]+)\]\(([^)]+)\)", parte)
			salida.append((f"{m.group(1)} ({m.group(2)})", ""))
		elif parte.startswith("*") and parte.endswith("*") and len(parte) > 2:
			salida.append((parte[1:-1], "i"))
		else:
			salida.append((parte, ""))
	return salida


def texto_plano(texto):
	return "".join(t for t, _ in trozos(texto))


def celdas(linea):
	interior = re.sub(r"^\||(?<!\\)\|$", "", linea.strip())
	return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", interior)]


def leer_tabla(lineas):
	filas = [celdas(l) for l in lineas]
	separador = filas[1] if len(filas) > 1 and all(re.fullmatch(r":?-+:?", c) for c in filas[1]) else None
	if separador:
		filas = [filas[0]] + filas[2:]
	n = len(filas[0])
	filas = [(f + [""] * n)[:n] for f in filas]
	pesos = None
	if separador:
		guiones = [len(c.strip(":")) for c in separador]
		if len(set(guiones)) > 1:
			pesos = guiones
	return filas, pesos


def leer_bloques(texto):
	lineas = texto.splitlines()
	bloques = []
	i = 0
	while i < len(lineas):
		linea = lineas[i]
		if not linea.strip():
			i += 1
			continue
		if linea.startswith("```"):
			j = i + 1
			codigo = []
			while j < len(lineas) and not lineas[j].startswith("```"):
				codigo.append(lineas[j])
				j += 1
			bloques.append({"tipo": "codigo", "lineas": codigo})
			i = j + 1
			continue
		m = re.match(r"^(#{1,3}) (.+)$", linea)
		if m:
			bloques.append({"tipo": "titulo", "nivel": len(m.group(1)), "texto": m.group(2).strip()})
			i += 1
			continue
		if linea.lstrip().startswith("|"):
			j = i
			while j < len(lineas) and lineas[j].lstrip().startswith("|"):
				j += 1
			filas, pesos = leer_tabla(lineas[i:j])
			bloques.append({"tipo": "tabla", "filas": filas, "pesos": pesos})
			i = j
			continue
		m = re.match(r"^(\s*)(- \[ \] |- |(\d+)\. )(.+)$", linea)
		if m:
			marca = "☐" if m.group(2) == "- [ ] " else ("•" if m.group(2) == "- " else f"{m.group(3)}.")
			bloques.append({"tipo": "lista", "nivel": len(m.group(1)) // 3, "marca": marca, "texto": m.group(4)})
			i += 1
			continue
		m = PIE.match(linea.strip())
		if m:
			bloques.append({"tipo": "pie", "texto": m.group(1), "plantilla": m.group(2) == "Plantilla"})
			i += 1
			continue
		parrafo = [linea.strip()]
		i += 1
		while i < len(lineas) and lineas[i].strip() and not re.match(r"^(#|\||```|\s*- |\s*\d+\. )", lineas[i]):
			parrafo.append(lineas[i].strip())
			i += 1
		bloques.append({"tipo": "parrafo", "texto": " ".join(parrafo)})
	return bloques


def leer_cuaderno(carpeta):
	archivos = [carpeta / "00-indice.md"] + sorted(carpeta.glob("paso-*.md")) + [carpeta / RECURSOS]
	return [(a, leer_bloques(a.read_text(encoding="utf-8"))) for a in archivos]


# Utilidades de formato

def sombrear(elemento_pr, color):
	shd = OxmlElement("w:shd")
	shd.set(qn("w:val"), "clear")
	shd.set(qn("w:color"), "auto")
	shd.set(qn("w:fill"), color)
	elemento_pr.append(shd)


def borde_izquierdo(parrafo, color, grosor=18):
	ppr = parrafo._p.get_or_add_pPr()
	bordes = OxmlElement("w:pBdr")
	izq = OxmlElement("w:left")
	izq.set(qn("w:val"), "single")
	izq.set(qn("w:sz"), str(grosor))
	izq.set(qn("w:space"), "6")
	izq.set(qn("w:color"), color)
	bordes.append(izq)
	ppr.append(bordes)


def fuente_estilo(estilo, nombre, tam, negrita=False, color=None):
	estilo.font.name = nombre
	estilo.font.size = Pt(tam)
	estilo.font.bold = negrita
	if color:
		estilo.font.color.rgb = RGBColor.from_string(color)
	rpr = estilo.element.get_or_add_rPr()
	rfonts = rpr.find(qn("w:rFonts"))
	if rfonts is None:
		rfonts = OxmlElement("w:rFonts")
		rpr.append(rfonts)
	for clave in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
		rfonts.set(qn(clave), nombre)
	for tema in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
		rfonts.attrib.pop(qn(tema), None)


def escribir(parrafo, texto, tam=None):
	for trozo, estilo in trozos(texto):
		run = parrafo.add_run(trozo)
		if estilo == "b":
			run.bold = True
		elif estilo == "i":
			run.italic = True
		elif estilo == "c":
			run.font.name = FUENTE_CODIGO
			run.font.size = Pt((tam or 10) - (0.5 if tam else 1))
		if tam and estilo != "c":
			run.font.size = Pt(tam)


def preparar_documento(titulo):
	doc = Document()
	seccion = doc.sections[0]
	seccion.page_width, seccion.page_height = Cm(21), Cm(29.7)
	seccion.left_margin, seccion.right_margin = Cm(2), Cm(2)
	seccion.top_margin, seccion.bottom_margin = Cm(2), Cm(1.8)

	estilos = doc.styles
	normal = estilos["Normal"]
	fuente_estilo(normal, FUENTE, 10)
	normal.paragraph_format.space_after = Pt(5)
	normal.paragraph_format.line_spacing = 1.15
	idioma = OxmlElement("w:lang")
	idioma.set(qn("w:val"), "es-ES")
	normal.element.get_or_add_rPr().append(idioma)

	fuente_estilo(estilos["Title"], FUENTE, 28, True, ACENTO)
	estilos["Title"].paragraph_format.space_after = Pt(12)
	for nombre, tam, antes, despues in (("Heading 1", 18, 0, 10), ("Heading 2", 13, 14, 4), ("Heading 3", 11, 10, 3)):
		estilo = estilos[nombre]
		fuente_estilo(estilo, FUENTE, tam, True, ACENTO)
		estilo.font.italic = False
		estilo.paragraph_format.space_before = Pt(antes)
		estilo.paragraph_format.space_after = Pt(despues)
		estilo.paragraph_format.keep_with_next = True

	pie = estilos.add_style("Pie de tabla", 1)
	pie.base_style = normal
	fuente_estilo(pie, FUENTE, 9, True, ACENTO)
	pie.paragraph_format.space_before = Pt(10)
	pie.paragraph_format.space_after = Pt(3)
	pie.paragraph_format.keep_with_next = True

	codigo = estilos.add_style("Codigo", 1)
	codigo.base_style = normal
	fuente_estilo(codigo, FUENTE_CODIGO, 8.5)
	codigo.paragraph_format.space_after = Pt(0)
	codigo.paragraph_format.line_spacing = 1.0
	sombrear(codigo.element.get_or_add_pPr(), FONDO_CODIGO)

	parrafo_pie = seccion.footer.paragraphs[0]
	parrafo_pie.alignment = WD_ALIGN_PARAGRAPH.RIGHT
	run = parrafo_pie.add_run(f"{titulo} · ")
	run.font.size = Pt(8)
	run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
	campo = OxmlElement("w:fldSimple")
	campo.set(qn("w:instr"), "PAGE")
	r = OxmlElement("w:r")
	rpr = OxmlElement("w:rPr")
	sz = OxmlElement("w:sz")
	sz.set(qn("w:val"), "16")
	rpr.append(sz)
	r.append(rpr)
	t = OxmlElement("w:t")
	t.text = "1"
	r.append(t)
	campo.append(r)
	parrafo_pie._p.append(campo)

	doc.core_properties.title = titulo
	doc.core_properties.subject = "Analítica social y predictiva · Máster Técnico en Marketing Digital & IA"
	doc.core_properties.language = "es-ES"
	return doc


# Tablas

def anchos_columnas(filas, pesos_fijos, plantilla):
	n = len(filas[0])
	if pesos_fijos:
		total = sum(pesos_fijos)
		return [p / total * ANCHO_UTIL_CM for p in pesos_fijos]
	pesos, minimos = [], []
	for c in range(n):
		textos = [texto_plano(f[c]) for f in filas]
		cuerpo = [t for t in textos[1:] if t]
		media = sum(map(len, cuerpo)) / len(cuerpo) if cuerpo else 0
		palabra_larga = max((len(p) for t in textos for p in t.split()), default=2)
		if plantilla and not cuerpo:
			peso = max(len(textos[0]), 20)
		elif plantilla:
			peso = min(max(media, len(textos[0]) * 0.7), 22)
		else:
			peso = max(media, len(textos[0]) * 0.7)
		pesos.append(max(peso, 3))
		minimos.append(min(max(1.0, palabra_larga * 0.2 + 0.45), ANCHO_UTIL_CM * 0.4))
	objetivo = [p / sum(pesos) * ANCHO_UTIL_CM for p in pesos]
	anchos = [max(o, m) for o, m in zip(objetivo, minimos)]
	exceso = sum(anchos) - ANCHO_UTIL_CM
	holgura = sum(a - m for a, m in zip(anchos, minimos))
	if exceso > 0 and holgura >= exceso:
		anchos = [a - exceso * (a - m) / holgura for a, m in zip(anchos, minimos)]
	elif exceso > 0:
		anchos = [a * ANCHO_UTIL_CM / sum(anchos) for a in anchos]
	return anchos


def marcar_fila(fila, cabecera):
	trpr = fila._tr.get_or_add_trPr()
	no_partir = OxmlElement("w:cantSplit")
	trpr.append(no_partir)
	if cabecera:
		repetir = OxmlElement("w:tblHeader")
		trpr.append(repetir)


def poner_tabla(doc, filas, pesos, plantilla):
	ncols = len(filas[0])
	junta = plantilla and len(filas) <= 15
	tam = 8.5 if ncols >= 6 else 9
	tabla = doc.add_table(rows=len(filas), cols=ncols)
	tabla.style = "Table Grid"
	tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
	tabla.autofit = False
	tblpr = tabla._tbl.tblPr
	disposicion = OxmlElement("w:tblLayout")
	disposicion.set(qn("w:type"), "fixed")
	tblpr.append(disposicion)

	anchos = anchos_columnas(filas, pesos, plantilla)
	for c, ancho in enumerate(anchos):
		tabla.columns[c].width = Cm(ancho)

	for r, datos in enumerate(filas):
		fila = tabla.rows[r]
		marcar_fila(fila, r == 0)
		if plantilla and r > 0 and any(not d for d in datos):
			fila.height = Cm(ALTO_FILA_VACIA_CM)
			fila.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
		for c, dato in enumerate(datos):
			celda = fila.cells[c]
			celda.width = Cm(anchos[c])
			parrafo = celda.paragraphs[0]
			parrafo.paragraph_format.space_after = Pt(1)
			parrafo.paragraph_format.line_spacing = 1.0
			parrafo.paragraph_format.keep_with_next = junta and r < len(filas) - 1
			escribir(parrafo, dato, tam)
			tcpr = celda._tc.get_or_add_tcPr()
			if r == 0:
				for run in parrafo.runs:
					run.bold = True
					if plantilla:
						run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
				sombrear(tcpr, ACENTO if plantilla else FONDO_CABECERA_EJEMPLO)
			elif not plantilla:
				sombrear(tcpr, FONDO_EJEMPLO)
			elif dato:
				sombrear(tcpr, FONDO_ETIQUETA)
	doc.add_paragraph().paragraph_format.space_after = Pt(2)


# Construcción

def construir(cuaderno, salida):
	titulo = texto_plano(cuaderno[0][1][0]["texto"])
	doc = preparar_documento(titulo)
	esperado = {"titulos": [], "plantillas": []}
	pie_pendiente = None
	for archivo, bloques in cuaderno:
		es_indice = archivo.name.startswith("00-")
		for n, bloque in enumerate(bloques):
			tipo = bloque["tipo"]
			if tipo == "titulo":
				texto = texto_plano(bloque["texto"])
				if bloque["nivel"] == 1 and es_indice:
					doc.add_paragraph(texto, style="Title")
				elif bloque["nivel"] == 1:
					p = doc.add_paragraph(texto, style="Heading 1")
					p.paragraph_format.page_break_before = True
					esperado["titulos"].append(texto)
				else:
					doc.add_paragraph(texto, style=f"Heading {bloque['nivel']}")
			elif tipo == "parrafo":
				p = doc.add_paragraph()
				escribir(p, bloque["texto"])
				anterior = bloques[n - 1] if n else None
				if not es_indice and anterior and anterior["tipo"] == "titulo" and anterior["nivel"] == 1:
					sombrear(p._p.get_or_add_pPr(), FONDO_EJEMPLO)
					borde_izquierdo(p, ACENTO)
					p.paragraph_format.space_after = Pt(10)
			elif tipo == "lista":
				p = doc.add_paragraph()
				izquierda = 0.7 + 0.6 * bloque["nivel"]
				p.paragraph_format.left_indent = Cm(izquierda)
				p.paragraph_format.first_line_indent = Cm(-0.55)
				p.paragraph_format.tab_stops.add_tab_stop(Cm(izquierda))
				p.paragraph_format.space_after = Pt(3)
				p.paragraph_format.keep_with_next = n + 1 < len(bloques) and bloques[n + 1]["tipo"] == "lista"
				p.add_run(f"{bloque['marca']}\t")
				escribir(p, bloque["texto"])
			elif tipo == "codigo":
				for linea in bloque["lineas"] or [""]:
					p = doc.add_paragraph(style="Codigo")
					p.add_run(linea)
				doc.add_paragraph().paragraph_format.space_after = Pt(2)
			elif tipo == "pie":
				doc.add_paragraph(texto_plano(bloque["texto"]), style="Pie de tabla")
				pie_pendiente = bloque
				continue
			elif tipo == "tabla":
				plantilla = bool(pie_pendiente and pie_pendiente["plantilla"])
				poner_tabla(doc, bloque["filas"], bloque["pesos"], plantilla)
				if plantilla:
					esperado["plantillas"].append({
						"pie": texto_plano(pie_pendiente["texto"]),
						"cabecera": [texto_plano(c) for c in bloque["filas"][0]],
						"filas": len(bloque["filas"]),
					})
			if pie_pendiente and tipo != "tabla":
				sys.exit(f"{archivo.name}: el pie «{pie_pendiente['texto']}» no va seguido de una tabla")
			pie_pendiente = None
	guardar_estable(doc, salida)
	return esperado


def guardar_estable(doc, salida):
	"""Guarda con fecha fija dentro del zip: el mismo markdown da los mismos bytes."""
	bruto = io.BytesIO()
	doc.save(bruto)
	with zipfile.ZipFile(bruto) as origen, zipfile.ZipFile(salida, "w") as destino:
		for item in origen.infolist():
			destino.writestr(zipfile.ZipInfo(item.filename, (2026, 1, 1, 0, 0, 0)), origen.read(item.filename), zipfile.ZIP_DEFLATED)


def comprobar(esperado, salida):
	doc = Document(salida)
	elementos = []
	for hijo in doc.element.body.iterchildren():
		if hijo.tag == qn("w:p"):
			elementos.append(Paragraph(hijo, doc))
		elif hijo.tag == qn("w:tbl"):
			elementos.append(Table(hijo, doc))
	titulos = [e.text for e in elementos if isinstance(e, Paragraph) and e.style.name == "Heading 1"]
	errores = [f"falta el título «{t}»" for t in esperado["titulos"] if t not in titulos]
	if len(titulos) != len(TITULOS_ESPERADOS) or not all(t.startswith(e) for t, e in zip(titulos, TITULOS_ESPERADOS)):
		errores.append(f"los títulos deben ser {TITULOS_ESPERADOS} en orden, y son {titulos}")
	for plantilla in esperado["plantillas"]:
		posiciones = [i for i, e in enumerate(elementos) if isinstance(e, Paragraph) and e.text == plantilla["pie"]]
		if not posiciones:
			errores.append(f"falta el pie «{plantilla['pie']}»")
			continue
		siguiente = elementos[posiciones[0] + 1] if posiciones[0] + 1 < len(elementos) else None
		if not isinstance(siguiente, Table):
			errores.append(f"«{plantilla['pie']}» no va seguido de una tabla")
			continue
		cabecera = [c.text for c in siguiente.rows[0].cells]
		if cabecera != plantilla["cabecera"]:
			errores.append(f"«{plantilla['pie']}»: cabecera {cabecera}, se esperaba {plantilla['cabecera']}")
		if len(siguiente.rows) != plantilla["filas"]:
			errores.append(f"«{plantilla['pie']}»: {len(siguiente.rows)} filas, se esperaban {plantilla['filas']}")
	return titulos, errores


def main():
	fallos = 0
	elegidas = sys.argv[1:]
	for carpeta, nombre in CUADERNOS:
		if elegidas and carpeta not in elegidas:
			continue
		salida = CARPETA / nombre
		esperado = construir(leer_cuaderno(CARPETA / carpeta), salida)
		titulos, errores = comprobar(esperado, salida)
		print(f"{nombre}: {len(titulos)} títulos, {len(esperado['plantillas'])} plantillas")
		for t in titulos:
			print(f"  {t}")
		for e in errores:
			print(f"ERROR: {e}")
		fallos += len(errores)
	if fallos:
		sys.exit(1)
	print("Comprobación: los .docx tienen todos los pasos, Recursos y todas las plantillas")


if __name__ == "__main__":
	main()
