
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class VentanaSecreta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Secreta")
        self.setMinimumSize(400, 300)

        caixa = QVBoxLayout()

        self.lblEtiqueta = QLabel("Ola")
        self.lblEtiqueta.setText("Estas en tu lugar secreto")
        self.lblEtiqueta.setStyleSheet("font-weight: bold; color: purple;")


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
        from PrimeraVentana import VentanaPrincipal
        self.vp = VentanaPrincipal()
        self.vp.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaSecreta()
    sys.exit(app.exec())

