# QGirdLayout::addWidget(
# 	QWidget* widget,		// QGridLayout에 넣어줄 위젯
#    int fromRow,			// 어디 행에 넣을 것인지
#     int fromColumn,		// 어디 열에 넣을 것인지
#     int rowSpan,			// widget 셀의 높이 비중
#     int columnSpan,		// widget 셀의 너비 비중
#     Qt::Alignment alignment =0  // 정렬값 설정, 기본값인 0은 좌측정렬이다.
# );

import matplotlib.pyplot as plt
import matplotlib
    
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import cv2
import sys
matplotlib.use('Qt5Agg')


from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel, QPushButton,QLineEdit,
    QVBoxLayout,QGridLayout)



        # TODO:
        # TODO: 
        # FIXME: 

#from seconed_page import MplCanvas,AnotherWindow
'''
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500, 350)

        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)
'''


image1 = cv2.imread('images/1.png')    
image2 = cv2.imread('images/2.jpg')    
image3 = cv2.imread('images/3.jpg')    
image4 = cv2.imread('images/4.jpg')    
images = [image1,image2,image3,image4]
cvt_images =[]
for image in images:
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cvt_images.append(image)
    
    


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #fig ,ax= plt.subplots(1,2,figsize=(10,5))
        super(MplCanvas, self).__init__(fig)
            
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        #sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        
        sc,ax= plt.subplots(1,4)

        for i in range(4):
            ax[i].imshow(cvt_images[i])
            ax[i].set_xticks([])
            ax[i].set_yticks([])
        plt.show()
        #self.resize(700, 700)
        
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()



class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 350)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 321, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0) #행.열
        self.gridLayout.setObjectName("gridLayout")

        ################################################################################################

        self.search_image_edit = QLineEdit(self.gridLayoutWidget)
        self.search_image_edit.setObjectName("search_image_edit")
        self.gridLayout.addWidget(self.search_image_edit, 0, 0, 1, 1)

        self.number_edit = QLineEdit(self.gridLayoutWidget)
        self.number_edit.setObjectName("number_edit")
        self.gridLayout.addWidget(self.number_edit, 1, 0, 1, 1)



        #####################################  <--- label  -->  #########################################################

        # search_image 
        self.search_image_lbl = QLabel(self.gridLayoutWidget)
        self.search_image_lbl.setObjectName("search_image_lbl")
        self.gridLayout.addWidget(self.search_image_lbl, 0, 1, 1, 1)


        #number
        self.number_lbl = QLabel(self.gridLayoutWidget)
        self.number_lbl.setObjectName("number_lbl")
        self.gridLayout.addWidget(self.number_lbl, 1, 1, 1, 1)
        
        #####################################  <--- Button  -->  #########################################################

        #quit_Button
        self.quit_btn = QPushButton(self.centralwidget)
        self.quit_btn.setObjectName("quit_btn")
        self.quit_btn.setGeometry(QtCore.QRect(270, 270, 75, 23))

        self.quit_btn.setCheckable(True)


        #Input_Button
        self.Input_btn = QPushButton(self.gridLayoutWidget)
        self.Input_btn.setObjectName("Input_btn")
        self.gridLayout.addWidget(self.Input_btn, 3, 1, 1, 1)

        self.Input_btn.setCheckable(True)
        self.Input_btn.clicked.connect(self.input_btn_click)
        

    

##########################################################################################################

        MainWindow.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 21))
        #self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow) ???
        
        
############################   <--- button click event functions  --- >  ############################################################

    def input_btn_click(self, checked):
        if self.window1.isVisible():
            self.window1.hide()

        else:
            self.window1.show()

    def quit_btn_click(self):
            print('quit_btn_click')


    
    
################################<---   setText  ----> ############################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_image_lbl.setText(_translate("MainWindow", "search_image"))
        self.number_lbl.setText(_translate("MainWindow", "number"))
        self.quit_btn.setText(_translate("MainWindow", "quit"))
        self.Input_btn.setText(_translate("MainWindow", "Input"))





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
