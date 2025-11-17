import sys
# Importamos QHBoxLayout para una posible expansión, aunque usaremos QVBoxLayout para el principal
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableView, QVBoxLayout,
    QWidget, QLabel, QRadioButton, QButtonGroup,
    QPushButton, QWidget, QHBoxLayout, QGroupBox
)
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt6.QtGui import QColor, QIcon, QAction


# Nota: El icono "tic16x16.jpg" no está disponible en este entorno,
# por lo que he comentado la línea para asegurar la ejecución del código.

class ModeloTabla(QAbstractTableModel):
    """Modelo de datos personalizado para QTableView."""

    def __init__(self, datos):
        super().__init__()
        self.datos = datos

    def rowCount(self, parent=QModelIndex()):
        return len(self.datos)

    def columnCount(self, parent=QModelIndex()):
        return len(self.datos[0]) if self.datos else 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        valor = self.datos[index.row()][index.column()]

        # Mostrar el valor como texto
        if role == Qt.ItemDataRole.DisplayRole:
            return str(valor)

        # Cambiar color de fondo si es True/False
        if role == Qt.ItemDataRole.BackgroundRole:
            if valor is True:
                return QColor("#E6FFDA")  # Verde muy claro
            elif valor is False:
                return QColor("#FFDADA")  # Rojo muy claro

        # Cambiar color de texto si es nombre
        if role == Qt.ItemDataRole.ForegroundRole:
            if valor == "Ana":
                return QColor("darkblue")
            if valor == "Luis":
                return QColor("darkred")

        # Ejemplo de icono: mostrar un marcador si el valor es True
        # if role == Qt.ItemDataRole.DecorationRole:
        #     if valor is True:
        #         # NOTA: Icono comentado ya que "tic16x16.jpg" no está disponible
        #         # return QIcon("tic16x16.jpg")
        #         pass

        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                # La primera fila contiene los encabezados en este ejemplo
                return self.datos[0][section]
            # No se requiere encabezado vertical explícito en este caso
        return None


class DemoTabla(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Demo PyQt6 Combinada: Tabla y Controles")
        self.setGeometry(100, 100, 800, 600)

        # ----------------------------------------------------
        # 1. Configuración del Layout Principal
        # ----------------------------------------------------

        # El widget central que contendrá todo
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # El diseño principal (Vertical)
        main_layout = QVBoxLayout(central_widget)

        # ----------------------------------------------------
        # 2. SECCIÓN DE LA TABLA (Anterior 'layout1')
        # ----------------------------------------------------

        # Datos de ejemplo (Excluimos la primera fila de datos reales)
        datos = [
            ["Nombre", "Edad", "Activo"],  # Encabezados (se usan en headerData)
            ["Ana", 25, True],
            ["Luis", 30, False],
            ["Marta", 28, True],
            ["Juan", 40, False]
        ]

        # Crear modelo y tabla
        self.modelo = ModeloTabla(datos)
        self.tabla = QTableView()
        # Ajustamos el modelo para omitir la primera fila de datos, usándola solo como encabezado
        self.tabla.setModel(ModeloTabla(datos[1:]))

        # Configurar la tabla para seleccionar filas completas
        self.tabla.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        # Label para mostrar selección
        self.label_seleccion = QLabel("Fila seleccionada: ninguna")

        # Diseño para la tabla y su label
        table_group = QGroupBox("Visor de Tabla con Roles Personalizados")
        layout_table = QVBoxLayout(table_group)
        layout_table.addWidget(self.tabla)
        layout_table.addWidget(self.label_seleccion)

        main_layout.addWidget(table_group)

        # Conectar selección de filas (Nota: la conexión debe hacerse después de inicializar self.tabla)
        self.tabla.selectionModel().selectionChanged.connect(self.fila_seleccionada)

        # ----------------------------------------------------
        # 3. SECCIÓN DE RADIO BUTTONS (Anterior 'layout2')
        # ----------------------------------------------------

        # Layout para los grupos de radio buttons
        container = QWidget()
        layout_controls = QHBoxLayout(container)

        # --- Grupo 1 ---
        GroupBox1 = QGroupBox("Grupo de Opciones 1")
        vbox1 = QVBoxLayout(GroupBox1)
        self.radio1 = QRadioButton("Grupo1 - Opción 1")
        self.radio2 = QRadioButton("Grupo1 - Opción 2")
        self.radio5 = QRadioButton("Grupo1 - Opción 3")
        self.grupo1 = QButtonGroup(self)
        self.grupo1.setExclusive(True)
        self.grupo1.addButton(self.radio1)
        self.grupo1.addButton(self.radio2)
        self.grupo1.addButton(self.radio5)
        vbox1.addWidget(self.radio1)
        vbox1.addWidget(self.radio2)
        vbox1.addWidget(self.radio5)
        layout_controls.addWidget(GroupBox1)

        # --- Grupo 2 ---
        GroupBox2 = QGroupBox("Grupo de Opciones 2")
        vbox2 = QVBoxLayout(GroupBox2)
        self.radio3 = QRadioButton("Grupo2 - Opción A")
        self.radio4 = QRadioButton("Grupo2 - Opción B")
        self.radio6 = QRadioButton("Grupo2 - Opción C")
        self.grupo2 = QButtonGroup(self)
        self.grupo2.setExclusive(True)
        self.grupo2.addButton(self.radio3)
        self.grupo2.addButton(self.radio4)
        self.grupo2.addButton(self.radio6)
        vbox2.addWidget(self.radio3)
        vbox2.addWidget(self.radio4)
        vbox2.addWidget(self.radio6)
        layout_controls.addWidget(GroupBox2)

        main_layout.addWidget(container)

        # --- Sección de resultado y limpieza ---
        result_group = QGroupBox("Resultado y Control")
        vbox_result = QVBoxLayout(result_group)

        # Label para mostrar la selección
        self.label_radios = QLabel("Selecciona una opción de cada grupo")
        self.label_radios.setStyleSheet("font-weight: green;")

        # Botón para limpiar selección
        self.botonLimpiar = QPushButton("Limpiar selección")
        self.botonLimpiar.setStyleSheet("""
            QPushButton {
                background-color: #E0E0E0;
                border: 1px solid #C0C0C0;
                border-radius: 5px;
                padding: 6px 15px;
            }
            QPushButton:hover {
                background-color: #D4D4D4;
            }
        """)
        self.botonLimpiar.clicked.connect(self.limpiar_seleccion)

        vbox_result.addWidget(self.label_radios)
        vbox_result.addWidget(self.botonLimpiar)
        main_layout.addWidget(result_group)

        main_layout.addStretch(1)  # Relleno para que los widgets se peguen arriba

        # Conexión de eventos para los radio buttons
        for r in [self.radio1, self.radio2, self.radio5, self.radio3, self.radio4, self.radio6]:
            r.toggled.connect(self.mostrar_seleccion)

        # Llamar a mostrar_seleccion al inicio para establecer el estado inicial del label
        self.mostrar_seleccion()

    # ----------------------------------------------------
    # Métodos (sin cambios funcionales, solo usan self.)
    # ----------------------------------------------------

    def fila_seleccionada(self, selected, deselected):
        # Obtener índices de filas seleccionadas
        # Nota: Usamos el modelo que solo contiene las filas de datos (datos[1:])
        filas = [index.row() + 1 for index in self.tabla.selectionModel().selectedIndexes()]
        filas = sorted(set(filas))  # quitar duplicados y sumar 1 para referenciar la fila original de datos
        if filas:
            self.label_seleccion.setText(f"Filas seleccionadas: {filas} (datos)")
        else:
            self.label_seleccion.setText("Fila seleccionada: ninguna")

    def mostrar_seleccion(self):
        g1 = "Ninguno"
        g2 = "Ninguno"

        # Grupo 1
        if self.radio1.isChecked():
            g1 = "Opción 1"
        elif self.radio2.isChecked():
            g1 = "Opción 2"
        elif self.radio5.isChecked():
            g1 = "Opción 3"

        # Grupo 2
        if self.radio3.isChecked():
            g2 = "Opción A"
        elif self.radio4.isChecked():
            g2 = "Opción B"
        elif self.radio6.isChecked():
            g2 = "Opción C"

        self.label_radios.setText(f"Grupo1: **{g1}**, Grupo2: **{g2}**")

    def limpiar_seleccion(self):
        # Desactivar exclusividad del grupo 1, limpiar botones, volver a activar
        # Usamos el método setExclusive(False) y luego setExclusive(True) para permitir deseleccionar
        self.grupo1.setExclusive(False)
        for btn in self.grupo1.buttons():
            btn.setChecked(False)
        self.grupo1.setExclusive(True)

        # Desactivar exclusividad del grupo 2, limpiar botones, volver a activar
        self.grupo2.setExclusive(False)
        for btn in self.grupo2.buttons():
            btn.setChecked(False)
        self.grupo2.setExclusive(True)

        self.label_radios.setText("Selecciona una opción de cada grupo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DemoTabla()
    window.show()
    sys.exit(app.exec())