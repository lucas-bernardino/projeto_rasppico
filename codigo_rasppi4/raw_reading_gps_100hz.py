import time
import threading
import serial
import binascii
import RPi.GPIO as GPIO
import datetime
import requests
import subprocess
import multiprocessing
import math


sensor_gps = serial.Serial("/dev/serial0", 115200, timeout=0.1)

unlock = bytes.fromhex('FF AA 69 88 B5')
save = bytes.fromhex('FF AA 00 00 00')

sensor_gps.write(unlock)
time.sleep(0.5)

rrate = bytes.fromhex('FF AA 03 0B 00')
sensor_gps.write(rrate)
time.sleep(0.5)

baud = bytes.fromhex('FF AA 04 06 00')
sensor_gps.write(baud)
time.sleep(0.5)

sensor_gps.write(save)
time.sleep(0.5)
print("STARTING TO READ")

tempo_inicial = (str(datetime.datetime.now())).split()[1]
sensor_gps.flushInput()
sensor_gps.flushOutput()
contador = 0
while True:
    sensor_a = sensor_gps.read(2)
    if sensor_a:
        if binascii.hexlify(sensor_a).decode('utf-8') == "5551" :
                data_worthy = "5551" + binascii.hexlify(sensor_gps.read(86)).decode('utf-8')
                print(data_worthy)
		contador +=1

tempo_final = (str(datetime.datetime.now())).split()[1]

print(f"TEMPO INICIAL: {tempo_inicial}\nTEMPO FINAL: {tempo_final}\nNUMERO DE DADOS: {contador}")
