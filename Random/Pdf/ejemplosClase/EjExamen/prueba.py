from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label

# 1. DATOS Y CONFIGURACIÓN INICIAL
guion = []

fila0 = ['FACTURA SIMPLIFICADA', '', '','']
fila1 = ['Nombre de tu empresa', '','', 'Logo de la Empresa']
fila2 = ['Dirección', '', '','']
fila3 = ['Ciudad y Pais', '', '','']
fila4 = ['CIF/NIF','', 'Fecha Emisión', 'DD/MM/AAAA']
fila5 = ['Teléfono','', 'Número de Factura', 'A0001']
fila6 = ['Mail', '', '','']

fila_descripcion = ['Descripcion','Importe','Cantidad','Total']
fila_producto1 = ['Producto1','3.2','5','16.00']
fila_producto2 = ['Producto2','4.2','5','17.00']
fila_producto3 = ['Producto3','5.2','5','18.00']
fila_producto4 = ['Producto4','6.2','5','69.00']

# 2. CONFIGURACIÓN DE LA GRÁFICA (OBJETOS GRAPHICS)
# Le damos tamaño al Drawing para que se vea la gráfica
d = Drawing(400, 200)

titulo_grafica = Label()
titulo_grafica.setText("Práctica grafica")
titulo_grafica.setOrigin(150, 180) # Ajustado para que salga centrado sobre la gráfica

datos_grafica = [(16,2,64,14,53,6)]
string_grafica = ['10','20','30','40','50','60']

grafica = VerticalBarChart()
grafica.x = 50 # Ajustado para que no se salga del dibujo
grafica.y = 50
grafica.height = 100
grafica.width = 300
grafica.data = datos_grafica
grafica.valueAxis.valueMin = 0
grafica.valueAxis.valueMax = 100
grafica.valueAxis.valueStep = 10
grafica.categoryAxis.categoryNames = string_grafica
grafica.barSpacing = 5
grafica.categoryAxis.labels.boxAnchor = 'nw'

d.add(titulo_grafica)
d.add(grafica)

# 3. CONFIGURACIÓN DE LA TABLA (OBJETOS PLATYPUS)
tabla_texto = Table([fila0,fila1,fila2,fila3,fila4,fila5,fila6,fila_descripcion,fila_producto1,fila_producto2,fila_producto3,fila_producto4])

tabla_texto.setStyle([
    ('FONTSIZE',(0,0),(-1,0),15),
    ('SPAN',(0,0),(-1,0)),
    ('ALIGN',(0,0),(-1,0),'RIGHT'),
    ('FONTSIZE',(0,1),(0,1),20),
    ('FONTSIZE',(0,1),(1,1),15),
    ('ALIGN',(0,1),(0,1),'LEFT'),
    ('ALIGN', (1, 1), (-1, 1), 'RIGHT'),
    ('FONTSIZE',(2,1),(2,1),15),
    ('TOPPADDING',(1,1),(-1,1),20),
    ('FONTNAME',(0,1),(-1,1),'Helvetica-BoldOblique'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('TEXTCOLOR',(0,0),(-1,0),colors.red),
    ('TEXTCOLOR',(2,1),(-1,1),colors.red),
    ('BOTTOMPADDING',(0,6),(-1,6),20),
    ('BACKGROUND',(0,7),(-1,7),colors.red),
    ('INNERGRID',(0,7),(-1,-1),0.5,colors.white),
    ('BACKGROUND',(0,8),(-1,-1),colors.gray),
    ('ALIGN',(0,7),(-1,11),'CENTER'),
    ('ALIGN', (3, 8), (-1, 11), 'RIGHT')
])

# 4. MONTAJE DEL GUION (FLUJO DEL DOCUMENTO)
follaEstilo = getSampleStyleSheet()

# Cabecera
cabeceira = follaEstilo["Heading4"]
cabeceira.backColor = colors.lightblue
guion.append(Paragraph("CABECEIRA DO DOCUMENTO", cabeceira))

# Cuerpo de texto
texto = "Texto incluido no documento, e que forma o contido. "
corpoTexto = follaEstilo['BodyText']
corpoTexto.fontSize = 12
guion.append(Paragraph(texto, corpoTexto))
guion.append(Spacer(0, 30))

# Imagen
try:
    imaxe = Image("../Imagenes/Imaxe1.png", width=200, height=200)
    guion.append(imaxe)
except:
    pass # Si no encuentra la imagen, continúa

guion.append(Spacer(0, 20))

# Título de la Gráfica
cabeceiraCursiva = follaEstilo["Heading2"]
cabeceiraCursiva.fontName = 'Helvetica-Oblique'
cabeceiraCursiva.alignment = 1
guion.append(Paragraph(" Exemplo", cabeceiraCursiva))
guion.append(Spacer(0, 10))

# Tabla y Gráfica final
guion.append(tabla_texto)
guion.append(Spacer(0, 20))
guion.append(d)

# 5. GENERACIÓN DEL PDF
doc = SimpleDocTemplate('Practica tablas.pdf', pagesize=A4, showBoundary=1)
doc.build(guion)