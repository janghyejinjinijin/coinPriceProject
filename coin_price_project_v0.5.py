import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

form_class = uic.loadUiType("ui/coinPriceUi.ui")[0]

class CoinViewThread(QThread):

   coinDataSet = pyqtSignal(float, float, float, float, float, float, float, float) #타입만써주기

    def __init__(self):
        super().__init__()
        self.ticker = "BTC" #초기비트코인
        self.alive = True #스레드임

    @pyqtSignal(float, float, float, float, float, float, float, float) #타입선언
    def run(self):


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("BitCoin Price Overview")
        self.setWindowIcon(QIcon("icon/bitcoin.png"))
        self.statusBar().showMessage('ver 0.5 by Hyejin')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
