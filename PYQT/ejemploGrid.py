import sys
import Grid
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout

from PYQT.Grid import VentanaConGrid


class EjemploGrid(QMainWindow):
    def __init__(self):
        super().__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        cajaPrincipal = QVBoxLayout()
        centralWidget.setLayout(cajaPrincipal)

        cajaVertical = QHBoxLayout()

        cajaHorizontal = QVBoxLayout()



        cajaRoja = cajaVertical
        VentanaConGridRojo= Grid.VentanaConGrid('red')
        cajaRoja.addWidget(VentanaConGridRojo)
        cajaPrincipal.addLayout(cajaRoja)

        cajaAmarilla = cajaVertical
        VentanaConGridAmarillo= Grid.VentanaConGrid('yellow')
        cajaAmarilla.addWidget(VentanaConGridAmarillo)
        cajaPrincipal.addLayout(cajaAmarilla)

        cajaRoja = cajaVertical
        VentanaConGridRojo= Grid.VentanaConGrid('red')
        cajaRoja.addWidget(VentanaConGridRojo)
        cajaPrincipal.addLayout(cajaRoja)






        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EjemploGrid()
    sys.exit(app.exec())