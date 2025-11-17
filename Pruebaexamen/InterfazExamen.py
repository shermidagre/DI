import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QTextEdit, QTableWidget,
    QTableWidgetItem, QMessageBox, QLabel
)


class InterfazExamen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Miniexamen PyQt")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        layout_principal = QVBoxLayout()

        # --- Texto corto ---
        self.label = QLabel("Texto corto:")
        self.input_text = QLineEdit()
        layout_principal.addWidget(self.label)
        layout_principal.addWidget(self.input_text)

        # --- Texto largo ---
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Texto largo...")
        layout_principal.addWidget(self.text_edit)

        # Texto para el nombre

        self.labelNombre = QLabel("Nombre:")
        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText("Nombre...")
        layout_principal.addWidget(self.labelNombre)
        layout_principal.addWidget(self.nombre)


        # --- Botones base ---
        layout_botones = QHBoxLayout()
        self.boton_mostrar = QPushButton("Mostrar")
        layout_botones.addWidget(self.boton_mostrar)

        self.botonSaludar = QPushButton("Saludar")
        layout_botones.addWidget(self.botonSaludar)

        self.botonLimpar = QPushButton("Limpar")
        layout_botones.addWidget(self.botonLimpar)

        self.botonTabla = QPushButton("Agregar tabla")
        layout_botones.addWidget(self.botonTabla)

        layout_principal.addLayout(layout_botones)
        self.boton_mostrar.clicked.connect(self.mostrar_texto)
        self.botonSaludar.clicked.connect(self.saludar)
        self.botonLimpar.clicked.connect(self.limpiarTexto)
        self.botonTabla.clicked.connect(self.agregarTabla)




        # --- Tabla ---
        self.tabla = QTableWidget()
        self.tabla.setRowCount(0)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Texto corto", "Texto largo"])
        layout_principal.addWidget(self.tabla)

        self.setLayout(layout_principal)

    def mostrar_texto(self):
        texto_corto = self.input_text.text()
        texto_largo = self.text_edit.toPlainText()
        QMessageBox.information(self, "Contenido", f"Texto corto: {texto_corto}\nTexto largo:\n{texto_largo}")

    def saludar(self):
        nombre = self.nombre.text()  # Obtener el texto del QLineEdit
        QMessageBox.information(self, "Saludo", f"¡Hola, {nombre}!")

    def limpiarTexto(self):
        self.input_text.clear()
        self.text_edit.clear()

    def agregarTabla(self):
        # Obtener el número actual de filas y agregar una nueva
        fila_nueva = self.tabla.rowCount()
        self.tabla.setRowCount(fila_nueva + 1)

        # Insertar el texto corto en la columna 0
        texto_corto = self.input_text.text()
        item_texto_corto = QTableWidgetItem(texto_corto)
        self.tabla.setItem(fila_nueva, 0, item_texto_corto)

        # Insertar el texto largo en la columna 1
        texto_largo = self.text_edit.toPlainText()
        item_texto_largo = QTableWidgetItem(texto_largo)
        self.tabla.setItem(fila_nueva, 1, item_texto_largo)

        # Calcular la longitud del texto largo y ponerla en la columna 2
        longitud_texto = str(len(texto_largo))
        item_longitud = QTableWidgetItem(longitud_texto)
        self.tabla.setItem(fila_nueva, 2, item_longitud)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = InterfazExamen()
    ventana.show()
    sys.exit(app.exec())
