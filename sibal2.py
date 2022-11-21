import sys
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    def init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # self.window1 = SubWindow()
        # self.window2 = SubWindow()

        layout = QVBoxLayout()


        button1 = QPushButton("Push for Window 1")
        # button1.clicked.connect(self.toggle_window1)
        layout.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        # button2.clicked.connect(self.toggle_window2)
        layout.addWidget(button2)

        self.setLayout(layout)

        self.setWindowTitle('dfdf')
        self.setGeometry(200, 200, 800, 600)
        self.show()
        

    # def toggle_window1(self, checked):
    #     if self.window1.isVisible():
    #         self.window1.hide()

    #     else:
    #         self.window1.show()

    # def toggle_window2(self, checked):
    #     if self.window2.isVisible():
    #         self.window2.hide()

    #     else:
    #         self.window2.show()


# class SubWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.setLayout(self.layout)
#         self.setGeometry(200, 200, 800, 600)

#     def initUI(self):
#         self.fig = plt.Figure()
#         self.canvas = FigureCanvas(self.fig)
        
#         layout = QVBoxLayout()
#         layout.addWidget(self.canvas)
#         cb = QComboBox()
#         cb.addItem('Graph1')
#         cb.addItem('Graph2')
#         cb.activated[str].connect(self.onComboBoxChanged)
#         layout.addWidget(cb)
#         self.layout = layout
#         self.onComboBoxChanged(cb.currentText())

#     def onComboBoxChanged(self, text):
#         if text == 'Graph1':
#             self.doGraph1()
#         elif text == 'Graph2':
#             self.doGraph2()

#     def doGraph1(self):
#         x = np.arange(0, 10, 0.5)
#         y1 = np.sin(x)
#         y2 = np.cos(x)
        
#         self.fig.clear()
#         ax = self.fig.add_subplot(111)
#         ax.plot(x, y1, label="sin(x)")
#         ax.plot(x, y2, label="cos(x)", linestyle="--")
        
#         ax.set_xlabel("x")
#         ax.set_xlabel("y")
        
#         ax.set_title("sin & cos")
#         ax.legend()
        
#         self.canvas.draw()


#     def doGraph2(self):
#         X = np.arange(-5, 5, 0.25)
#         Y = np.arange(-5, 5, 0.25)
#         X, Y = np.meshgrid(X, Y)
#         Z = X**2 + Y**2
        
#         self.fig.clear()
        
#         ax = self.fig.gca(projection='3d')
#         ax.plot_wireframe(X, Y, Z, color='black')
#         self.canvas.draw() 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    sys.exit(app.exec_())