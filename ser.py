import serial
import time 
from datetime import datetime  
import serial.tools.list_ports
import sys 

serPort = ""
int1 = 0
str1 = ""
str2 = ""

ports = list(serial.tools.list_ports.comports())
for p in ports:
   print (p)

ser = serial.Serial()
f = open('data.txt','a')

print("Enter your port , which connected arduino UNO")
ser.port = input()

print("Enter your baudRate ")
ser.baudrate = int(input())

while True:
  h1=ser.readline() 
  if h1:
   print(datetime.now())
   ss = h1.decode('utf-8')
   print(ss)


time.sleep(1)