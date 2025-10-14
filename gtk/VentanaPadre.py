
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
import VentanaHija


class VentanaPadre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Padre")
        self.setMinimumSize(400, 300)

        self.VentanaHija = None

        caixa = QVBoxLayout()



        btnOutraFiestra = QPushButton("Abrir la ventana hija")
        btnOutraFiestra.setStyleSheet("background-color: lightgreen;")
        btnOutraFiestra.clicked.connect(self.abrirventanahija)
        caixa.addWidget(btnOutraFiestra)

        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()




    def abrirventanahija(self):

        self.hide()
        if self.VentanaHija is  None:
            self.VentanaHija = VentanaHija.VentanaHija(self)
        self.VentanaHija.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPadre()
    sys.exit(app.exec())

