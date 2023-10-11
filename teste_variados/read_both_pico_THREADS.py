from machine import UART, Pin
import binascii
import _thread

arquivo = open("dados.txt", "a")
lock = _thread.allocate_lock() # create a lock object

uart_sensor_wt901 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1)) #Sensor A
uart_sensor_jyme01 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9)) #Sensor B

cont = 0

# define a function for reading sensor A
def read_sensor_a():
    global cont
    while True:
        sensor_a = uart_sensor_wt901.read()
        if sensor_a:
            try:
                sensor_a_decoded = binascii.hexlify(sensor_a).decode('utf-8')
                if len(sensor_a_decoded) == 88 and sensor_a_decoded[0:4] == "5551" and sensor_a_decoded[22:26] == "5552" and sensor_a_decoded[44:48] == "5553" and sensor_a_decoded[66:70] == "5554":
                    # acquire the lock before writing to the file
                    lock.acquire()
                    arquivo.write(sensor_a_decoded + "\n")
                    print(sensor_a_decoded)
                    cont += 1
                    # release the lock after writing to the file
                    lock.release()
            except:
                print("Instabilidade......")

# define a function for reading sensor B
def read_sensor_b():
    global cont
    while True:
        sensor_b = uart_sensor_jyme01.read()
        if sensor_b:
            try:
                sensor_b_decoded = (sensor_b.decode('utf-8')).replace("Angle:","").rstrip()
                if len(sensor_b_decoded) > 3:
                    # acquire the lock before writing to the file
                    lock.acquire()
                    arquivo.write(sensor_b_decoded + "\n")
                    print(sensor_b_decoded)
                    cont += 1
                    # release the lock after writing to the file
                    lock.release()
            except:
                print("Instabilidade......")

# start a new thread for reading sensor A on core 1
_thread.start_new_thread(read_sensor_a, ())
# start a new thread for reading sensor B on core 0
_thread.start_new_thread(read_sensor_b, ())

# wait until cont reaches 500
while cont < 500:
    pass

arquivo.close()