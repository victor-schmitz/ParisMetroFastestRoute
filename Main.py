import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from TELARotaMetroParis_ui import Ui_MainWindow
from RotaMetroParis import RotaMetroParis

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, estacoes_conectadas):
        super().__init__()
        self.setupUi(self)
        
        self.estacoes_conectadas = estacoes_conectadas  # Armazene as estações conectadas

        # Conecte o botão Pesquisar Rota à função de pesquisa
        self.pushButton.clicked.connect(self.pesquisarRota)

    def pesquisarRota(self):
        # Obtenha as estações de origem e destino selecionadas
        estacao_origem = self.comboBox.currentText()
        estacao_destino = self.comboBox_2.currentText()

        # Crie uma instância da classe RotaMetroParis
        rota_paris = RotaMetroParis()

        # Chame a função a_estrela para encontrar o caminho mais curto
        caminho = rota_paris.a_estrela(self.estacoes_conectadas, estacao_origem, estacao_destino)

        # Verifique se um caminho foi encontrado
        if caminho:
            print("Caminho mais curto:", caminho)
            # Exiba o caminho na interface ou faça o que quiser com ele
        else:
            QMessageBox.warning(self, "Sem rota encontrada", "Não foi possível encontrar uma rota entre as estações selecionadas.", QMessageBox.Ok)

def main():
    estacoes_conectadas = { # Estações conectadas
        'E1': {'E2': 10},
        'E2': {'E1': 10, 'E3': 8.5, 'E9': 10, 'E10': 3.5},
        'E3': {'E2': 8.5, 'E4': 6.3, 'E9': 9.4, 'E13': 18.7},
        'E4': {'E3': 6.3, 'E5': 13, 'E8': 15.3, 'E13': 12.8},
        'E5': {'E4': 13, 'E6': 3, 'E7': 2.4, 'E8': 30},
        'E6': {'E5': 3},
        'E7': {'E5': 2.4},
        'E8': {'E4': 15.3, 'E9': 9.6, 'E12': 6.4, 'E5': 30},
        'E9': {'E2': 10, 'E3': 9.4,'E11': 12.2, 'E8': 9.6},
        'E10': {'E2': 3.5},
        'E11': {'E9': 12.2},
        'E12': {'E8': 6.4},
        'E13': {'E14': 5.1, 'E3': 18.7, 'E4': 12.8},
        'E14': {'E13': 5.1}    
    }

    app = QApplication(sys.argv)
    window = MainWindow(estacoes_conectadas)
    window.setFixedSize(523, 670)  # Defina o tamanho fixo da janela
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
