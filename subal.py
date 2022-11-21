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
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.resize(500,500)
        # self.label = QLabel("Another Window % d" % randint(0, 100))
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        
        # self.setCentralWidget(sc)
        # layout.addWidget(self.sc)
        # self.setLayout(self.sc)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(self.toggle_window1)
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(self.toggle_window2)
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window1(self, checked):
        if self.window1.isVisible():
            self.window1.hide()

        else:
            self.window1.show()

    def toggle_window2(self, checked):
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()