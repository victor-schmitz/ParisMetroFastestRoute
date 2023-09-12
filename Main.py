import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from TELARotaMetroParis_ui import Ui_MainWindow
from RotaMetroParis import RotaMetroParis

def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(523, 563)  # Defina o tamanho fixo da janela
    
    MainWindow.show()  
    app.exec_()

if __name__ == "__main__":
    main()
