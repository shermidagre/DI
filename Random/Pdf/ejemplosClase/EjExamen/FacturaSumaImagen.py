from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer, PageBreak, KeepTogether
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend

# 1. DATOS Y CONFIGURACIÓN INICIAL
guion = []
hojaEstilo = getSampleStyleSheet()

# --- Datos de la Empresa y Factura ---
nombre_empresa = "Soluciones Digitales S.A."
direccion_empresa = "Av. Innovación, 789"
ciudad_pais_empresa = "Future City, España"
cif_nif_empresa = "A-12345678"
telefono_empresa = "+34 986 789 012"
email_empresa = "info@solucionesdigitales.com"
logo_path = "../Imagenes/box-pixilart.png"

fecha_emision = "26/01/2026"
numero_factura = "SD-2026-002"

cliente_nombre = "Corporación Global S.L."
cliente_referencia = "Ref: Proy. Alpha"

# --- Datos de Productos/Servicios en la Factura ---
productos = [
    {"item": "Diseño UX/UI Plataforma", "horas": 80, "tarifa_hora": 45.00},
    {"item": "Desarrollo Backend API", "horas": 120, "tarifa_hora": 60.00},
    {"item": "Integración Frontend", "horas": 100, "tarifa_hora": 55.00},
    {"item": "Pruebas y QA", "horas": 40, "tarifa_hora": 40.00},
]

# Calcular importes
for p in productos:
    p["importe"] = p["horas"] * p["tarifa_hora"]

subtotal = sum(p["importe"] for p in productos)
iva_porcentaje = 0.21
iva_total = subtotal * iva_porcentaje
total_factura = subtotal + iva_total

# --- Datos para el Gráfico (derivados de los productos) ---
datos_grafico_tarta = [p["importe"] for p in productos]
etiquetas_grafico_tarta = [f"{p['item']} ({p['importe']:.2f}€)" for p in productos]
colores_tarta_dinamico = [colors.blue, colors.green, colors.orange, colors.purple, colors.red, colors.pink]


# 2. CONFIGURACIÓN DE ELEMENTOS PLATYPUS Y GRAPHICS

# --- Encabezado General ---
# Usamos una tabla para posicionar el logo y la información de la empresa
cabecera_data = [
    [Image(logo_path, width=70, height=70), Paragraph(f"<font size=18 color=darkred><b>{nombre_empresa}</b></font><br/>{direccion_empresa}<br/>{ciudad_pais_empresa}<br/>CIF/NIF: {cif_nif_empresa}", hojaEstilo['Normal'])],
]
table_header = Table(cabecera_data, colWidths=[100, 400])
table_header.setStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('ALIGN', (0,0), (0,0), 'LEFT'),
    ('ALIGN', (1,0), (1,0), 'RIGHT'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
])

# --- Información de Factura y Cliente (en dos columnas) ---
fact_info_data = [
    [Paragraph("<b>FACTURA</b>", hojaEstilo['h2']), Paragraph(f"<b>Nº FACTURA:</b> {numero_factura}<br/><b>FECHA:</b> {fecha_emision}", hojaEstilo['Normal'])],
    [Paragraph(f"<b>CLIENTE:</b><br/>{cliente_nombre}<br/>{cliente_referencia}", hojaEstilo['Normal']), ''],
]
table_fact_client_info = Table(fact_info_data, colWidths=[250, 250])
table_fact_client_info.setStyle([
    ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BACKGROUND', (0,0), (0,0), colors.yellow),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
])

# --- Tabla de Detalles de Productos/Servicios ---
tabla_detalle_data = [
    [Paragraph("<b>Concepto</b>", hojaEstilo['Normal']), Paragraph("<b>Horas</b>", hojaEstilo['Normal']), Paragraph("<b>Tarifa/Hr</b>", hojaEstilo['Normal']), Paragraph("<b>Importe</b>", hojaEstilo['Normal'])]
]
for p in productos:
    tabla_detalle_data.append([p["item"], str(p["horas"]), f"{p['tarifa_hora']:.2f} €", f"{p['importe']:.2f} €"])

# Añadir totales con estilos específicos
tabla_detalle_data.append(['', '', Paragraph("<b>Subtotal:</b>", hojaEstilo['Normal']), f"{subtotal:.2f} €"])
tabla_detalle_data.append(['', '', Paragraph(f"<b>IVA ({int(iva_porcentaje*100)}%):</b>", hojaEstilo['Normal']), f"{iva_total:.2f} €"])
tabla_detalle_data.append(['', '', Paragraph("<b>TOTAL A PAGAR:</b>", hojaEstilo['Normal']), Paragraph(f"<font color=red size=14><b>{total_factura:.2f} €</b></font>", hojaEstilo['Normal'])])


table_detalle_productos = Table(tabla_detalle_data, colWidths=[280, 70, 70, 80])
table_detalle_productos.setStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.darkcyan),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('ALIGN', (1,1), (-1,-4), 'RIGHT'), # Horas, Tarifa, Importe
    ('BACKGROUND', (0,1), (-1,-4), colors.lightcyan),
    ('ALIGN', (2,-3), (2,-1), 'RIGHT'), # Etiquetas Subtotal, IVA, Total
    ('ALIGN', (3,-3), (3,-1), 'RIGHT'), # Valores Subtotal, IVA, Total
    ('FONTNAME', (2,-3), (2,-1), 'Helvetica-Bold'),
    ('BACKGROUND', (2,-1), (3,-1), colors.lightyellow), # Fondo Total
])

# --- Gráfico de Tarta de Distribución de Ingresos ---
d_ingresos_pie = Drawing(400, 250)

# Título del gráfico
titulo_pie = Label()
titulo_pie.setText("Distribución de Ingresos por Servicio")
titulo_pie.setOrigin(200, 240)
titulo_pie.fontName = 'Helvetica-Bold'
titulo_pie.fontSize = 14
d_ingresos_pie.add(titulo_pie)

# Gráfico de Tarta
grafico_pie = Pie()
grafico_pie.x = 100
grafico_pie.y = 50
grafico_pie.width = 150
grafico_pie.height = 150
grafico_pie.data = datos_grafico_tarta
grafico_pie.slices.strokeWidth = 0.5

# Asignar colores a las rebanadas y preparar las etiquetas
for i, data_val in enumerate(datos_grafico_tarta):
    grafico_pie.slices[i].fillColor = colores_tarta_dinamico[i % len(colores_tarta_dinamico)]
# La propiedad 'labels' del objeto Pie toma una lista de cadenas.
# No se establecen individualmente en grafico_pie.slices[i].label.
# Si sideLabels está activado, ReportLab usa la lista 'labels' para mostrar.
grafico_pie.labels = [f"{etiquetas_grafico_tarta[i]}" for i in range(len(datos_grafico_tarta))]
# Establecer el estilo de fuente y tamaño para las etiquetas generadas por sideLabels
grafico_pie.slices.fontName = 'Helvetica'
grafico_pie.slices.fontSize = 8

d_ingresos_pie.add(grafico_pie)

# Leyenda para el gráfico de tarta
leyenda_pie = Legend()
leyenda_pie.x = 280
leyenda_pie.y = 150
leyenda_pie.alignment = 'right'
leyenda_pie.boxAnchor = 'nw'
leyenda_pie.columnMaximum = 1
leyenda_pie.fontName = 'Helvetica'
leyenda_pie.fontSize = 9
leyenda_pie.strokeWidth = 0.5
leyenda_pie.strokeColor = colors.black
leyenda_pie.deltax = 10
leyenda_pie.deltay = 10
leyenda_pie.autoXPadding = 5
leyenda_pie.yGap = 2

leyenda_items_pie = []
for i in range(len(datos_grafico_tarta)):
    leyenda_items_pie.append((colores_tarta_dinamico[i % len(colores_tarta_dinamico)], etiquetas_grafico_tarta[i]))
leyenda_pie.colorNamePairs = leyenda_items_pie

d_ingresos_pie.add(leyenda_pie)


# 3. MONTAJE DEL GUION (FLUJO DEL DOCUMENTO)

guion.append(table_header)
guion.append(Spacer(1, 20))

guion.append(table_fact_client_info)
guion.append(Spacer(1, 15))

# Usar KeepTogether para la tabla de productos y su título
guion.append(KeepTogether([
    Paragraph("<b>DETALLE DE SERVICIOS PRESTADOS</b>", hojaEstilo['h3']),
    Spacer(1, 5),
    table_detalle_productos
]))
guion.append(Spacer(1, 30))

guion.append(Paragraph("<b>ANÁLISIS DE INGRESOS</b>", hojaEstilo['h3']))
guion.append(Spacer(1, 10))
guion.append(Paragraph("La siguiente gráfica muestra la distribución porcentual de los ingresos generados por cada tipo de servicio o producto.", hojaEstilo['BodyText']))
guion.append(Spacer(1, 15))

guion.append(d_ingresos_pie)
guion.append(Spacer(1, 40))

guion.append(Paragraph("Gracias por su confianza en Soluciones Digitales S.A.", hojaEstilo['Italic']))
guion.append(Spacer(1, 10))

# Pie de página
estilo_footer = hojaEstilo['Normal']
estilo_footer.fontSize = 8
estilo_footer.alignment = 1
guion.append(Paragraph(f"{nombre_empresa} - {email_empresa} - Página 1 de 1", estilo_footer))


# 4. GENERACIÓN DEL PDF
doc = SimpleDocTemplate('ejemplo_examen4.pdf', pagesize=A4, showBoundary=0)
doc.build(guion)