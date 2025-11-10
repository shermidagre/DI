
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana")
        self.setMinimumSize(400, 300)

        caixa = QVBoxLayout()

        self.lblEtiqueta = QLabel("Ola")
        self.lblEtiqueta.setText("Introduce tu nombre")
        self.lblEtiqueta.setStyleSheet("font-weight: bold; color: blue;")
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)



        self.saudo = QLineEdit()

        btnSaudo = QPushButton("Saludar")
        btnSaudo.setStyleSheet("background-color: lightblue;")
        btnSaudo.clicked.connect(self.saludar)
        self.saudo.returnPressed.connect(self.saludar)


        caixa.addWidget(self.lblEtiqueta)
        caixa.addWidget(self.saudo)
        caixa.addWidget(btnSaudo)

        btnOutraFiestra = QPushButton("Abrir la ventana hija")
        btnOutraFiestra.setStyleSheet("background-color: lightgreen;")
        btnOutraFiestra.clicked.connect(self.abrirventanahija)
        caixa.addWidget(btnOutraFiestra)

        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()


    def saludar (self):
        nome = self.saudo.text()
        self.saudo.clear()
        nome = nome.strip()
        if nome == "" or nome.isdigit():
            self.lblEtiqueta.setStyleSheet("font-weight: bold; color: red;")
            nome = "Porfavor introduce un nombre"
            self.lblEtiqueta.setText(""f"{nome}!")
        else:
           self.lblEtiqueta.setText(f"Ola, {nome}!")
           self.lblEtiqueta.setStyleSheet("font-weight: bold; color: green;")

           # con el q timer de pyqt6 abrimos la ventana secreta despues de 2 segundos

           QTimer.singleShot(2000, self.abrirventanasecreta)



    def abrirventanahija(self):
        self.close()
        from pyq.SegundaVentana import SegundaVentana
        self.vh = SegundaVentana()
        self.vh.show()

    def abrirventanasecreta(self):
        self.close()
        from pyq.VentanaSecreta import VentanaSecreta
        self.vs = VentanaSecreta()
        self.vs.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(app.exec())

