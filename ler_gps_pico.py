import time
import _thread
from machine import UART, Pin
import binascii

uart_sensor_wt901 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5)) #Sensor A
uart_sensor_jyme01 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9)) #Sensor B
data_sensors = ""


button = Pin(20, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)
interrupt_flag = False
debounce_time = 0

hall = Pin(11, Pin.IN, Pin.PULL_UP)


# LIDAR COM O UnicodeError
# CORRIGIR ESSE ERRO OSError: core1 in use
# Eles acontecem sempre na primeira vez, mas não é toda vez que acontece. Aleatorio


def callback(pin):
    global interrupt_flag, debounce_time, lock
    if (time.ticks_ms()-debounce_time) > 500:
        lock.acquire()
        interrupt_flag = not interrupt_flag
        debounce_time=time.ticks_ms()
        print("Estou na CALLBACK")

        lock.release()

button.irq(trigger=Pin.IRQ_FALLING, handler=callback)

def core0_thread():

    global run_core_1
    global data_sensors
    global cont
    global lock

    while interrupt_flag:


        sensor_a = uart_sensor_wt901.read()

        if sensor_a:

            # print("ESTOU NO CORE0")

            sensor_a_decoded = binascii.hexlify(sensor_a).decode('utf-8')


            if len(sensor_a_decoded) == 88 and sensor_a_decoded[0:4] == "5551" and sensor_a_decoded[22:26] == "5552" and sensor_a_decoded[44:48] == "5553" and sensor_a_decoded[66:70] == "5554":

                lock.acquire()

                data_sensors = ""
                data_sensors += sensor_a_decoded

                lock.release()

    sensor_a_decoded = ""


cont = 0

def core1_thread():

    global run_core_1
    global data_sensors
    global cont
    global lock

    while interrupt_flag:


        sensor_b = uart_sensor_jyme01.read()

        if sensor_b:

            # print("ESTOU NO CORE1")

            sensor_b_decoded = (sensor_b.decode('utf-8')).replace("Angle:","").rstrip()

            if len(data_sensors) == 88:

                lock.acquire()

                print("LEITURA HALL: ", hall.value())

                data_sensors += sensor_b_decoded
                if len(data_sensors) > 20:

                    arquivo.write(data_sensors + "\n")
                    print("DADOS COMBINADOS: ", data_sensors)

                data_sensors = ""

                lock.release()


    sensor_b_decoded = ""
    data_sensors = ""




lock = _thread.allocate_lock()

# second_thread = _thread.start_new_thread(core1_thread, ())

# core0_thread()

while True:
    if interrupt_flag:
        print("entrei na interrupcao")

        try:
            read_number = open('number.txt', 'r')
            last_number = int(read_number.read()[-1])
            arquivo = open(f"dados{str(last_number + 1)}.txt", "a")
            write_number = open('number.txt', 'w')
            write_number.write(str(last_number + 1))
            read_number.close()
            write_number.close()
        except Exception as e:
            print(e)
            arquivo = open("dados0.txt", "a")
            write_number = open('number.txt', 'a')
            write_number.write('0')
            write_number.close()

        second_thread = _thread.start_new_thread(core1_thread, ())
        core0_thread()

        data_sensors = ""

        print("apos as threads")







# CODIG PRA HALL COM A RASP PI https://forums.raspberrypi.com/viewtopic.php?t=151465 (UTILIZA UM HALL UNIPOLAR)
