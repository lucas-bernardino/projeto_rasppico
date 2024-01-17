import time
import threading
import serial
import binascii
import RPi.GPIO as GPIO
import datetime
import requests
import subprocess
import multiprocessing
import math
#from handle_sensors_module import *


#time.sleep(30)


sensor_gps = serial.Serial("/dev/serial0", 9600, timeout=1)
sensor_angulo = serial.Serial("/dev/ttyAMA2", 9600, timeout=11)
data_sensors = ""

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb2 in position 0: invalid start byte
# corrigir esse erro. provavelmente pode colocar um try pq so acontece na primeira vez 
# que aperta o botao

# tem que arrumar o erro que na primeria vez que começa a rodar aidna nao existe o arquivo 
# number.txt, dai ele joga um erro mas ao inves de so criar o arquivo e continuar o programa
# parece que ele roda o erro e trava ali mesmo. solucionar isso
# o erro: ERRO LINHA 29:  [Errno 2] No such file or directory: 'number.txt'

BUTTON_GPIO = 26
contador = 0
interrupt_flag = False
check_bug = True
dados_package = {}
contador_botao = 0
flag_button_collection = False

#session = requests.Session()

def button_pressed_callback(channel):
    global interrupt_flag, data_sensors, contador_botao, flag_button_collection
    interrupt_flag = not interrupt_flag
    print("Button pressed")
    current_time = datetime.datetime.now()
    print(current_time)
    print(f"Contador: {contador}")
    data_sensors = ""
    #if not flag_button_collection:
    #    new_collection = session.post("http://150.162.217.34:3001/button_pressed", json = {"contador": contador_botao})
    #    print("Resposta button pressed: ", new_collection.text)
    #    contador_botao+=1
    #flag_button_collection = not flag_button_collection
    

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, callback=button_pressed_callback, bouncetime=1000)

def ticks_ms():
    return int(time.time() * 1000)

def calculate_elapse(channel):
    global pulse, start_timer, elapse
    pulse += 1
    elapse = ticks_ms() - start_timer
    start_timer = ticks_ms()

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
pulse = 0
start_timer = ticks_ms()

HALL_PIN = 23

GPIO.setmode(GPIO.BCM)
sensor = GPIO.setup(HALL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(HALL_PIN, GPIO.FALLING, callback=calculate_elapse)

def calculate_speed(r_cm):
    global pulse, elapse, rpm, dist_km, dist_meas, km_per_hour
    if elapse != 0:
        rpm = 1 / (elapse / 60000)
        circ_cm = 2 * math.pi * r_cm
        dist_km = circ_cm / 100000
        km_per_sec = dist_km / (elapse / 1000)
        km_per_hour = km_per_sec * 3600
        dist_meas = (dist_km * pulse) * 1000
        return km_per_hour



def check_bug_timer():
    global interrupt_flag, check_bug
    if check_bug:
        #Cancelar as duas threads?
        interrupt_flag = False
        time.sleep(0.5)
        interrupt_flag = True


def core0_thread():
    global run_core_1
    global data_sensors
    global cont
    global check_bug

    while interrupt_flag:
        sensor_a = sensor_gps.read(2)
        if sensor_a:
            if binascii.hexlify(sensor_a).decode('utf-8') == "5551" :
                
                    check_bug = False
                    if not interrupt_flag:
                        data_sensors = ""
                        sensor_a = ""
                        break
                            
                    data_worthy = "5551" + binascii.hexlify(sensor_gps.read(86)).decode('utf-8')
                            
                    data_sensors = ""
                    data_sensors += data_worthy

    
    data_worthy = ""
    data_sensors = ""


def core1_thread():
    global run_core_1
    global data_sensors
    global contador
    global dados_package

    while interrupt_flag:
        sensor_b = sensor_angulo.readline()
        if sensor_b:
            try:
                sensor_b_decoded = sensor_b.decode('utf-8').replace("Angle:", "").rstrip()


                if len(data_sensors) == 176:

                    if not interrupt_flag:
                        data_sensors = ""
                        sensor_b_decoded = ""
                        break

                    #print("LEITURA HALL: ", hall.value()
                    data_sensors += (str(datetime.datetime.now())).split()[1]

                    data_sensors += sensor_b_decoded

                    if len(data_sensors) > 20:
                        calculate_speed(15)  # call this function with wheel radius as a parameter
                        hall_data = "#{:.2f}${:.2f}".format(rpm, km_per_hour)
                        data_sensors += hall_data
                        # print('rpm:{0:.0f}-RPM kmh:{1:.0f}-KMH dist_meas:{2:.2f}m pulse:{3}'.format(rpm, km_per_hour, dist_meas, pulse))
                        arquivo.write(data_sensors + "\n")
                        #print(f"DADOS COMBINADOS: {data_sensors}, horario: {datetime.datetime.now()}, cont: {contador}. Tam data sensors: {len(data_sensors)}")
                        """
                        acel_x, acel_y, acel_z, temp = handleSensor1(data_sensors[0:22])
                        vel_x, vel_y, vel_z = handleSensor2(data_sensors[22:44])
                        roll, pitch, yaw = handleSensor3(data_sensors[44:66])
                        mag_x, mag_y, mag_z = handleSensor4(data_sensors[66:88])
                        air_press, altitude = handleSensor5(data_sensors[88:110])
                        longitude, latitude = handleSensor6(data_sensors[110:132])
                        velocidade_gps = handleSensor7(data_sensors[132:154])
                        angle = data_sensors[176:]

                        dados_package = {
                        "id": contador,
                        "acel_x": acel_x,
                        "acel_y": acel_y,
                        "acel_z": acel_z,
                        "vel_x": vel_x,
                        "vel_y": vel_y,
                        "vel_z": vel_z,
                        "roll": roll,
                        "pitch": pitch,
                        "yaw": yaw,
                        "mag_x": mag_x,
                        "mag_y": mag_y,
                        "mag_z": mag_z,
                        "temp": temp,
                        "esterc": angle,
                        "rot": "999",
                        "veloc": velocidade_gps,
                        "long": longitude,
                        "lat": latitude,
                        "press_ar": air_press,
                        "altitude": altitude,
                        }
                        #post_data = session.post("http://150.162.217.34:3001/enviar", json=dados_package)
                        # #print(f"\nResposta: {req.text}\n")  
                        print(dados_package)"""

                        print("Dados: ", data_sensors)

                        contador +=1
                        
                    data_sensors = ""
            except UnicodeDecodeError:
                print("ERRO UNICODE")
                pass

    
    sensor_b_decoded = ""
    data_sensors = ""


while True:
    if interrupt_flag:
        print("entrei na interrupcao")
        data_sensors = ""

        sensor_gps.flushInput()
        sensor_gps.flushOutput()
        sensor_angulo.flushInput()
        sensor_angulo.flushOutput()


        try:
            read_number = open('number.txt', 'r')
            last_number = int(read_number.read())
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
            pass

        timer_thread = threading.Timer(1.5, check_bug_timer)  
        check_bug = True  
        timer_thread.start()
        
        thread1 = threading.Thread(target=core1_thread)
        thread1.start()

        
        core0_thread()
        
        data_sensors = ""
        print("apos as threads")

        sensor_gps.flushInput()
        sensor_gps.flushOutput()
        sensor_angulo.flushInput()
        sensor_angulo.flushOutput()

        arquivo.close()



# erro caso a rasp fique sem internet: OSError: [Errno 101] Network is unreachable

