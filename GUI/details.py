import sys

from PyQt5 import  QtCore,QtGui,QtWidgets,uic
from PyQt5.QtWidgets import  QApplication

import mysql.connector
conn=mysql.connector.connect(user='root',password='devesh',host='localhost',database='GUI')
cursor = conn.cursor()


import serial,random
import time
import multiprocessing

form_class, QMainWindow = uic.loadUiType("details.ui")

from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE





class container(QMainWindow, form_class):
    c=0
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.display()
    def display(self):
        cursor = conn.cursor()
        query_1 = ("select * from address where p_id = 90002")
        query_2 = ("select * from patient where p_id = 90002")
        cursor.execute(query_1)
        c=[]
        for x in cursor:
            data=[str(i) for i in x]
        #print(data)
        self.label_29.setText(data[1])
        self.label_30.setText(data[2])
        self.label_28.setText(data[3])
        self.label_26.setText(data[4])
        self.label_27.setText(data[5])
        cursor.execute(query_2)
        c=[]
        for x in cursor:
            data=[str(i) for i in x]
        #print(data)
        self.label_17.setText(data[1])
        self.label_18.setText(data[2])
        self.label_19.setText(data[4])
        self.label_24.setText(data[3])
        self.label_21.setText(data[5])
        self.label_22.setText(data[6])
        #self.label_20.setText(data[3])
        self.label_23.setText(data[2])
        
        
        
        
         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dv = container()
    dv.show()
    app.exec_()

