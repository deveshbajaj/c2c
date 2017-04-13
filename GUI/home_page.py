import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication



import serial,random
import time
import multiprocessing

form_class, QMainWindow = uic.loadUiType("home_page.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE





class container(QMainWindow, form_class):
    c=0
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.label.mousePressEvent=self.C_history
        self.label_2.mousePressEvent=self.B_history
        self.label_3.mousePressEvent=self.R_time
        self.label_4.mousePressEvent=self.C_Report
    def C_history(self,event):
        Popen([executable, 'history_page.py'], creationflags=CREATE_NEW_CONSOLE)
    def B_history(self,event):
        e=1
    def R_time(self,event):
        Popen([executable, 'dispaly_graph.py'], creationflags=CREATE_NEW_CONSOLE)
    def C_Report(self,event):
        Popen([executable, 'details.py'], creationflags=CREATE_NEW_CONSOLE)
    
        
        
         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = container()
    dv.show()
    app.exec_()

