from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer, PageBreak
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label

# 1. DATOS Y CONFIGURACIÓN INICIAL
guion = []
hojaEstilo = getSampleStyleSheet()

# Texto largo para demostrar flujo de texto en múltiples páginas
texto_largo = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""  * 2# Repetimos el texto para asegurar varias páginas

# Datos para una tabla simple
datos_tabla_simple = [
    ['Header 1', 'Header 2', 'Header 3'],
    ['Dato A1', 'Dato A2', 'Dato A3'],
    ['Dato B1', 'Dato B2', 'Dato B3'],
    ['Dato C1', 'Dato C2', 'Dato C3'],
]

# Datos para un gráfico de barras simple
datos_barras = [(10, 20, 30, 40, 50)]
etiquetas_barras = ['Ene', 'Feb', 'Mar', 'Abr', 'May']

# 2. CONFIGURACIÓN DE ELEMENTOS

# Estilo para el título del documento
estilo_titulo_doc = hojaEstilo['h1']
estilo_titulo_doc.alignment = 1
estilo_titulo_doc.textColor = colors.darkred

# Estilo para el cuerpo de texto
estilo_body = hojaEstilo['BodyText']
estilo_body.fontSize = 10
estilo_body.leading = 12 # Espaciado entre líneas

# Configuración de la tabla simple
tabla_simple = Table(datos_tabla_simple, colWidths=[100, 100, 100])
tabla_simple.setStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
])

# Configuración del gráfico de barras
d_barras = Drawing(400, 200)

titulo_barras = Label()
titulo_barras.setText("Ventas Mensuales")
titulo_barras.setOrigin(200, 180)
titulo_barras.fontName = 'Helvetica-Bold'
titulo_barras.fontSize = 12
d_barras.add(titulo_barras)

grafico_barras = VerticalBarChart()
grafico_barras.x = 50
grafico_barras.y = 50
grafico_barras.height = 100
grafico_barras.width = 300
grafico_barras.data = datos_barras
grafico_barras.valueAxis.valueMin = 0
grafico_barras.valueAxis.valueMax = 60
grafico_barras.valueAxis.valueStep = 10
grafico_barras.categoryAxis.categoryNames = etiquetas_barras
grafico_barras.groupSpacing = 10
grafico_barras.barSpacing = 2
d_barras.add(grafico_barras)

# 3. MONTAJE DEL GUION (FLUJO DEL DOCUMENTO)

guion.append(Paragraph("Ejemplo de Examen 2: Flujo de Texto y Múltiples Elementos", estilo_titulo_doc))
guion.append(Spacer(1, 20))

guion.append(Paragraph("Este documento demuestra la capacidad de ReportLab para manejar el flujo de texto en múltiples páginas, combinar elementos como tablas e imágenes, y presentar gráficos de manera efectiva.", estilo_body))
guion.append(Spacer(1, 10))

guion.append(Paragraph("Texto Extenso:", hojaEstilo['h2']))
guion.append(Spacer(1, 5))
guion.append(Paragraph(texto_largo, estilo_body))
guion.append(Spacer(1, 20))

# Añadir un salto de página para asegurar que el siguiente contenido aparezca en una nueva página
guion.append(PageBreak())

guion.append(Paragraph("Tabla de Datos Simple:", hojaEstilo['h2']))
guion.append(Spacer(1, 10))
guion.append(tabla_simple)
guion.append(Spacer(1, 20))

# Intento de cargar una imagen existente, con manejo de error
try:
    # Ajusta la ruta si es necesario para tu entorno
    imaxe_ejemplo = Image("../Imagenes/equis16x216.jpg", width=150, height=100)
    guion.append(Paragraph("Imagen de Ejemplo:", hojaEstilo['h2']))
    guion.append(Spacer(1, 10))
    guion.append(imaxe_ejemplo)
except Exception as e:
    guion.append(Paragraph(f"No se pudo cargar la imagen: equis16x216.jpg. Error: {e}", hojaEstilo['Error']))
guion.append(Spacer(1, 20))


guion.append(Paragraph("Gráfico de Ventas:", hojaEstilo['h2']))
guion.append(Spacer(1, 10))
guion.append(d_barras)
guion.append(Spacer(1, 20))

guion.append(Paragraph("Fin del Ejemplo 2.", estilo_body))

# 4. GENERACIÓN DEL PDF
doc = SimpleDocTemplate('TablasImagenesSimple.pdf', pagesize=A4, showBoundary=0)
doc.build(guion)
