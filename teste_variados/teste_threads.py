from machine import UART, Pin
import binascii
import _thread

# arquivo = open("dados.txt", "a")

uart_sensor_wt901 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1)) #Sensor A
uart_sensor_jyme01 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9)) #Sensor B

cont = 0

def second_thread():
    while True:
        leit_ang = uart_sensor_jyme01.read()
        if leit_ang:
            print("LEITURA ANGULO: ", leit_ang.decode('utf-8'))

_thread.start_new_thread(second_thread, ())

while True:
    sensor_a = uart_sensor_wt901.read()
    # sensor_b = uart_sensor_jyme01.read()
    if sensor_a:
        print(binascii.hexlify(sensor_a).decode('utf-8'))
        
        sensor_a_decoded = binascii.hexlify(sensor_a).decode('utf-8')
        if len(sensor_a_decoded) == 88:
            
            if cont == 500:
                break
            
            print(sensor_a_decoded)
            
