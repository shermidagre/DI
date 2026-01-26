# Arquitectura de un Documento ReportLab: Guía Completa de Objetos y Posicionamiento

¡Hola! Veo que quieres entender cómo funciona ReportLab para crear PDFs, ¡y no te preocupes, aquí te lo explico como si fuera la primera vez que lo ves! Piensa en ReportLab como una caja de herramientas muy potente para construir documentos PDF con Python.

El objetivo de este documento es proporcionarte una guía completa sobre los objetos principales de ReportLab, cómo se posicionan en el documento y qué atributos clave tienen. Así tendrás un esquema mental claro para estructurar tus exámenes.

## ¿Qué es ReportLab y cómo funciona un PDF "programado"?

Imagina que un PDF es como un lienzo en blanco o un pergamino digital. Con ReportLab, en lugar de dibujar con un pincel, escribimos instrucciones en Python para que el ordenador "dibuje" el texto, las tablas, las imágenes y los gráficos en ese pergamino.

La clave de ReportLab es algo llamado **Platypus** (¡sí, como el ornitorrinco!). Platypus nos ayuda a organizar el contenido de forma más inteligente, como si fuera un procesador de textos, manejando automáticamente cosas como los saltos de página cuando el contenido es muy largo.

## El Gran Secreto: El "Guion" (o "Story")

Piensa en el PDF que vas a crear como una película o una obra de teatro. Y como toda obra, necesita un **guion**. En ReportLab, este guion es una lista normal de Python (normalmente llamada `guion` o `story`). En esta lista, vas añadiendo, en orden, todos los "elementos" que quieres que aparezcan en tu PDF.

**Regla de Oro:** Los elementos se añaden al `guion` **en el orden en que quieres que aparezcan de arriba a abajo en el PDF**. Si pones la imagen antes que el título, la imagen saldrá primero.

## Estructura General de un Archivo ReportLab

Todos los ejemplos que tienes siguen, más o menos, esta estructura:

1.  **Importaciones (Las Herramientas que Necesitas):** Aquí le dices a Python qué funciones y clases de ReportLab vas a usar (ej: `Paragraph`, `Table`, `Image`, `VerticalBarChart`, `colors`, etc.). Piensa en esto como sacar las herramientas adecuadas de tu caja.
2.  **Datos y Configuración Inicial:** Preparas toda la información que mostrarás (texto, números, listas para tablas o gráficos) y creas los estilos básicos de texto (`hojaEstilo = getSampleStyleSheet()`).
3.  **Configuración de Elementos (Creando las "Piezas" del PDF):** Creas cada "cosa" que irá en tu PDF (párrafos, tablas, imágenes, gráficos) y les das sus características (tamaño, color, contenido, etc.). Es como construir los ladrillos.
4.  **Montaje del Guion (¡Construyendo el PDF en Orden!):** Añades esos "ladrillos" a tu lista `guion` en el orden exacto en que quieres que aparezcan en el documento. Esto es el "plano" de tu casa.
5.  **Generación del PDF (¡Creando el Archivo!):** Finalmente, le dices a ReportLab que tome tu `guion` y lo "construya" en un archivo PDF (`SimpleDocTemplate(...).build(guion)`). Es como construir la casa según el plano.

## Entendiendo la Posición: Flujo Vertical vs. Posición Fija

Este es uno de los puntos más importantes para que tus documentos queden como esperas:

*   **Flujo Vertical (Platypus - "Lo normal"):** La mayoría de las cosas que añades al `guion` (como `Paragraph`, `Table`, `Image`, `Spacer`, `PageBreak`, `KeepTogether`) se comportan como en un procesador de textos. Se van colocando una debajo de la otra. ReportLab las "empuja" hacia abajo y las organiza en las páginas. Este es el comportamiento por defecto y la base de cómo se posicionan los objetos.
*   **Posición Fija (Graphics - "El minilienzo"):** Los gráficos, sin embargo, son un caso especial. Se dibujan dentro de un "lienzo" especial llamado `Drawing`. Dentro de este `Drawing`, tú sí puedes decir exactamente dónde va cada elemento (como un `VerticalBarChart`, un `Pie`, un `HorizontalLineChart` o un `Label`) usando coordenadas `(x, y)`. Luego, este `Drawing` completo se añade al `guion` y se comporta como una sola "pieza" en el flujo vertical.

## Esquema Mental para Posicionar Objetos (¡Tu CheckList!)

1.  **Piensa en Vertical:** Todo lo que añades al `guion` fluye de arriba abajo. Los elementos se apilan.
2.  **Usa `Spacer` sin miedo:** ¿Necesitas más espacio entre dos elementos? ¡`Spacer` al rescate! `guion.append(Spacer(1, 30))` para 30 puntos de espacio vertical.
3.  **Las Tablas son tus Amigas para Layout:** Si necesitas colocar cosas una al lado de la otra (como un logo y la info de la empresa), o en una cuadrícula compleja, ¡usa una `Table`! Puedes hacerla "invisible" (sin bordes) si solo la usas para organizar.
4.  **`Drawing` es tu Minilienza para Gráficos:** Para gráficos, piensa que estás dibujando dentro de una caja (`Drawing`). Aquí usas coordenadas `(x, y)` para posicionar los elementos del gráfico *dentro de esa caja*. Luego, la caja `Drawing` se añade al `guion` como un bloque más al `guion`.

## Atributos Clave de los Objetos (¡Tu Chuleta Completa!)

Aquí tienes una chuleta rápida de atributos importantes para los objetos que más usarás en el examen, con sus propósitos y cómo se usan.

### **1. `SimpleDocTemplate` (El Documento Completo)**

Es el contenedor principal de tu PDF.

*   `filename` (cadena): El nombre del archivo PDF que se creará (ej: `'mi_documento.pdf'`).
*   `pagesize` (tupla): El tamaño de la página (ej: `A4`, `letter`). `reportlab.lib.pagesizes` tiene muchos tamaños predefinidos.
*   `showBoundary` (0 o 1): Si lo pones a `1`, dibuja un borde rojo alrededor de cada elemento `Flowable` en el PDF. ¡Útil para ver dónde está cada "caja" y depurar la posición! Si es `0` (o no lo pones), no se ve nada.

### **2. `Paragraph` (Texto con Estilo)**

Para bloques de texto que se ajustan al ancho de la página.

*   `text` (cadena): El texto que quieres mostrar. Puedes usar etiquetas HTML básicas (`<b>`, `<i>`, `<font color="red">`) dentro del texto para dar formato.
*   `style` (objeto Style): El estilo de texto a aplicar. ¡Esto es CRUCIAL! Se obtiene de `getSampleStyleSheet()`.
    *   **Cómo obtener y modificar estilos:**
        ```python
        hojaEstilo = getSampleStyleSheet()
        estilo_titulo = hojaEstilo['h1'] # Obtiene un estilo predefinido
        estilo_titulo.fontSize = 24    # Cambia el tamaño de la fuente
        estilo_titulo.textColor = colors.blue # Cambia el color del texto
        estilo_titulo.alignment = 1    # Alineación: 0=LEFT, 1=CENTER, 2=RIGHT
        # Otros atributos comunes de estilo:
        # estilo_titulo.fontName = 'Helvetica-Bold'
        # estilo_titulo.backColor = colors.lightgrey # Fondo del párrafo
        # estilo_titulo.leading = 14 # Espacio entre líneas del párrafo
        # estilo_titulo.leftIndent = 20 # Margen izquierdo
        # estilo_titulo.rightIndent = 20 # Margen derecho
        ```

### **3. `Image` (Imágenes)**

Para insertar imágenes en tu PDF.

*   `filename` (cadena): Ruta al archivo de imagen (ej: `'../Imagenes/logo.png'`). Puede ser una ruta relativa.
*   `width` (número): Ancho de la imagen en puntos.
*   `height` (número): Alto de la imagen en puntos.
*   `hAlign` (cadena): Alineación horizontal si la imagen es más pequeña que el espacio disponible ('LEFT', 'CENTER', 'RIGHT').

### **4. `Spacer` (Espacios Vacíos)**

Para añadir espacios en blanco vertical u horizontal y separar elementos.

*   `width` (número): Ancho del espacio. Normalmente `1` para un espacio vertical, ya que el ancho se autoajusta. Para un espacio horizontal dentro de una tabla, sí sería un número.
*   `height` (número): Alto del espacio en puntos. Este es el que usas para separar cosas verticalmente (ej: `Spacer(1, 20)` crea un espacio de 20 puntos de alto).

### **5. `PageBreak` (Salto de Página)**

Fuerza un salto de página, moviendo el siguiente contenido a una nueva hoja.

*   Se añade directamente al `guion`: `guion.append(PageBreak())`.

### **6. `KeepTogether` (Mantener Juntos)**

Asegura que un grupo de elementos (ej: un título y su tabla) no se separe en dos páginas diferentes.

*   Toma una lista de `Flowables`: `guion.append(KeepTogether([titulo_parrafo, mi_tabla]))`.

### **7. `Table` (Tablas y Layout Avanzado)**

El objeto más versátil para mostrar datos tabulares y para organizar el diseño de tu documento.

*   `data` (lista de listas): La "matriz" de datos de tu tabla. Cada sublista es una fila, y cada elemento de la sublista es el contenido de una celda. Las celdas pueden contener texto, `Paragraph`, `Image`, etc.
*   `colWidths` (lista o tupla): Ancho de cada columna en puntos. Si no lo pones, ReportLab intenta autoajustar. Puedes usar `None` para que ReportLab calcule.
*   `rowHeights` (lista o tupla): Alto de cada fila en puntos.
*   `setStyle` (lista de tuplas de comandos): Aquí es donde defines el diseño de tu tabla. Cada comando es una tupla: `('COMANDO', (col_ini, row_ini), (col_fin, row_fin), VALOR)`.
    *   `(col_ini, row_ini)`: Esquina superior izquierda de la celda o rango de celdas.
    *   `(col_fin, row_fin)`: Esquina inferior derecha de la celda o rango de celdas.
        *   `(-1,-1)` se refiere a la última celda.
        *   `(-1,0)` se refiere a la última celda de la primera fila.
    *   **Comandos de Estilo Comunes:**
        *   `'BACKGROUND'`: `colors.red` (color de fondo de celdas).
        *   `'TEXTCOLOR'`: `colors.blue` (color del texto).
        *   `'ALIGN'`: `'LEFT'`, `'CENTER'`, `'RIGHT'` (alineación horizontal).
        *   `'VALIGN'`: `'TOP'`, `'MIDDLE'`, `'BOTTOM'` (alineación vertical).
        *   `'FONTNAME'`: `'Helvetica-Bold'`, `'Courier'` (tipo de fuente).
        *   `'FONTSIZE'`: `12` (tamaño de la fuente).
        *   `'BOTTOMPADDING'`, `'TOPPADDING'`, `'LEFTPADDING'`, `'RIGHTPADDING'`: `5` (espaciado interno de las celdas en puntos).
        *   `'GRID'`, `'BOX'`, `'INNERGRID'`: `(0.5, colors.black)` (bordes y rejillas de la tabla).
            *   `'BOX'`: Borde exterior.
            *   `'INNERGRID'`: Rejilla interior.
        *   `'LINEABOVE'`, `'LINEBELOW'`, `'LINEBEFORE'`, `'LINEAFTER'`: `(1, colors.red)` (líneas específicas).
        *   `'SPAN'`: Para unir celdas. `'SPAN', (col_ini, row_ini), (col_fin, row_fin)`. ¡Útil para títulos que ocupan varias columnas!

### **8. `Drawing` (El Contenedor de Gráficos)**

Es el "lienzo" donde dibujas tus gráficos y otros elementos de `reportlab.graphics`. Este `Drawing` se añade luego al `guion` como una única "caja".

*   `width` (número): Ancho de tu "lienzo" de dibujo en puntos.
*   `height` (número): Alto de tu "lienzo" de dibujo en puntos.
*   `add(elemento)`: Para añadir gráficos (`VerticalBarChart`, `Pie`, `HorizontalLineChart`), etiquetas (`Label`), leyendas (`Legend`), etc., a este lienzo. Las coordenadas `(x, y)` de estos elementos son relativas a la esquina inferior izquierda de este `Drawing`.

### **9. Objetos Gráficos Específicos (¡Los Gráficos en Sí!)**

Todos los gráficos comparten algunas propiedades básicas:

*   `x`, `y` (números): Posición `(x, y)` del gráfico dentro de su `Drawing` (relativa a la esquina inferior izquierda del `Drawing`).
*   `width`, `height` (números): Dimensiones del gráfico dentro de su `Drawing`.
*   `data` (lista de tuplas): Los datos que el gráfico va a representar. La estructura de `data` depende del tipo de gráfico.

#### **9.1. `VerticalBarChart` (Gráficos de Barras Verticales)**

*   `data`: Una lista de tuplas. Cada tupla es una "serie" de datos.
    *   `ej: [(10, 20, 30), (15, 25, 35)]` son dos series con tres barras cada una.
    *   **¡TRUCO para colores individuales!:** Si quieres que cada barra de una *única línea de datos* tenga un color diferente, debes hacer que cada barra sea su propia "serie": `data = [(v1,), (v2,), (v3,)]`.
*   `valueAxis` (objeto): El eje de los valores (normalmente vertical).
    *   `valueMin`, `valueMax`, `valueStep`: Valores mínimo, máximo y el incremento de las marcas en el eje.
*   `categoryAxis` (objeto): El eje de las categorías (normalmente horizontal).
    *   `categoryNames` (lista de cadenas): Nombres para las categorías (ej: `['Ene', 'Feb', 'Mar']`).
    *   `labels`: Objeto para configurar las etiquetas del eje de categorías.
        *   `labels.boxAnchor`: Posición del anclaje de la caja del texto (ej: `'ne'` para noreste, `'n'` para norte).
        *   `labels.angle`: Ángulo de las etiquetas (útil si los nombres son largos).
        *   `labels.dx`, `labels.dy`: Desplazamiento de las etiquetas.
*   `bars`: Objeto `BarChartProperties` para configurar el aspecto de las barras.
    *   **¡CLAVE para colores!**: Si `data` tiene múltiples series, `chart.bars[idx_serie].fillColor = color`.
    *   **¡CLAVE para colores INDIVIDUALES en una sola serie!**: Si has reestructurado `data` a `[(v1,), (v2,), ...]`, entonces `chart.bars[i].fillColor = color` para cada barra `i`.
    *   `fillColor` (color o lista de colores): Color de relleno.
    *   `strokeColor`, `strokeWidth`: Color y grosor del borde.
    *   `barSpacing`: Espacio entre barras de la misma serie.
    *   `groupSpacing`: Espacio entre grupos de barras (si tienes varias series).

#### **9.2. `Pie` (Gráficos de Tarta)**

*   `data`: Una lista de números. Cada número es el valor de una "rebanada" de la tarta (ej: `[10, 20, 30]`).
*   `slices`: Objeto `WedgeProperties` para configurar las rebanadas.
    *   `slices[i].fillColor`: Color de relleno para la rebanada `i`.
    *   `slices[i].strokeWidth`, `slices[i].strokeColor`: Borde de la rebanada.
    *   `slices[i].popout`: Cuánto "sale" la rebanada del centro (útil para destacar).
    *   **¡CLAVE para etiquetas!**: Para el texto de las etiquetas de cada rebanada:
        *   `labels` (lista de cadenas): Una lista de textos para cada rebanada.
        *   `slices.fontName`, `slices.fontSize`, `slices.fontColor`: Para el estilo de los textos de las etiquetas.
        *   `sideLabels`: `0` o `1`. Si es `1`, ReportLab dibuja las etiquetas fuera de la tarta con líneas indicadoras.
        *   `labelRadius`: Distancia de la etiqueta al centro de la tarta.

#### **9.3. `HorizontalLineChart` (Gráficos de Líneas Horizontales)**

*   `data`: Una lista de tuplas. Cada tupla es una "serie" de puntos para una línea.
    *   `ej: [(10, 12, 15), (8, 11, 14)]` son dos líneas.
*   `valueAxis`, `categoryAxis`: Similares a `VerticalBarChart`.
*   `lines`: Propiedades para las líneas.
    *   `lines[i].strokeWidth`: Grosor de la línea `i`.
    *   `lines[i].strokeColor`: Color de la línea `i`.
    *   `lines[i].symbol`: Para añadir marcadores en cada punto de la línea (ej: `makeMarker('Circle')`).

### **10. `Label` (Texto dentro de un `Drawing`)**

Para añadir texto dentro de tus objetos `Drawing` (títulos de gráficos, etiquetas específicas, etc.).

*   `setText(cadena)`: El texto a mostrar.
*   `setOrigin(x, y)`: Posición `(x, y)` de la etiqueta dentro del `Drawing`.
*   `fontName` (cadena): Tipo de fuente.
*   `fontSize` (número): Tamaño de la fuente.
*   `angle` (número): Ángulo del texto en grados.

### **11. `Legend` (Leyendas para Gráficos)**

Para explicar qué significa cada color o línea en tu gráfico.

*   `x`, `y` (números): Posición `(x, y)` de la leyenda dentro del `Drawing`.
*   `colorNamePairs` (lista de tuplas): `[(color, 'Nombre')]`. La lista de pares (color del elemento, texto de la leyenda).
*   `fontName`, `fontSize`: Estilo del texto de la leyenda.
*   `boxAnchor`: Cómo se "ancla" la caja de la leyenda (ej: `'nw'` para esquina superior izquierda).
*   `strokeColor`, `strokeWidth`: Color y grosor del borde de la leyenda.

---

¡Espero que esta guía detallada te dé una base sólida para tu examen! Recuerda que la práctica es clave. Revisa los ejemplos de la carpeta `ejemplosClase/EjExamen/` para ver cómo se aplican estos conceptos. ¡Mucha suerte!