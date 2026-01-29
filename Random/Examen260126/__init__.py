import sqlite3

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer, PageBreak
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label


def obterProductos(self, limite=5):
    conexion = sqlite3.connect("bdTendaOrdeadoresBig.bd")
    cursor = conexion.cursor()

    cursor.execute("""

        SELECT p.id_produto,
               p.nome,
               SUM(if.cantidade) as total_vendido,
               SUM(if.cantidade * if.prezo_unitario * (1 - if.desconto/100)) as facturacion
        FROM linhas_factura if
        JOIN produtos p ON if.id_produto = p.id_produto
        GROUP BY p.id_produto, p.nome
        ORDER BY total_vendido DESC
        LIMIT?
    """, (limite,))

    resultados = cursor.fetchall()

    conexion.close()

    return resultados


print(obterProductos(5))


# 1. DATOS Y CONFIGURACIÓN INICIAL
guion = []
hojaEstilo = getSampleStyleSheet()

# Texto largo para demostrar flujo de texto en múltiples páginas
texto_largo = """

"""  * 1

listanueva = [('Posicion','Produto','Unidades Vendidas', 'Facturacion'),]

print(listanueva)
listanueva2 = []

prueba = [obterProductos(5)]

for l in prueba:
    for i in l:
        for p in i:
            listanueva2.append(p)


# Datos para un gráfico de barras simple
etiquetas_vertical = [(listanueva2[2], listanueva2[6], listanueva2[10], listanueva2[14], listanueva2[18])]
etiquetas_horizontal = [listanueva2[1], listanueva2[5], listanueva2[9], listanueva2[13], listanueva2[17]]



# Datos para una tabla simple

datos_tabla = listanueva
datos_tabla2 = obterProductos(5)

#obtener datos


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
tabla_simple = Table(datos_tabla, colWidths=[130, 130, 130])
tabla_simple.setStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
])

tabla_simple2 = Table(datos_tabla2, colWidths=[130, 130, 130])
tabla_simple2.setStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
])

# Configuración del gráfico de barras
d_barras = Drawing(400, 200)

grafico_barras = VerticalBarChart()
grafico_barras.x = 50
grafico_barras.y = 50
grafico_barras.height = 100
grafico_barras.width = 400
grafico_barras.data = etiquetas_vertical
grafico_barras.valueAxis.valueMin = 0
grafico_barras.valueAxis.valueMax = 80
grafico_barras.valueAxis.valueStep = 10
grafico_barras.categoryAxis.categoryNames = etiquetas_horizontal
grafico_barras.groupSpacing = 14
grafico_barras.barSpacing = 2
grafico_barras.categoryAxis.labels.boxAnchor = 'ne'
grafico_barras.categoryAxis.labels.angle = 30 # pa meterle el angulo
d_barras.add(grafico_barras)

titulo_barras = Label()
titulo_barras.setText("Ventas ")
titulo_barras.setOrigin(200, 180)
titulo_barras.fontName = 'Helvetica-Bold'
titulo_barras.fontSize = 12
d_barras.add(titulo_barras)



#





guion.append(Paragraph("DI, EXAME: 1 CONTROL 2 AV Data : 26/01 de 2026", estilo_titulo_doc))
guion.append(Spacer(1, 20))

guion.append(Paragraph("", estilo_body))
guion.append(Spacer(1, 10))

guion.append(Paragraph("A partir de aqui estaran los ejercicios, esto es un subtitulo , en vez de la posicion de index, modifique el sql y puse el id del producto, y modifique la funcion del sql para que de limite tubiera 5 ya que con 10 aunque le establecieras el limite despues no lo aceptaba", hojaEstilo['h2']))
guion.append(Spacer(1, 5))
guion.append(Paragraph(texto_largo, estilo_body))
guion.append(Spacer(1, 20))

guion.append(Paragraph("Ejercicio 1", hojaEstilo['h2']))
guion.append(Spacer(1, 10))
guion.append(d_barras)
guion.append(Spacer(1, 20))


guion.append(Spacer(1, 40))
guion.append(Paragraph("Fin del ejercicio 1", estilo_body))

guion.append(Spacer(1, 150))
guion.append(Paragraph("Ejercicio 2", hojaEstilo['h2']))
guion.append(Spacer(1, 10))
guion.append(tabla_simple)
guion.append(tabla_simple2)
guion.append(Spacer(1, 20))


guion.append(Paragraph("Fin del ejercicio 2", estilo_body))

nombre = str(listanueva2[1])
unidades = str(listanueva2[2])
ud1 =  listanueva2[2]
ud2 =  listanueva2[6]
ud3 =  listanueva2[10]
ud4 =  listanueva2[14]
ud5 =  listanueva2[18]
suma = ud1 + ud2 + ud3 + ud4 + ud5
sumaAver = str(suma)


udf1 = listanueva2[3]
udf2 = listanueva2[7]
udf3 = listanueva2[11]
udf4 = listanueva2[15]
udf5 = listanueva2[19]

sumaf = udf1 + udf2 + udf3 + udf4 + udf5

sumafAver = str(sumaf)

guion.append(Spacer(1, 50))   
guion.append(Paragraph("Texto explicativo onde se comenta o cliente con mais facturacion importe desta, do estilo,O producto mais vendido he  " + nombre + " con " + unidades + " unidades " +
                       "no total, os 5 `productos mais vendidos representan " + sumaAver +
                       " unidades vendidas e unha facturacion de " + sumafAver + "  $.",
                       estilo_body))

doc = SimpleDocTemplate('Samuel_Hermida_Gregores_Examen_2AV.pdf', pagesize=A4, showBoundary=0)
doc.build(guion)
