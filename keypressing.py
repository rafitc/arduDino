import subprocess   
import time
import pyautogui
import serial
#subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe',  #Add google chrome path for chrome users.
#    '-new-tab', 'https://chromedino.com/'])  #to open browser and open Dino game.
          								     #I'm a firefox user so, i don't have Dino game,
          								     #Here i'm using chromedino.com to play game. 
time.sleep(6)                 #give a short time to open and setup all.
print("All sett :)")

ser = serial.Serial('COM4')		#Update with your arduino [port]
ser.baudrate = '9600'			#set baudRate

while True:						# looping. 
  h1=ser.readline() 			#reading serial data. 
  if h1:
   ss = int(h1.decode('utf-8')) # encode and make a int value
   if ss== 1:					# true while obstacle. 
   	print("Oh :< Jump!! ")		
   	pyautogui.press('up') 		#Auto press [UP] key           