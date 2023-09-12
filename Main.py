import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from TELARotaMetroParis_ui import Ui_MainWindow
from RotaMetroParis import RotaMetroParis

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, estacoes_conectadas):
        super().__init__()
        self.setupUi(self)

        self.estacoes_conectadas = estacoes_conectadas
        self.estacao_labels = {
            'E1': self.labelE1,
            'E2': self.labelE2,
            'E3': self.labelE3,
            'E4': self.labelE4,
            'E5': self.labelE5,
            'E6': self.labelE6,
            'E7': self.labelE7,
            'E8': self.labelE8,
            'E9': self.labelE9,
            'E10': self.labelE10,
            'E11': self.labelE11,
            'E12': self.labelE12,
            'E13': self.labelE13,
            'E14': self.labelE14
        }

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
            self.mostrarCaminhoNoMapa(caminho)  # Chame a função para mostrar os labels

            # Exiba o caminho na interface ou faça o que quiser com ele
        else:
            QMessageBox.warning(self, "Sem rota encontrada", "Não foi possível encontrar uma rota entre as estações selecionadas.", QMessageBox.Ok)

    def mostrarCaminhoNoMapa(self, caminho):
        # Primeiro, oculte todas as labels de estação
        for label in self.estacao_labels.values():
            label.setHidden(True)
            
        # Em seguida, mostre apenas as labels das estações no caminho
        for estacao in caminho:
            if estacao in self.estacao_labels:
                self.estacao_labels[estacao].setHidden(False)            

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
    window.labelE1.setHidden(True)  # Para ocultar o labelE1
    window.labelE2.setHidden(True)  # Para ocultar o labelE2
    window.labelE3.setHidden(True)  # Para ocultar o labelE3
    window.labelE4.setHidden(True)  # Para ocultar o labelE4
    window.labelE5.setHidden(True)  # Para ocultar o labelE5
    window.labelE6.setHidden(True)  # Para ocultar o labelE6
    window.labelE7.setHidden(True)  # Para ocultar o labelE7
    window.labelE8.setHidden(True)  # Para ocultar o labelE8
    window.labelE9.setHidden(True)  # Para ocultar o labelE9
    window.labelE10.setHidden(True)  # Para ocultar o labelE10
    window.labelE11.setHidden(True)  # Para ocultar o labelE11
    window.labelE12.setHidden(True)  # Para ocultar o labelE12
    window.labelE13.setHidden(True)  # Para ocultar o labelE13
    window.labelE14.setHidden(True)  # Para ocultar o labelE14

    estacao_labels = {
    'E1': window.labelE1,
    'E2': window.labelE2,
    'E3': window.labelE3,
    'E4': window.labelE4,
    'E5': window.labelE5,
    'E6': window.labelE6,
    'E7': window.labelE7,
    'E8': window.labelE8,
    'E9': window.labelE9,
    'E10': window.labelE10,
    'E11': window.labelE11,
    'E12': window.labelE12,
    'E13': window.labelE13,
    'E14': window.labelE14
    }

    window.setFixedSize(523, 670)  # Defina o tamanho fixo da janela
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
