import serial
import time
import chardet

serial_port = 'COM5'
baud_rate = 9600

set = serial.Serial(serial_port, baud_rate, timeout=1)

print("rodando wt901")

try:
    with open("teste5.txt", "w") as f:

        while True:
        
            # print("linha 16")

            data = set.readline().strip()

            print(data)

            # print("Tamanho de data: ", len(data))

            # for d, index in enumerate(data):
            #     print("Data: ", index)
            #     print(d)
            
            # print("----------------------------------------")

            # if len(data) == 11:
            #     print(data)
                
            #     f.write(str(data))
            #     f.write("\n")
            

except KeyboardInterrupt:
    print("Closing the serial port.")
    set.close()