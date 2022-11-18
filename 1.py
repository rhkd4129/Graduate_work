import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1',self)
        btn1.setCheckable(True)
        #pixed True 설정시 누른 상태와 그렇지 않은 상태를 구분한다, 
        btn1.toggle() 
        # 상태를 바꾼다
        
        btn2 = QPushButton(self)
        btn2.setText('Button&2')
        btn2.setToolTip('This is a Putsh ')

        btn3= QPushButton('&Button3',self)
        btn3.setEnabled(False)
        #Fasle 설정시 버튼을 사용할 수 없다, 

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)



        self.setWindowTitle('My First Application')
        self.move(700, 0)
        self.resize(400, 400)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())