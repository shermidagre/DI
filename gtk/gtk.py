
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana")
        self.setMinimumSize(400, 300)

        caixa = QVBoxLayout()

        self.lblEtiqueta = QLabel("Ola")
        self.lblEtiqueta.setText("Introduce tu nombre :")

        self.saudo = QLineEdit()

        btnSaudo = QPushButton ("Saludar")
        btnSaudo.clicked.connect(self.saludar)

        caixa.addWidget(self.lblEtiqueta)
        caixa.addWidget(self.saudo)
        caixa.addWidget(btnSaudo)

        self.lblEtiqueta2 = QLabel("Qui ti pasa :")

        self.saudo2 = QLineEdit()

        btnSaudo2 = QPushButton ("klkrandom")
        btnSaudo2.clicked.connect(self.saludar2)


        caixa.addWidget(self.lblEtiqueta2)
        caixa.addWidget(self.saudo2)
        caixa.addWidget(btnSaudo2)

        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()


    def saludar (self):
        nome = self.saudo.text()
        self.lblEtiqueta.setText(f"Ola, {nome}!")

    def saludar2 (self):
        nome2 = self.saudo2.text()
        self.lblEtiqueta2.setText(f"me la pela, {nome2}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()

    sys.exit(app.exec())

