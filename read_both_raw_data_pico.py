from machine import UART, Pin
import binascii

arquivo = open("dados.txt", "a")

uart_sensor_wt901 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1)) #Sensor A
uart_sensor_jyme01 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9)) #Sensor B

cont = 0
# CUIDAR COM O LEN DE 176
while True:
    sensor_a = uart_sensor_wt901.read()
    sensor_b = uart_sensor_jyme01.read()
    # if sensor_a:
    #     print(binascii.hexlify(sensor_a).decode('utf-8'))
    
    if sensor_a and sensor_b:
        try:
            sensor_a_decoded = binascii.hexlify(sensor_a).decode('utf-8')
            if len(sensor_a_decoded) == 176 and sensor_a_decoded[0:4] == "5551" and sensor_a_decoded[22:26] == "5552" and sensor_a_decoded[44:48] == "5553" and sensor_a_decoded[66:70] == "5554":
                
                if cont == 700:
                    break
                
                sensor_b_decoded = (sensor_b.decode('utf-8')).replace("Angle:","").rstrip()
                
                if len(sensor_b_decoded) > 3:
                
                    arquivo.write(sensor_a_decoded + sensor_b_decoded + "\n")
                    print(sensor_a_decoded + sensor_b_decoded)
                    cont+=1
        except Exception as e:
            print(e)

arquivo.close()
