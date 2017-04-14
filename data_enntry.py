import serial
import time
import csv
ser = serial.Serial('com13',9600)

#reading

time.sleep(2)

while(1):
    if (ser.inWaiting()>0):
        xx=ser.readline()
        xx=xx.decode()
        print(xx)
        data=[dat for dat in xx.split(',')]
        with open('information.csv', 'a') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(data)

        
"""# writing
while(1):
    x=int(input("enter number:-"))
    ser.write(str(x).encode())
"""
