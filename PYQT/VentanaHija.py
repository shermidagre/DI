
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from pyq import VentanaPadre


class VentanaHija(QMainWindow):
    def __init__(self, ventandapadre):
        super().__init__()
        self.ventandapadre = None
        self.setWindowTitle("Mi segunda ventana")
        self.setMinimumSize(400, 300)

        caixa = QVBoxLayout()

        self.lblEtiqueta = QLabel("Ola")
        self.lblEtiqueta.setText("Esta es la segunda ventana")
        self.lblEtiqueta.setStyleSheet("font-weight: bold; color: red;")
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btnSaudo = QPushButton("Abrir la ventana padre")
        btnSaudo.setStyleSheet("background-color: lightblue;")
        btnSaudo.clicked.connect(self.abrirventanapadre)

        caixa.addWidget(self.lblEtiqueta)
        caixa.addWidget(btnSaudo)





        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()


    def abrirventanapadre (self):

        self.close()
        if self.ventandapadre is None:
            self.ventandapadre = VentanaPadre.VentanaPadre()
            self.ventandapadre.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaHija(None)
    sys.exit(app.exec())
