from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer, PageBreak
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend

# 1. DATOS Y CONFIGURACIÓN INICIAL
guion = []
hojaEstilo = getSampleStyleSheet()

# --- Datos de la Empresa y Factura ---
nombre_empresa = "Innovaciones Tecnológicas S.L."
direccion_empresa = "Calle Ficticia, 123"
ciudad_pais_empresa = "Technocity, España"
cif_nif_empresa = "B-87654321"
telefono_empresa = "+34 981 123 456"
email_empresa = "contacto@innovaciones.es"
logo_path = "../Imagenes/equis16x216.jpg"

fecha_emision = "26/01/2026"
numero_factura = "IT-2026-001"

cliente_nombre = "Cliente Ejemplar S.A."
cliente_direccion = "Avenida del Saber, 45"
cliente_ciudad = "Conocimiento, España"

# --- Datos de Productos/Servicios en la Factura ---
productos = [
    {"descripcion": "Desarrollo Web Personalizado", "cantidad": 1, "precio_unitario": 1500.00},
    {"descripcion": "Mantenimiento Servidor (12 meses)", "cantidad": 1, "precio_unitario": 600.00},
    {"descripcion": "Licencia Software X (anual)", "cantidad": 3, "precio_unitario": 120.00},
    {"descripcion": "Consultoría IT (horas)", "cantidad": 8, "precio_unitario": 75.00},
]

# Calcular importes
for p in productos:
    p["importe"] = p["cantidad"] * p["precio_unitario"]

subtotal = sum(p["importe"] for p in productos)
iva_porcentaje = 0.21
iva_total = subtotal * iva_porcentaje
total_factura = subtotal + iva_total

# --- Datos para el Gráfico (derivados de los productos) ---
datos_grafico_ventas = []
etiquetas_grafico_ventas = []
for p in productos:
    datos_grafico_ventas.append(p["importe"])
    etiquetas_grafico_ventas.append(p["descripcion"])

# Ajustar datos para el gráfico de barras: cada valor como su propia serie para permitir colores individuales
datos_barras_final = []
for importe in datos_grafico_ventas:
    datos_barras_final.append((importe,))


# 2. CONFIGURACIÓN DE ELEMENTOS PLATYPUS Y GRAPHICS

# --- Encabezado de la Factura ---
cabecera_factura_data = [
    [Paragraph(f"<font size=16 color=darkblue><b>{nombre_empresa}</b></font>", hojaEstilo['Normal']), '', Image(logo_path, width=50, height=50)],
    [direccion_empresa, '', ''],
    [ciudad_pais_empresa, '', ''],
    [f"CIF/NIF: {cif_nif_empresa}", '', ''],
    [f"Teléfono: {telefono_empresa}", '', f"Fecha: {fecha_emision}"],
    [f"Email: {email_empresa}", '', f"Factura Nº: {numero_factura}"],
]

table_cabecera = Table(cabecera_factura_data, colWidths=[200, 150, 100])
table_cabecera.setStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('ALIGN', (2,0), (2,0), 'RIGHT'), # Logo a la derecha
    ('SPAN', (0,0), (1,0)), # Nombre empresa
    ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('GRID', (0,0), (-1,-1), 0.25, colors.lightgrey),
    ('ALIGN', (2,4), (2,5), 'RIGHT'), # Fecha y Nº Factura
])

# --- Datos del Cliente ---
datos_cliente = [
    [Paragraph("<b>FACTURAR A:</b>", hojaEstilo['Normal'])],
    [cliente_nombre],
    [cliente_direccion],
    [cliente_ciudad]
]
table_cliente = Table(datos_cliente, colWidths=[250])
table_cliente.setStyle([
    ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
    ('BACKGROUND', (0,0), (0,0), colors.lightgreen),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ('GRID', (0,0), (-1,-1), 0.25, colors.lightgrey),
])

# --- Tabla de Productos/Servicios ---
tabla_productos_data = [["Descripción", "Cantidad", "P. Unitario", "Importe"]]
for p in productos:
    tabla_productos_data.append([p["descripcion"], str(p["cantidad"]), f"{p['precio_unitario']:.2f} €", f"{p['importe']:.2f} €"])
tabla_productos_data.append(["", "", "Subtotal:", f"{subtotal:.2f} €"])
tabla_productos_data.append(["", "", f"IVA ({int(iva_porcentaje*100)}%):", f"{iva_total:.2f} €"])
tabla_productos_data.append(["", "", "TOTAL:", f"{total_factura:.2f} €"])

table_productos = Table(tabla_productos_data, colWidths=[250, 60, 80, 80])
table_productos.setStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ('BACKGROUND', (0,1), (-1,-4), colors.lightblue), # Filas de productos
    ('ALIGN', (1,1), (-1,-4), 'RIGHT'), # Alinea datos numericos de productos
    ('ALIGN', (2,-3), (2,-1), 'RIGHT'), # Etiquetas Subtotal, IVA, Total
    ('ALIGN', (3,-3), (3,-1), 'RIGHT'), # Valores Subtotal, IVA, Total
    ('FONTNAME', (2,-3), (2,-1), 'Helvetica-Bold'),
    ('FONTNAME', (3,-3), (3,-1), 'Helvetica-Bold'),
    ('BACKGROUND', (0,-3), (-1,-1), colors.lightgrey),
    ('TEXTCOLOR', (3,-1), (3,-1), colors.red), # Total en rojo
    ('FONTSIZE', (3,-1), (3,-1), 12),
])

# --- Gráfico de Ventas por Concepto ---
d_ventas_chart = Drawing(400, 250)

# Título del gráfico
titulo_chart = Label()
titulo_chart.setText("Distribución de Ingresos por Concepto")
titulo_chart.setOrigin(200, 240)
titulo_chart.fontName = 'Helvetica-Bold'
titulo_chart.fontSize = 14
d_ventas_chart.add(titulo_chart)

# Gráfico de barras
grafico_barras_ventas = VerticalBarChart()
grafico_barras_ventas.x = 50
grafico_barras_ventas.y = 50
grafico_barras_ventas.height = 150
grafico_barras_ventas.width = 350
grafico_barras_ventas.data = datos_barras_final # Usa los datos derivados
grafico_barras_ventas.valueAxis.valueMin = 0
grafico_barras_ventas.valueAxis.valueMax = max(datos_grafico_ventas) * 1.2 # Dinámico
grafico_barras_ventas.valueAxis.valueStep = (max(datos_grafico_ventas) * 1.2) / 5
grafico_barras_ventas.categoryAxis.categoryNames = etiquetas_grafico_ventas
grafico_barras_ventas.categoryAxis.labels.boxAnchor = 'ne'
grafico_barras_ventas.categoryAxis.labels.dx = 8
grafico_barras_ventas.categoryAxis.labels.dy = -10
grafico_barras_ventas.categoryAxis.labels.angle = 30
grafico_barras_ventas.barSpacing = 5

# Colores dinámicos para las barras
colores_barras = [colors.blue, colors.green, colors.orange, colors.purple, colors.red]
# Itera usando el número de series que hemos creado en datos_barras_final
for i in range(len(datos_barras_final)):
    # Accede directamente a las propiedades de la barra para cada "serie"
    grafico_barras_ventas.bars[i].fillColor = colores_barras[i % len(colores_barras)] # Ciclar colores

d_ventas_chart.add(grafico_barras_ventas)

# Leyenda (opcional, si hay múltiples series en el gráfico de barras)
# leyenda_barras = Legend()
# ... (configurar leyenda si es necesario)
# d_ventas_chart.add(leyenda_barras)

# 3. MONTAJE DEL GUION (FLUJO DEL DOCUMENTO)

# Título Principal del Documento
estilo_titulo_doc = hojaEstilo['h1']
estilo_titulo_doc.alignment = 1
estilo_titulo_doc.textColor = colors.darkblue
guion.append(Paragraph("INFORME DE FACTURACIÓN Y ANÁLISIS DE VENTAS", estilo_titulo_doc))
guion.append(Spacer(1, 20))

# Sección de Factura
guion.append(table_cabecera)
guion.append(Spacer(1, 15))
guion.append(table_cliente)
guion.append(Spacer(1, 15))
guion.append(table_productos)
guion.append(Spacer(1, 30))

# Introducción al análisis de ventas
estilo_body = hojaEstilo['BodyText']
guion.append(Paragraph("A continuación, se presenta un análisis gráfico de la distribución de los ingresos generados por los diferentes conceptos de servicios y productos facturados.", estilo_body))
guion.append(Spacer(1, 15))

# Añadir el gráfico de ventas
guion.append(d_ventas_chart)
guion.append(Spacer(1, 20))

# Conclusión
guion.append(Paragraph("Este análisis permite identificar las áreas de mayor contribución económica, facilitando la toma de decisiones estratégicas.", estilo_body))
guion.append(Spacer(1, 40))

# Pie de página
estilo_footer = hojaEstilo['Normal']
estilo_footer.fontSize = 8
estilo_footer.alignment = 1
guion.append(Paragraph(f"{nombre_empresa} - {email_empresa} - Página 1 de 1", estilo_footer))


# 4. GENERACIÓN DEL PDF
doc = SimpleDocTemplate('ejemplo_examen3.pdf', pagesize=A4, showBoundary=0)
doc.build(guion)
