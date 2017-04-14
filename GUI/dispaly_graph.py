import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication



import serial,random
import time
import multiprocessing

form_class, QMainWindow = uic.loadUiType("dispaly_graph.ui")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE





class container(QMainWindow, form_class):
    c=0
    list_alt=[]
    def __init__(self):
        super(container, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        fig1 = Figure(facecolor='white', edgecolor='red')
        self.canvas1 = FigureCanvas(fig1)
        self.real_display.addWidget(self.canvas1)
        self.plot_main = fig1.add_subplot('111', axisbg='white')
        self.plot_graph()
    def plot_graph(self):
        f=open("GUI.txt",'r')
        yo=[j for j in f]
        data=[x for x in yo[0].split(',')]
        print(data)
        f.close()
        if len(self.list_alt)>5:
            del(self.list_alt[0])
            #print(self.list_alt)
            self.canvas1.draw()
            self.plot_main.clear()
            self.plot_main.plot(self.list_alt,'g')
            self.plot_main.axes.get_xaxis().set_visible(False)
            self.plot_main.axes.get_yaxis().set_visible(False)
            
            
            self.list_alt.append(float (data[0]))
        else:
            self.canvas1.draw()
            self.plot_main.clear()
            self.plot_main.plot(self.list_alt,'g')
            self.list_alt.append(float(data[0]))
            
            self.plot_main.axes.get_xaxis().set_visible(False)
            self.plot_main.axes.get_yaxis().set_visible(False)
        self.label_10.setText(data[1])
        if data[1] == '!':
            data[1]=72
        else :
            data[1]=76+i
            
        self.label_11.setText(str(data[1]))
        self.label_12.setText(data[0])
        QtCore.QTimer.singleShot(100, lambda: self.plot_graph())
        
         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = container()
    dv.show()
    app.exec_()

