import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton, QGroupBox
)
from PyQt6.QtCore import Qt


class FormularioClientes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 16-11-2023 grupo A")
        self.setGeometry(100, 100, 600, 500)
        self.initUI()

    def initUI(self):
        # Layout principal da janela
        main_layout = QVBoxLayout(self)

        ## 1. Seção Superior de Entrada de Dados (Simulando a área "Albari")
        # Criamos o QGroupBox, que visualmente agrupa os campos
        gpbCliente = QGroupBox("Albari")
        input_layout = QGridLayout()

        # --- Campos que replicam a imagem (2 colunas) ---

        # Elementos da Linha 1 (Número Albari / Data)
        lblNumeroAlbari = QLabel("Número Albari")
        cmbNumeroAlbari = QComboBox()
        lblData = QLabel("Data")
        txtData = QLineEdit()

        # Elementos da Linha 2 (Número Cliente / Nome Cliente)
        lblNumeroCliente = QLabel("Número Cliente")
        txtNumeroCliente = QLineEdit()
        lblNomeCliente = QLabel("Nome Cliente")
        txtNomeCliente = QLineEdit()

        # Elementos da Linha 3 (Apelidos)
        lblApelidosCliente = QLabel("Apelidos")
        txtApelidosCliente = QLineEdit()

        # Adicionar widgets ao QGridLayout

        # Linha 0 (Rótulos no topo da imagem: Número Albari, Data)
        input_layout.addWidget(lblNumeroAlbari, 0, 0)
        input_layout.addWidget(cmbNumeroAlbari, 0, 1)  # O ComboBox está na imagem
        input_layout.addWidget(lblData, 0, 2)
        input_layout.addWidget(txtData, 0, 3)

        # Linha 1 (Rótulos da sua lista: Número Cliente, Nome Cliente)
        input_layout.addWidget(lblNumeroCliente, 1, 0)
        input_layout.addWidget(txtNumeroCliente, 1, 1)
        input_layout.addWidget(lblNomeCliente, 1, 2)
        input_layout.addWidget(txtNomeCliente, 1, 3)

        # Linha 2 (Rótulo da sua lista: Apelidos)
        input_layout.addWidget(lblApelidosCliente, 2, 0)
        input_layout.addWidget(txtApelidosCliente, 2, 1)

        # Definir o QGridLayout como o layout do QGroupBox
        gpbCliente.setLayout(input_layout)
        main_layout.addWidget(gpbCliente)

        ## 2. Botões de Ação (Engadir, Editar, Borrar)
        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        h_layout_acoes = QHBoxLayout()
        h_layout_acoes.addWidget(btnEngadir)
        h_layout_acoes.addWidget(btnEditar)
        h_layout_acoes.addWidget(btnBorrar)
        h_layout_acoes.addStretch(1)  # Empurra os botões para a esquerda

        main_layout.addLayout(h_layout_acoes)

        ## 3. Área de Texto Grande (QTextEdit)
        self.txeClientes = QTextEdit()
        main_layout.addWidget(self.txeClientes)

        ## 4. Rodapé (Cancelar, Aceptar)
        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        h_layout_rodape = QHBoxLayout()
        h_layout_rodape.addStretch(1)  # Empurra os botões para a direita
        h_layout_rodape.addWidget(btnCancelar)
        h_layout_rodape.addWidget(btnAceptar)

        main_layout.addLayout(h_layout_rodape)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = FormularioClientes()
    janela.show()
    sys.exit(app.exec())