from machine import UART, Pin
import binascii

arquivo = open("dados.txt", "a")

sensor = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5)) #Sensor A
# uart_sensor_jyme01 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9)) #Sensor B

cont = 0

while True:
    sensor_read = sensor.read()
    # sensor_b = uart_sensor_jyme01.read()

    if sensor_read:
        try:
            sensor_read_decoded = binascii.hexlify(sensor_read).decode('utf-8')
            if len(sensor_read_decoded) == 176 and sensor_read_decoded[0:4] == "5551" and sensor_read_decoded[22:26] == "5552" and sensor_read_decoded[44:48] == "5553" and sensor_read_decoded[66:70] == "5554":
                
                
                if cont == 50:
                    break
                
                # sensor_b_decoded = (sensor_b.decode('utf-8')).replace("Angle:","").rstrip()
                
                arquivo.write(sensor_read_decoded + "\n")
                print(sensor_read_decoded)
                cont+=1
                
                # if len(sensor_b_decoded) > 3:
                
                #     arquivo.write(sensor_read_decoded + sensor_b_decoded + "\n")
                #     print(sensor_read_decoded + sensor_b_decoded)
                #     cont+=1
        except:
            print("Instabilidade......")

arquivo.close()
