from genericpath import exists
import time,os,sys

if os.path.exists('Cry.ConsoleApp.exe'):
    print('Viridian ConsoleApp Detected')
else:
    print('viridian file not found move')
    
    
while True:
    os.startfile('Cry.ConsoleApp.exe')
    print('Starting Viridian')
    #3600 is an hour
    time.sleep(3600)
    os.system('TASKKILL /F /IM Cry.ConsoleApp.exe')
    if os.path.exists('players.txt'):
        os.remove('players.txt')