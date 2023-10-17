from witmotion import IMU
from time import sleep
import pandas as pd
import json
from datetime import datetime

acel_x_list = []
acel_y_list = []
acel_z_list = []
temp_list = []
roll_list = []
pitch_list = []
yaw_list = []
ang_x_list = []
ang_y_list = []
ang_z_list = []
mag_x_list = []
mag_y_list = []
mag_z_list = []
all_lists = []
time_list = []

TAMANHO = 4*40

def callback(msg):

    if str(msg).split()[0] == "acceleration" :
        acel_x = str(msg).split()[3].replace("vec:(", "")[:-1]
        acel_y = str(msg).split()[4][:-1]
        acel_z = str(msg).split()[5][:-1]
        temp = str(msg).split()[6].replace("temp_celsius:", "")
        print("Aceleração x: ", acel_x)
        print("Aceleração y: ", acel_y)
        print("Aceleração z: ", acel_z)
        print("Temperatura: ", temp)
        acel_x_list.append(acel_x)
        acel_y_list.append(acel_y)
        acel_z_list.append(acel_z)
        temp_list.append(temp)
        time_now = str(datetime.now()).split()[-1].split()[-1]
        time_list.append(time_now)

    elif str(msg).split()[0] == "angle":
        roll = str(msg).split()[3].replace("roll:", "")
        pitch = str(msg).split()[4].replace("pitch:", "")
        yaw = str(msg).split()[5].replace("yaw:", "")
        version = str(msg).split()[6].replace("version:", "")
        roll_list.append(roll)
        pitch_list.append(pitch)
        yaw_list.append(yaw)
        print("Roll:", roll)
        print("Pitch:", pitch)
        print("Yaw:", yaw)
        print("Version:", version)

    elif str(msg).split()[0] == "angular":
        ang_x = str(msg).split()[4].replace("w:(", "")[:-1]
        ang_y = str(msg).split()[5][:-1]
        ang_z = str(msg).split()[6][:-1]
        ang_x_list.append(ang_x)
        ang_y_list.append(ang_y)
        ang_z_list.append(ang_z)
        print("Velocidade Angular x: ", ang_x)
        print("Velocidade Angular y: ", ang_y)
        print("Velocidade Angular z: ", ang_z)

    elif str(msg).split()[0] == "magnetic":
        mag_x = str(msg).split()[3].replace("vec:(", "")[:-1]
        mag_y = str(msg).split()[4][:-1]
        mag_z = str(msg).split()[5][:-1]
        mag_x_list.append(mag_x)
        mag_y_list.append(mag_y)
        mag_z_list.append(mag_z)
        print("Campo Magnetico x: ", mag_x)
        print("Campo Magnetico y: ", mag_y)
        print("Campo Magnetico z: ", mag_z)
    
    if len(temp_list) == TAMANHO:

        all_lists = [acel_x_list, acel_y_list, acel_z_list, temp_list, roll_list, pitch_list, yaw_list, ang_x_list, ang_y_list,
                     ang_z_list, mag_x_list, mag_y_list, mag_z_list, time_list]

        for d in all_lists:
            if len(d) == TAMANHO:
                d.pop()

        data = {
            "Aceleração X": acel_x_list,
            "Aceleração Y": acel_y_list,
            "Aceleração Z": acel_z_list,
            "Temperatura": temp_list,
            "Roll": roll_list,
            "Pitch": pitch_list,
            "Yaw": yaw_list,
            "Velocidade Angular X": ang_x_list,
            "Velocidade Angular Y": ang_y_list,
            "Velocidade Angular Z": ang_z_list,
            "Campo Magnetico X: ": mag_x_list,
            "Campo Magnetico Y: ": mag_y_list,
            "Campo Magnetico Z: ": mag_z_list,
            "Tempo: ": time_list
        }
        
        df = pd.DataFrame(data)
        df.to_excel("dados_excelreal2.xlsx", index=False)
        print(df)
        sleep(30)


imu = IMU("COM5") 
imu.subscribe(callback)
