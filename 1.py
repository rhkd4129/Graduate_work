import matplotlib.pyplot as plt
import cv2
image1 = cv2.imread('1.png')    
image2 = cv2.imread('2.jpg')    
image3 = cv2.imread('3.jpg')    
image4 = cv2.imread('4.jpg')    

images = [image1,image2,image3,image4]
cvt_images =[]
for image in images:
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cvt_images.append(image)
    
#img = cv2.imread('travel.jpg',0)
# img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
#plt.imshow(img,cmap = 'gray');


import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #fig ,ax= plt.subplots(1,2,figsize=(10,5))
        super(MplCanvas, self).__init__(fig)


        
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        #sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        
        sc,ax= plt.subplots(1,4)

        for i in range(4):
            ax[i].imshow(cvt_images[i])
            ax[i].set_xticks([])
            ax[i].set_yticks([])
        plt.show()
 


        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
