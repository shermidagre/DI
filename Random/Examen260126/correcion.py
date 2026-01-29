import sqlite3

from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table, Spacer, PageBreak
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.textlabels import Label


def obterProductos(path, limite = 10):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT c.nome, COUNT(DISTINCT f.id_factura) as num_facturas,
        SUM(if.cantidade * if.prezo_unitario * (1-if.desconto/100)*(1+p.iva/100)) as facturacion_total
        FROM clientes c
        JOIN facturas f ON c.id_cliente = f.id_cliente
        JOIN linhas_factura if ON f.id_factura = if.id_factura
        JOIN produtos p ON if.id_produto = p.id_produto
        GROUP BY c.id_cliente, c.nome
        ORDER BY facturacion_total DESC
        LIMIT ?
    """,(limite,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados


datos = obterProductos("bdTendaOrdeadoresBig.bd",5)


def xerarFactura(datos):
    cabeceira = ['Posicion','Cliente','N Facturas','Facturacion Total']
    datosTabla = []
    datosTabla.append(cabeceira)

    for orde,linea in enumerate(datos):
        datosTabla.append([orde+1, linea[0], linea[1], f"{linea[2]:.2f} €"])
    print(datosTabla)

    t = Table(datosTabla)

    style = [
        # Cabecera

        ('BACKGROUND',(0,0),(-1,0),colors.blueviolet),
        ('TEXTCOLOR',(0,0),(-1,0),colors.white),
        ('ALIGN',(0,0),(-1,0),'CENTER'),

        # Datos

        ('GRID',(0,0),(-1,-1),1,colors.black),
        ('ALIGN',(0,1),(0,-1),'CENTER'),
        ('ALIGN',(2,1),(2,-1),'CENTER'),
        ('ALIGN',(-1,1),(-1,-1),'RIGHT'),
    ]

    for i in range(2,len(datosTabla),2):
        style.append(('BACKGROUND',(0,i),(-1,i),colors.lightgrey))

    t.setStyle(style)

    doc = SimpleDocTemplate("InformeClientes.pdf", pagesize=A4)

    doc.build([t])

    return t



def xerarTarta(datos):

    facturacion = []
    etiquetas = []

    for linea in datos:
        facturacion.append(linea[-1])
        etiquetas.append(linea[0])

    ancho = 400
    alto = 350
    debuxo = Drawing(ancho,alto)
    tarta = Pie()
    tarta.x = ancho / 2 - 100
    tarta.y = alto / 2 - 100
    tarta.width = 200
    tarta.height = 200
    tarta.data = facturacion
    tarta.labels = etiquetas
    doc = SimpleDocTemplate("GraficoClientes.pdf", pagesize=A4)
    guion = []

    debuxo.add(tarta)
    guion.append(debuxo)
    doc.build(guion)
    return tarta

def xerarInformentos(datos):
    elementos = []
    follaEstilo = getSampleStyleSheet()
    estiloTitulo = follaEstilo["Heading1"]

    titulo = Paragraph("INFORME DE CLIENTES OIR FACTURACION",estiloTitulo)

    elementos.append(titulo)
    elementos.append(xerarTarta(datos))
    elementos.append(xerarFactura(datos))

    doc = SimpleDocTemplate("Informe.pdf", pagesize=A4)

    doc.build(elementos)


xerarTarta(datos)
xerarFactura(datos)
