import serial
import time
import chardet

def angulo():
    serial_port = 'COM6'
    baud_rate = 9600

    set = serial.Serial(serial_port, baud_rate, timeout=1)
    
    while True:
        
        data = set.readline().decode("utf-8", errors = "ignore").strip()

        if data:
            a = data.replace("Angle:", "")
            return a 
