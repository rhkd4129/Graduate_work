import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QVBoxLayout,QLabel,QLineEdit

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        # btn1.toggle()

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        # label1 = QLabel('one label',self)
        lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.textChanged[str].connect(self.onChanged)
        #qle의 텍스트가 바꾸면  onchanged() 메서드를 호출 

        # vbox = QVBoxLayout()
        # vbox.addWidget(btn1)

        # vbox.addWidget(btn3)
        # vbox.addWidget(lbl)
        # vbox.addWidget(label2)

        # self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    #ㄹ
    # 입력된 text를 라벨 위젯의 텍스트로 설정

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        # 텓스트의 길이에 따라 라벨의 길이를 조절

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())