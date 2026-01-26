# Guía de Estudio y Estrategias para el Examen de Diseño de Interfaces (ReportLab)

Este documento tiene como objetivo proporcionarte una guía para abordar los posibles problemas del examen de Diseño de Interfaces, centrándose en la generación de PDFs con la librería ReportLab en Python.

## Estructura General de un Documento ReportLab

La mayoría de los ejercicios implicarán la creación de un PDF que combine texto, tablas y/o gráficos. Recuerda la estructura básica:

1.  **Importaciones:** Asegúrate de importar todos los módulos necesarios (`SimpleDocTemplate`, `Paragraph`, `Table`, `Image`, `Spacer`, `Drawing`, `VerticalBarChart`, `Pie`, `HorizontalLineChart`, `colors`, `getSampleStyleSheet`, `pagesizes`, etc.).
2.  **Datos y Configuración Inicial:** Define los datos que se mostrarán en el PDF (listas para tablas, tuplas para gráficos, etc.).
3.  **Configuración de Estilos:** Utiliza `getSampleStyleSheet()` para obtener estilos predefinidos y modifícalos según sea necesario.
4.  **Creación de Elementos Platypus (Story):**
    *   **Párrafos:** Usa `Paragraph("Tu texto", tuEstilo)`.
    *   **Espacios:** Usa `Spacer(ancho, alto)` para añadir espacios verticales u horizontales.
    *   **Imágenes:** Usa `Image("ruta/a/imagen.png", width=X, height=Y)`.
    *   **Tablas:** Define una lista de listas para los datos y luego crea `Table(datos)`. Aplica estilos con `table.setStyle([])`.
    *   **Gráficos:** Los gráficos requieren un objeto `Drawing` (`Drawing(ancho, alto)`) al que se le añade el tipo de gráfico (`VerticalBarChart`, `Pie`, etc.) y las etiquetas (`Label`). Luego se añade el `Drawing` al `guion`.
5.  **Construcción del "Guion" (Story):** Crea una lista llamada `guion` (o similar) y añade los elementos Platypus en el orden deseado.
6.  **Generación del PDF:**
    *   Crea un objeto `SimpleDocTemplate("nombre_archivo.pdf", pagesize=A4, showBoundary=0)`.
    *   Llama a `doc.build(guion)`.

## Puntos Clave a Considerar en el Examen

### 1. Tablas Avanzadas

*   **Combinación de celdas (`SPAN`):** Practica la combinación de celdas tanto horizontal como verticalmente.
*   **Estilos condicionales:** Aplica diferentes colores de fondo, fuentes o bordes a filas/columnas específicas.
*   **Contenido complejo en celdas:** Inserta imágenes o párrafos dentro de las celdas de una tabla (ver `ejemplosClase\Utils\ExemplosReportLab5.py`).
*   **Alineación y Relleno:** Dominar `ALIGN`, `VALIGN`, `LEFTPADDING`, `RIGHTPADDING`, `TOPPADDING`, `BOTTOMPADDING`.
*   **Bordes y Cuadrículas:** `BOX`, `INNERGRID`, `LINEABOVE`, `LINEBELOW`, `LINEAFTER`.

    *   **Referencia:**
        *   `ejemplosClase\Facturas\Factura1\__init__.py`
        *   `ejemplosClase\Facturas\Factura2\__init__.py`
        *   `ejemplosClase\EjExamen\prueba.py`
        *   `ejemplosClase\Utils\ExemplosReportLab5.py`

### 2. Gráficos

*   **Tipos de Gráficos:** Familiarízate con `VerticalBarChart`, `HorizontalLineChart`, `Pie` y `Pie3d`.
*   **Configuración de Ejes:** Ajusta `valueMin`, `valueMax`, `valueStep` para los ejes de valor, y `categoryNames` para los ejes de categorías.
*   **Etiquetas y Títulos:** Utiliza `Label` para títulos de gráficos y etiquetas de ejes. Controla su posición (`setOrigin`, `angle`).
*   **Leyendas (`Legend`):** Implementa leyendas para gráficos de barras y de tarta, controlando su posición y estilo.
*   **Estilos de Gráfico:** Colores de barras/sectores, grosor de líneas, símbolos en puntos de línea.
*   **Objeto `Drawing`:** Entiende cómo los gráficos se "dibujan" dentro de un objeto `Drawing` y cómo este se añade al `guion`.

    *   **Referencia:**
        *   `ejemplosClase\Graficos\__init__.py`
        *   `ejemplosClase\EjExamen\prueba.py`
        *   `ejemplosClase\Utils\ExemplosReportLab6.py`

### 3. Texto y Párrafos

*   **Estilos de Párrafo:** Uso de `getSampleStyleSheet()` y modificación de propiedades como `fontSize`, `fontName`, `textColor`, `backColor`, `alignment`.
*   **Flujo de Texto:** Cómo los párrafos se adaptan al ancho de página y se rompen automáticamente.
*   **Canvas Directo vs. Platypus:** Aunque ReportLab permite el uso directo de `canvas` para dibujo de bajo nivel (ver `ejemplosClase\Utils\ExemplosReportLab.py` y `ExemplosReportLab3.py`), en un examen de interfaces probablemente se priorizará Platypus por su manejo automático del flujo. No obstante, saber las diferencias es útil.

### 4. Imágenes

*   **Inserción de Imágenes:** `Image("ruta", width, height)`.
*   **Manejo de rutas:** Asegúrate de que las rutas a las imágenes sean correctas, ya sean relativas o absolutas.

### 5. Conceptos Avanzados (posibles, aunque menos probables en un primer examen)

*   **Multipage:** Cómo manejar contenido que se extiende a varias páginas. El `SimpleDocTemplate` lo maneja en gran medida de forma automática, pero considera el uso de `PageBreak()`.
*   **Flowables Personalizados:** Crear tus propios objetos `Flowable` para contenido muy específico.

## Estrategia General para el Examen

1.  **Lee Detenidamente el Enunciado:** Identifica todos los requisitos: qué elementos (texto, tablas, gráficos, imágenes) deben incluirse, qué estilos se deben aplicar, y cómo deben organizarse.
2.  **Esquematiza el PDF:** Haz un pequeño dibujo o lista de los elementos en el orden en que aparecerán en el documento. Esto te ayudará a organizar tu `guion`.
3.  **Empieza por lo Básico:** Crea un PDF simple con un `SimpleDocTemplate` y un párrafo. Asegúrate de que se genera correctamente.
4.  **Añade Elementos Uno a Uno:**
    *   Primero el texto principal y los títulos.
    *   Luego las imágenes.
    *   Después las tablas (primero los datos, luego los estilos).
    *   Finalmente los gráficos (objeto `Drawing`, gráfico, etiquetas, leyenda).
5.  **Prueba Iterativamente:** Genera el PDF con frecuencia para ver el resultado de tus cambios y corregir errores a medida que avanzas.
6.  **Manejo de Errores:** Presta atención a los mensajes de error de ReportLab. A menudo indican problemas con los estilos de tabla, los datos de los gráficos o las rutas de las imágenes.
7.  **Revisa los Ejemplos Existentes:** Utiliza los archivos en `ejemplosClase\Facturas`, `ejemplosClase\Graficos` y `ejemplosClase\Utils` como referencia. No tienes que memorizar todo, pero sí saber dónde buscar ejemplos de sintaxis y estilos.
8.  **¡Practica!** La mejor manera de prepararse es intentando recrear o modificar los ejemplos por tu cuenta.

¡Mucha suerte en tu examen!
