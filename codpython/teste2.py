# import serial
# import time
# ser = serial.Serial('COM5', 115200)
# time.sleep(2)
# ser.write(str.encode(""))
# b = ser.readline()

import serial
import time

serial_port = 'COM5'
baud_rate = 9600

set = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    with open("teste3.txt", "w") as f:

        while True:
        
            data = set.readline().decode('utf-8').strip()

            if data:
                print("Received data from serial port: ", data)
            f.write(data)
            f.write("\n")
            

except KeyboardInterrupt:
    print("Closing the serial port.")
    set.close()