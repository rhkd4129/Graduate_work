## Ex 5-1. QPushButton.

import sys


from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)

        btn2 = QPushButton('&Button2', self)
        btn2.setCheckable(True)
        

        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)


        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        self.setLayout(vbox)


        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def resizeBig(self):
            self.resize(400, 500)

    def resizeSmall(self):
            self.resize(200, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())