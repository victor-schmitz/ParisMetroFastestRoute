import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from TELARotaMetroParis_ui import Ui_MainWindow
from RotaMetroParis import RotaMetroParis
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, estacoes_conectadas):
        super().__init__() # Chamando o construtor da classe QMainWindow  
        self.setupUi(self) # Metodo gerado pelo Qt Designer para criar a interface gráfica

        self.estacoes_conectadas = estacoes_conectadas # Para usar estacoes_conectadas em toda a classe
        self.estacao_labels = {  # Dicionário que armazena os labels das estações
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

        font = QFont("Times New Roman", 12) 
        self.labelCaminho.setFont(font) # Definindo a fonte e tamanho do labelCaminho
        
        self.pushButton.clicked.connect(self.pesquisarRota) # Conectar o botão à função pesquisarRota

    def pesquisarRota(self): # Função para pesquisar a rota
        # Obtendo as estações de origem e destino selecionadas
        estacao_origem = self.comboBox.currentText()
        estacao_destino = self.comboBox_2.currentText()

        # Instância da classe RotaMetroParis
        rota_paris = RotaMetroParis()

        # Chamando a função a_estrela para encontrar o caminho mais curto
        caminho = rota_paris.a_estrela(self.estacoes_conectadas, estacao_origem, estacao_destino)            

        self.labelCaminho.setText("") # Limpando o labelCaminho

        # Verificando se um caminho foi encontrado
        if caminho:
            print("Caminho mais curto:", caminho)
            caminho_formatado = " -> ".join(caminho)  # Formatando o caminho como uma string. Exemplo: "E14 -> E13 -> E3 -> E9"
            self.labelCaminho.setText(caminho_formatado)
            self.mostrarCaminhoNoMapa(caminho)  # Chamando a função para mostrar os labels
        else:
            QMessageBox.warning(self, "Sem rota encontrada", "Não foi possível encontrar uma rota entre as estações selecionadas.", QMessageBox.Ok)

    def mostrarCaminhoNoMapa(self, caminho):
        # Ocultar todas as labels de estação
        for label in self.estacao_labels.values():
            label.setHidden(True)

        # Selecionando apenas as labels das estações no caminho
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
    # Ocultando os labels no inicio do programa
    window.labelE1.setHidden(True)  
    window.labelE2.setHidden(True)  
    window.labelE3.setHidden(True)  
    window.labelE4.setHidden(True)  
    window.labelE5.setHidden(True)  
    window.labelE6.setHidden(True) 
    window.labelE7.setHidden(True)  
    window.labelE8.setHidden(True) 
    window.labelE9.setHidden(True) 
    window.labelE10.setHidden(True) 
    window.labelE11.setHidden(True)  
    window.labelE12.setHidden(True)  
    window.labelE13.setHidden(True)  
    window.labelE14.setHidden(True) 
    window.setFixedSize(523, 670)  # Definindo o tamanho FIXO da janela
    window.show() # Exibindo a janela
    app.exec_() # Executando o programa, iniciando os eventos do Qt 

if __name__ == "__main__": # Se o programa for executado diretamente 
    main() # Chama a função main()