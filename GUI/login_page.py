import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication



import serial,random
import time
import multiprocessing

form_class, QMainWindow = uic.loadUiType("login_page.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE





class container(QMainWindow, form_class):
    c=0
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.pushButton.clicked.connect(self.log)
        self.pushButton_2.clicked.connect(self.sigup)
    def log(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == username:
            if password == password:
                Popen([executable, 'home_page.py'], creationflags=CREATE_NEW_CONSOLE)
    def sigup(self):
        Popen([executable, 'signup_page.py'], creationflags=CREATE_NEW_CONSOLE)
        
         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = container()
    dv.show()
    app.exec_()

