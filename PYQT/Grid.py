from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QColor , QPalette


class VentanaConGrid(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)

        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)
        paleta.setColor(QPalette.ColorRole.WindowText, QColor(color))
        self.setPalette(paleta)


        self.show()

if __name__ == "__main__":
    ventana = VentanaConGrid()
    ventana.show()
