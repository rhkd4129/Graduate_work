
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel, QPushButton,QLineEdit,
    QVBoxLayout,QGridLayout)
    
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib

import cv2
import sys
matplotlib.use('Qt5Agg')


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

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AnotherWindow()
    w.show()
    sys.exit(app.exec_())
'''
'''
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    QWidgetWindow =   QWidget()
    w = AnotherWindow()
    w.show()
    sys.exit(app.exec_())
'''

