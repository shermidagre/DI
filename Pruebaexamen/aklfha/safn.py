import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QTextEdit, QPushButton, QGroupBox
)
from PyQt6.QtCore import Qt


class FormularioClientes(QWidget):
    # Lista de dados fornecida no Ponto 3
    albarans = [
        ['1111nm', '02/11/2024', '1111', 'Ana', 'Ruiz'],
        ['2222io', '08/03/2024', '2222', 'Pedro', 'Diz'],
        ['3333qw', '23/10/2025', '3333', 'Rosa', 'Sanz']
    ]

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 16-11-2023 grupo A")
        self.setGeometry(100, 100, 600, 500)
        self.initUI()

    def initUI(self):
        # Layout principal da janela
        main_layout = QVBoxLayout(self)

        # ------------------ 1. Criação dos Widgets ------------------

        gpbCliente = QGroupBox("Albari")
        input_layout = QGridLayout()

        # Elementos do cabeçalho da imagem (Número Albari / Data)
        lblNumeroAlbari = QLabel("Número Albari")
        self.cmbNumeroAlbari = QComboBox()
        lblData = QLabel("Data")
        self.txtData = QLineEdit()

        # Elementos da sua lista (Número Cliente / Nome Cliente / Apelidos)
        lblNumeroCliente = QLabel("Número Cliente")
        self.txtNumeroCliente = QLineEdit()
        lblNomeCliente = QLabel("Nome Cliente")
        self.txtNomeCliente = QLineEdit()
        lblApelidosCliente = QLabel("Apelidos")
        self.txtApelidosCliente = QLineEdit()

        # Botões de Ação
        self.btnEngadir = QPushButton("Engadir")
        self.btnEditar = QPushButton("Editar")
        self.btnBorrar = QPushButton("Borrar")

        # Área de Texto
        self.txeClientes = QTextEdit()

        # Botões de Rodapé
        self.btnAceptar = QPushButton("Aceptar")
        self.btnCancelar = QPushButton("Cancelar")

        # ------------------ 2. Organização do Layout ------------------

        # Layout da área de entrada
        input_layout.addWidget(lblNumeroAlbari, 0, 0)
        input_layout.addWidget(self.cmbNumeroAlbari, 0, 1)
        input_layout.addWidget(lblData, 0, 2)
        input_layout.addWidget(self.txtData, 0, 3)

        input_layout.addWidget(lblNumeroCliente, 1, 0)
        input_layout.addWidget(self.txtNumeroCliente, 1, 1)
        input_layout.addWidget(lblNomeCliente, 1, 2)
        input_layout.addWidget(self.txtNomeCliente, 1, 3)

        input_layout.addWidget(lblApelidosCliente, 2, 0)
        input_layout.addWidget(self.txtApelidosCliente, 2, 1)

        gpbCliente.setLayout(input_layout)
        main_layout.addWidget(gpbCliente)

        # Layout dos botões de ação
        h_layout_acoes = QHBoxLayout()
        h_layout_acoes.addWidget(self.btnEngadir)
        h_layout_acoes.addWidget(self.btnEditar)
        h_layout_acoes.addWidget(self.btnBorrar)
        h_layout_acoes.addStretch(1)

        main_layout.addLayout(h_layout_acoes)

        # Área de texto
        main_layout.addWidget(self.txeClientes)

        # Layout dos botões de rodapé
        h_layout_rodape = QHBoxLayout()
        h_layout_rodape.addStretch(1)
        h_layout_rodape.addWidget(self.btnCancelar)
        h_layout_rodape.addWidget(self.btnAceptar)

        main_layout.addLayout(h_layout_rodape)

        self.setLayout(main_layout)

        # ------------------ 3. Chamadas de Funcionalidade ------------------
        self._load_albarans_to_combobox()  # Ponto 3
        self._configure_initial_state()  # Ponto 2 (Habilitar/Desabilitar botões)
        self._connect_signals()  # Ponto 2 (Cancelar) e Ponto 4, 5

    # ------------------ Implementação das Funções Solicitadas ------------------

    ## Ponto 2: Configurar estado inicial dos botões e fechar o programa

    def _configure_initial_state(self):
        """Define o estado inicial dos botões Aceptar e Cancelar."""
        # Botão Aceptar (non)
        self.btnAceptar.setEnabled(False)
        # Botão Cancelar (estea dispoñible)
        self.btnCancelar.setEnabled(True)

    def _connect_signals(self):
        """Conecta os sinais (events) dos widgets aos seus métodos."""

        # Ponto 2: Programar Cancelar para fechar a fiestra
        self.btnCancelar.clicked.connect(self.close)

        # Ponto 4: Chamar a função para carregar dados ao mudar a seleção
        self.cmbNumeroAlbari.currentIndexChanged.connect(self._fill_fields_from_selection)

        # Ponto 5: Chamar a função para processar os dados ao pulsar Editar
        self.btnEditar.clicked.connect(self._handle_editar)

        # Executar a função uma vez no início para carregar o primeiro elemento
        self._fill_fields_from_selection(0)

        ## Ponto 3: Carregar o primeiro elemento das sublistas no combo box 'Número de albará'

    def _load_albarans_to_combobox(self):
        """Carrega o primeiro elemento de cada sublista no QComboBox."""
        self.cmbNumeroAlbari.clear()  # Limpa para garantir

        for albaran in self.albarans:
            # O primeiro elemento (índice 0) é o número de albará
            self.cmbNumeroAlbari.addItem(albaran[0])

    ## Ponto 4: Programar a funcionalidade que permita introducir os campos (data, número cliente, nome cliente, apelido cliente)

    def _fill_fields_from_selection(self, index):
        """Preenche os campos QLineEdit com os dados correspondentes ao albará selecionado."""
        if 0 <= index < len(self.albarans):
            data = self.albarans[index]

            # Mapeamento dos índices da lista para os QLineEdits:
            # data[1] -> Data (txtData)
            # data[2] -> Número Cliente (txtNumeroCliente)
            # data[3] -> Nome Cliente (txtNomeCliente)
            # data[4] -> Apelidos (txtApelidosCliente)

            self.txtData.setText(data[1])
            self.txtNumeroCliente.setText(data[2])
            self.txtNomeCliente.setText(data[3])
            self.txtApelidosCliente.setText(data[4])
        else:
            # Limpa os campos se, por algum motivo, o índice for inválido (por exemplo, após um clear)
            self.txtData.clear()
            self.txtNumeroCliente.clear()
            self.txtNomeCliente.clear()
            self.txtApelidosCliente.clear()

    ## Ponto 5: Escribir o código o pulsar o botón editar, recolla o texto dos QLineEdit e o elemento do QComboBox seleccionado, e os incorpore nunha liña QLineEditTxt.

    def _handle_editar(self):
        """Recolhe os dados e os incorpora em uma nova linha no QTextEdit."""

        albaran_id = self.cmbNumeroAlbari.currentText()
        data_text = self.txtData.text()
        numero_cliente = self.txtNumeroCliente.text()
        nome_cliente = self.txtNomeCliente.text()
        apelidos = self.txtApelidosCliente.text()

        # Formata os dados em uma única linha para adicionar ao QTextEdit
        linha_formatada = (
            f"Albará: {albaran_id} | Data: {data_text} | Cliente: {numero_cliente} "
            f"- {nome_cliente} {apelidos}"
        )

        # Incorpora (append) a nova linha ao QTextEdit (self.txeClientes)
        self.txeClientes.append(linha_formatada)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = FormularioClientes()
    janela.show()
    sys.exit(app.exec())