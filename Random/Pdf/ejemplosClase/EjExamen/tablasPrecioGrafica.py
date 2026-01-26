from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer, PageBreak
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend

# 1. DATOS Y CONFIGURACIÓN INICIAL
guion = []
hojaEstilo = getSampleStyleSheet()

# Datos para la tabla de factura
datos_factura_cabecera = [
    ['FACTURA DETALLADA', '', '', ''],
    ['Empresa XYZ', '', '', 'Logo Aquí'],
    ['Dirección de la empresa', '', '', ''],
    ['Ciudad, País', '', '', ''],
    ['CIF/NIF: B12345678', '', 'Fecha:', '26/01/2026'],
    ['Teléfono: 123-456-789', '', 'Factura Nº:', '2026-001'],
    ['Email: info@empresa.com', '', '', '']
]

datos_factura_productos = [
    ['Descripción', 'Cantidad', 'Precio Unitario', 'Importe'],
    ['Servicio de Consultoría', '10', '75.00', '750.00'],
    ['Desarrollo de Software', '25', '120.00', '3000.00'],
    ['Licencia Anual', '1', '500.00', '500.00'],
    ['Soporte Técnico (horas)', '5', '60.00', '300.00'],
    ['', '', 'Subtotal:', '4550.00'],
    ['', '', 'IVA (21%):', '955.50'],
    ['', '', 'Total:', '5505.50']
]

# Datos para el gráfico de tarta
datos_tarta = [30, 20, 15, 35]
etiquetas_tarta = ['Consultoría', 'Desarrollo', 'Licencias', 'Soporte']
colores_tarta = [colors.blue, colors.green, colors.orange, colors.red]

# 2. CONFIGURACIÓN DE LA TABLA (OBJETOS PLATYPUS)
tabla_factura_cabecera = Table(datos_factura_cabecera, colWidths=[None, None, 80, 80])
tabla_factura_cabecera.setStyle([
    ('FONTSIZE', (0,0), (-1,0), 16),
    ('SPAN', (0,0), (-1,0)),
    ('ALIGN', (0,0), (-1,0), 'CENTER'),
    ('FONTSIZE', (0,1), (0,1), 12),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('ALIGN', (2,4), (2,6), 'RIGHT'),
    ('ALIGN', (3,4), (3,6), 'LEFT'),
    ('SPAN', (1,1), (2,1)),
    ('SPAN', (1,2), (2,2)),
    ('SPAN', (1,3), (2,3)),
])

tabla_factura_productos = Table(datos_factura_productos, colWidths=[200, 50, 70, 70])
tabla_factura_productos.setStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('BACKGROUND', (0,1), (-1,-3), colors.lightblue),
    ('ALIGN', (2,1), (-1,-3), 'RIGHT'), # Alinea cantidades y precios a la derecha
    ('ALIGN', (0, -3), (1, -1), 'RIGHT'), # Alinea etiquetas Subtotal, IVA, Total a la derecha
    ('BACKGROUND', (0,-3), (-1,-1), colors.lightgrey),
    ('FONTNAME', (0,-3), (-1,-1), 'Helvetica-Bold'),
    ('TEXTCOLOR', (0,-1), (-1,-1), colors.red),
    ('FONTSIZE', (0,-1), (-1,-1), 12),
    ('ALIGN', (2,-3), (-1,-1), 'RIGHT'), # Alinea valores Subtotal, IVA, Total a la derecha
])

# 3. CONFIGURACIÓN DEL GRÁFICO DE TARTA (OBJETOS GRAPHICS)
d_tarta = Drawing(400, 250)

# Título de la Gráfica
titulo_tarta = Label()
titulo_tarta.setText("Distribución de Servicios (Porcentaje)")
titulo_tarta.setOrigin(200, 240)
titulo_tarta.fontName = 'Helvetica-Bold'
titulo_tarta.fontSize = 14
d_tarta.add(titulo_tarta)

# Gráfico de Tarta
grafico_tarta = Pie()
grafico_tarta.x = 100
grafico_tarta.y = 50
grafico_tarta.width = 150
grafico_tarta.height = 150
grafico_tarta.data = datos_tarta
grafico_tarta.slices.strokeWidth = 0.5

# Asignar los colores a las rebanadas y preparar las etiquetas
for i, color in enumerate(colores_tarta):
    grafico_tarta.slices[i].fillColor = color
# La propiedad 'labels' del objeto Pie toma una lista de cadenas.
# No se establecen individualmente en grafico_tarta.slices[i].label.
# Si sideLabels está activado, ReportLab usa la lista 'labels' para mostrar.
grafico_tarta.labels = [f"{etiquetas_tarta[i]}: {datos_tarta[i]}%" for i in range(len(datos_tarta))]

grafico_tarta.sideLabels = 1
grafico_tarta.slices.fontName = 'Helvetica'
grafico_tarta.slices.fontSize = 8

d_tarta.add(grafico_tarta)

# Leyenda
leyenda_tarta = Legend()
leyenda_tarta.x = 280
leyenda_tarta.y = 150
leyenda_tarta.alignment = 'right'
leyenda_tarta.boxAnchor = 'nw'
leyenda_tarta.columnMaximum = 1
leyenda_tarta.fontName = 'Helvetica'
leyenda_tarta.fontSize = 9
leyenda_tarta.strokeWidth = 0.5
leyenda_tarta.strokeColor = colors.black
leyenda_tarta.deltax = 10
leyenda_tarta.deltay = 10
leyenda_tarta.autoXPadding = 5
leyenda_tarta.yGap = 2

leyenda_items = []
for i in range(len(datos_tarta)):
    leyenda_items.append((colores_tarta[i], f'{etiquetas_tarta[i]}'))
leyenda_tarta.colorNamePairs = leyenda_items

d_tarta.add(leyenda_tarta)

# 4. MONTAJE DEL GUION (FLUJO DEL DOCUMENTO)

# Título del documento
estilo_titulo = hojaEstilo['h1']
estilo_titulo.alignment = 1
estilo_titulo.textColor = colors.darkgreen
guion.append(Paragraph("Informe de Actividad y Facturación", estilo_titulo))
guion.append(Spacer(1, 0.2 * A4[1])) # Espacio

# Introducción
estilo_body = hojaEstilo['BodyText']
guion.append(Paragraph("A continuación se presenta un informe detallado de las actividades realizadas y la facturación correspondiente al periodo actual. Este documento incluye una factura detallada y una representación gráfica de la distribución de los servicios.", estilo_body))
guion.append(Spacer(1, 0.1 * A4[1])) # Espacio

# Título para la factura
estilo_subtitulo = hojaEstilo['h2']
estilo_subtitulo.alignment = 0
estilo_subtitulo.textColor = colors.black
guion.append(Paragraph("Detalle de Factura", estilo_subtitulo))
guion.append(Spacer(1, 10))

# Añadir la tabla de cabecera de factura
guion.append(tabla_factura_cabecera)
guion.append(Spacer(1, 5))

# Añadir la tabla de productos
guion.append(tabla_factura_productos)
guion.append(Spacer(1, 20))

# Título para el gráfico
guion.append(Paragraph("Distribución de Servicios por Categoría", estilo_subtitulo))
guion.append(Spacer(1, 10))

# Añadir el gráfico de tarta
guion.append(d_tarta)
guion.append(Spacer(1, 20))

# Conclusión
guion.append(Paragraph("Este informe proporciona una visión clara de la composición de nuestros servicios y su impacto en la facturación total.", estilo_body))
guion.append(Spacer(1, 0.1 * A4[1])) # Espacio

# Pie de página simple
# Definir un estilo personalizado para el pie de página
estilo_footer = hojaEstilo['Normal']
estilo_footer.fontSize = 8
estilo_footer.alignment = 1
guion.append(Paragraph("Generado por Empresa XYZ - Contacto: info@empresa.com", estilo_footer))


# 5. GENERACIÓN DEL PDF
doc = SimpleDocTemplate('TablasPrecioGrafica.pdf', pagesize=A4, showBoundary=0)
doc.build(guion)
