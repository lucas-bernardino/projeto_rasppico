from witmotion import IMU
from time import sleep
import pandas as pd
import json
from datetime import datetime
import requests

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

flag_acel = False
flag_angle = False
flag_angular = False
flag_magnetic = False

id_cont = 0

session = requests.Session()

def callback(msg):
    
    global flag_acel
    global flag_angle
    global flag_angular
    global flag_magnetic
    
    global acel_x
    global acel_y
    global acel_z
    global temp
    global roll
    global pitch
    global yaw
    global ang_x
    global ang_y
    global ang_z
    global mag_x
    global mag_y
    global mag_z
    
    global id_cont

    if str(msg).split()[0] == "acceleration":
        acel_x = str(msg).split()[3].replace("vec:(", "")[:-1]
        acel_y = str(msg).split()[4][:-1]
        acel_z = str(msg).split()[5][:-1]
        temp = str(msg).split()[6].replace("temp_celsius:", "")
        acel_x_list.append(acel_x)
        acel_y_list.append(acel_y)
        acel_z_list.append(acel_z)
        temp_list.append(temp)
        time_now = str(datetime.now()).split()[-1].split()[-1]
        time_list.append(time_now)
        flag_acel = True

    elif str(msg).split()[0] == "angle":
        roll = str(msg).split()[3].replace("roll:", "")
        pitch = str(msg).split()[4].replace("pitch:", "")
        yaw = str(msg).split()[5].replace("yaw:", "")
        version = str(msg).split()[6].replace("version:", "")
        roll_list.append(roll)
        pitch_list.append(pitch)
        yaw_list.append(yaw)
        flag_angle = True
        

    elif str(msg).split()[0] == "angular":
        ang_x = str(msg).split()[4].replace("w:(", "")[:-1]
        ang_y = str(msg).split()[5][:-1]
        ang_z = str(msg).split()[6][:-1]
        ang_x_list.append(ang_x)
        ang_y_list.append(ang_y)
        ang_z_list.append(ang_z)
        flag_angular = True
        

    elif str(msg).split()[0] == "magnetic":
        mag_x = str(msg).split()[3].replace("vec:(", "")[:-1]
        mag_y = str(msg).split()[4][:-1]
        mag_z = str(msg).split()[5][:-1]
        mag_x_list.append(mag_x)
        mag_y_list.append(mag_y)
        mag_z_list.append(mag_z)
        flag_magnetic = True
    
        
    
    if flag_acel and flag_angle and flag_angular and flag_magnetic:
        flag_acel = False
        flag_angle = False
        flag_angular = False
        flag_magnetic = False
        data = {
            "id": id_cont,
            "acel_x": acel_x,
            "acel_y": acel_y,
            "acel_z": acel_z,
            "vel_x": ang_x,
            "vel_y": ang_y,
            "vel_z": ang_z,
            "roll": roll,
            "pitch": pitch,
            "yaw": yaw,
            "mag_x": mag_x,
            "mag_y": mag_y,
            "mag_z": mag_z,
            "temp": temp,
        }
        
        res = session.post('http://localhost:3000/enviar', json=data)
        print(res.text)
        
        id_cont += 1
        


imu = IMU("COM5") 
imu.subscribe(callback)