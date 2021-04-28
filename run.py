import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import requests
import pykorbit

form_class = uic.loadUiType("coin.ui")[0]


class MySignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit()
        self.signal2.emit(1, 2)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.signal2.connect(self.signal2_emitted)
        mysignal.run()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))

    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted")

    @pyqtSlot(int, int)
    def signal2_emitted(self, arg1, arg2):
        print("signal2 emitted", arg1, arg2)

        #self.setGeometry(100, 200, 300, 400)
        #self.setWindowTitle("Coins")
        #self.setWindowIcon(QIcon("./image/coin.png"))

        #btn = QPushButton("monitor", self)
        #btn.move(10, 10)
        #btn.clicked.connect(self.btn_clicked)


    #def btn_clicked(self):
    #    print("monitor 클릭")

        #btn = QPushButton("search", self)
        #btn.move(10, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()