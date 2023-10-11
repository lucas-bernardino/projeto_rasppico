from machine import UART, Pin
import binascii

uart_sensor_wt901 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1)) #Sensor A
uart_sensor_jyme01 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9)) #Sensor B

cont = 0

while True:
    sensor_a = uart_sensor_wt901.read()
    sensor_b = uart_sensor_jyme01.read()
    if sensor_a and sensor_b:
        
        sensor_a_decoded = binascii.hexlify(sensor_a).decode('utf-8')
        
        if len(sensor_a_decoded) == 88:
            
                
            if cont == 1000:
                break
            
            sensor_b_decoded = (sensor_b.decode('utf-8')).replace("Angle:","")
            
            print(sensor_b_decoded)
            
            # print(sensor_a_decoded + sensor_b_decoded)
            
            
            cont+=1

