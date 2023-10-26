import serial
import binascii

serial_port = 'COM5'
baudrate = 9600


sensor = serial.Serial(serial_port, baudrate, timeout=1)

while True:
    read_sensor = sensor.readline()
    if read_sensor:
        print(binascii.hexlify(read_sensor).decode('utf-8'))