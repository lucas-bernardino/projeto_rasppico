from time import sleep
import _thread
from machine import UART, Pin
import binascii

uart_sensor_wt901 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1)) #Sensor A
uart_sensor_jyme01 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9)) #Sensor B

data_sensors = ""

arquivo = open("dados.txt", "a")

def core0_thread():
    global run_core_1
    global data_sensors
    global cont

    while True:
        sensor_a = uart_sensor_wt901.read()
        if sensor_a:
            sensor_a_decoded = binascii.hexlify(sensor_a).decode('utf-8')

            if len(sensor_a_decoded) == 88 and sensor_a_decoded[0:4] == "5551" and sensor_a_decoded[22:26] == "5552" and sensor_a_decoded[44:48] == "5553" and sensor_a_decoded[66:70] == "5554":
                # print(sensor_a_decoded)
                data_sensors = ""
                data_sensors += sensor_a_decoded
 
        # signal core 1 to run
        run_core_1 = True
 
        # wait for core 1 to finish
        # print("core 0 waiting")
        while run_core_1:
            pass 
 
cont = 0   

def core1_thread():
    global run_core_1
    global data_sensors
    global cont

    while True:
 
        # wait for core 0 to signal start
        # print("core 1 waiting")
        while not run_core_1:
            pass
        
        sensor_b = uart_sensor_jyme01.read()
        if sensor_b:
            if cont == 500: 
                arquivo.close()
                print("Programa acabou.")
                return
            sensor_b_decoded = (sensor_b.decode('utf-8')).replace("Angle:","").rstrip()
            # print(sensor_b_decoded)
            if len(data_sensors) == 88:
                data_sensors += sensor_b_decoded         
                arquivo.write(data_sensors + "\n")   
                print("DADOS COMBINADOS: ", data_sensors)
                
                data_sensors = ""
                cont+=1
 
        # signal core 0 code finished
        run_core_1 = False
 
 
# Global variable to send signals between threads
run_core_1 = False
 
second_thread = _thread.start_new_thread(core1_thread, ())
core0_thread()

