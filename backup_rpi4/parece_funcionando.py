import time
import threading
import serial
import binascii
import RPi.GPIO as GPIO
import sys
import datetime

sensor_gps = serial.Serial("/dev/serial0", 9600, timeout=1)
sensor_angulo = serial.Serial("/dev/ttyAMA2", 9600, timeout=1)
data_sensors = ""

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb2 in position 0: invalid start byte
# corrigir esse erro. provavelmente pode colocar um try pq so acontece na primeira vez 
# que aperta o botao

# tem que arrumar o erro que na primeria vez que comeÃ§a a rodar aidna nao existe o arquivo 
# number.txt, dai ele joga um erro mas ao inves de so criar o arquivo e continuar o programa
# parece que ele roda o erro e trava ali mesmo. solucionar isso
# o erro: ERRO LINHA 29:  [Errno 2] No such file or directory: 'number.txt'

BUTTON_GPIO = 26
contador = 0
interrupt_flag = False

def button_pressed_callback(channel):
    global interrupt_flag
    interrupt_flag = not interrupt_flag
    print("Button pressed")
    current_time = datetime.datetime.now()
    print(current_time)
    print(f"Contador: {contador}")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback=button_pressed_callback, bouncetime=300)


def core0_thread():
    global run_core_1
    global data_sensors
    global cont
    global lock

    while interrupt_flag:
        sensor_a = sensor_gps.read(2)
        if sensor_a:
            if binascii.hexlify(sensor_a).decode('utf-8') == "5551" :
                    lock.acquire()
                            
                    data_worthy = "5551" + binascii.hexlify(sensor_gps.read(86)).decode('utf-8')
                            
                    data_sensors = ""
                    data_sensors += data_worthy

                    lock.release()

                        
    data_worthy = ""


def core1_thread():
    global run_core_1
    global data_sensors
    global lock
    global contador

    while interrupt_flag:
        sensor_b = sensor_angulo.readline()
        if sensor_b:
            sensor_b_decoded = sensor_b.decode('utf-8').replace("Angle:", "").rstrip()

            if len(data_sensors) == 176:
                lock.acquire()

                #print("LEITURA HALL: ", hall.value()
                
                data_sensors += sensor_b_decoded

                if len(data_sensors) > 20:
                    arquivo.write(data_sensors + "\n")
                    print("DADOS COMBINADOS: ", data_sensors)
                    contador +=1
                    
                data_sensors = ""

                lock.release()


    sensor_b_decoded = ""
    data_sensors = ""    

lock = threading.Lock()

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
            print("ERRO LINHA 29: ", e)
            arquivo = open("dados0.txt", "a")
            write_number = open('number.txt', 'a')
            write_number.write('0')
            write_number.close()

        thread1 = threading.Thread(target=core1_thread)
        thread1.start()
        core0_thread()
        data_sensors = ""
        print("apos as threads")
        arquivo.close()
