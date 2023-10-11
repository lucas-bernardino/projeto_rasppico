import struct
import pandas as pd
from save_raw_data_pc2 import saveRawData
from handle_sensors_module import handleSensor1, handleSensor2, handleSensor3, handleSensor4

saveRawData()

number = open("number_pc.txt", "r")
    
n_times = int(number.read()[-1]) + 1

for n in range( n_times ):
    
    file = open(f'dados_pc{n}.txt', 'r')

    dados_com_n = file.readlines()
    dados_ = [dado.rstrip() for dado in dados_com_n]

    list_of_dicts = []

    contador = 0


    for data in dados_:
        try:
            if data[0:4] == "5551" and data[22:26] == "5552" and data[44:48] == "5553" and data[66:70] == "5554":
                acel_x, acel_y, acel_z, temp = handleSensor1(data[0:22])
                vel_x, vel_y, vel_z = handleSensor2(data[22:44])
                roll, pitch, yall = handleSensor3(data[44:66])
                mag_x, mag_y, mag_z = handleSensor4(data[66:])
                angle = data[88:]

                dict_data = {
                    "Aceleracao X": acel_x,
                    "Aceleracao Y": acel_y,
                    "Aceleracao Z": acel_z,
                    "Temperatura": temp,
                    "Velocidade X": vel_x,
                    "Velocidade Y": vel_y,
                    "Velocidade Z": vel_z,
                    "Roll": roll,
                    "Pitch": pitch,
                    "Yall": yall,
                    "Magnetico X": mag_x,
                    "Magnetico Y": mag_y,
                    "Magnetico Z": mag_z,
                    "Angulo": angle, 
                }
                list_of_dicts.append(dict_data)
                contador += 1
        except Exception as e:
            print(f"Erro: {e}.\n\nPosicao: {contador} ")

    df = pd.DataFrame(data=list_of_dicts)
    
    df.to_excel(f"dados{n}.xlsx", index=False)

    file.close()
    
    print(f"Script{n} finalizado.")