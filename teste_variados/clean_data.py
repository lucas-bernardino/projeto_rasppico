import struct
import pandas as pd
from save_raw_data_pc import saveRawData

saveRawData()

file = open('dados_pico.txt', 'r')

CONSTANTE_1 = 16 * 9.8 / 32768
CONSTANTE_2 = 2000 / 32768
CONSTANTE_3 = 180 / 32768
CONSTANTE_4 = 2000 / 32768


def handleSensor1(sensor_list):
  acel_x = struct.unpack(
      "<h",
      bytearray(
          [int("0x" + sensor_list[4:6], 16),
           int("0x" + sensor_list[6:8], 16)]))[0] * CONSTANTE_1
  acel_y = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[8:10], 16),
          int("0x" + sensor_list[10:12], 16)
      ]))[0] * CONSTANTE_1
  acel_z = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[12:14], 16),
          int("0x" + sensor_list[14:16], 16)
      ]))[0] * CONSTANTE_1
  temp = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[16:18], 16),
          int("0x" + sensor_list[18:20], 16)
      ]))[0] / 100

  print("Acel X: ", acel_x)
  print("Acel Y: ", acel_y)
  print("Acel Z: ", acel_z)
  print("Temp: ", temp)
  return [acel_x, acel_y, acel_z, temp]



def handleSensor2(sensor_list):
  vel_x = struct.unpack(
      "<h",
      bytearray(
          [int("0x" + sensor_list[4:6], 16),
           int("0x" + sensor_list[6:8], 16)]))[0] * CONSTANTE_2
  vel_y = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[8:10], 16),
          int("0x" + sensor_list[10:12], 16)
      ]))[0] * CONSTANTE_2
  vel_z = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[12:14], 16),
          int("0x" + sensor_list[14:16], 16)
      ]))[0] * CONSTANTE_2

  print("Velocidade Ang. X: ", vel_x)
  print("Velocidade Ang. Y: ", vel_y)
  print("Velocidade Ang. Z: ", vel_z)
  return [vel_x, vel_y, vel_z]

def handleSensor3(sensor_list):
  roll = struct.unpack(
      "<h",
      bytearray(
          [int("0x" + sensor_list[4:6], 16),
           int("0x" + sensor_list[6:8], 16)]))[0] * CONSTANTE_3
  pitch = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[8:10], 16),
          int("0x" + sensor_list[10:12], 16)
      ]))[0] * CONSTANTE_3
  yall = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[12:14], 16),
          int("0x" + sensor_list[14:16], 16)
      ]))[0] * CONSTANTE_3

  print("Roll: ", roll)
  print("Pitch: ", pitch)
  print("Yall: ", yall)
  return [roll, pitch, yall]

def handleSensor4(sensor_list):
  mag_x = struct.unpack(
      "<h",
      bytearray(
          [int("0x" + sensor_list[4:6], 16),
           int("0x" + sensor_list[6:8], 16)]))[0] * CONSTANTE_3
  mag_y = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[8:10], 16),
          int("0x" + sensor_list[10:12], 16)
      ]))[0] * CONSTANTE_3
  mag_z = struct.unpack(
      "<h",
      bytearray([
          int("0x" + sensor_list[12:14], 16),
          int("0x" + sensor_list[14:16], 16)
      ]))[0] * CONSTANTE_3


  print("Magnetico X: ", mag_x)
  print("Magnetico Y: ", mag_y)
  print("Magnetico Z: ", mag_z)
  return [mag_x, mag_y, mag_z]

cont = 0
dados_com_n = file.readlines()
dados_ = [dado.rstrip() for dado in dados_com_n]

list_of_dicts = []

for data in dados_:
  acel_x, acel_y, acel_z, temp = handleSensor1(data[0:22])
  vel_x, vel_y, vel_z = handleSensor2(data[22:44])
  roll, pitch, yall = handleSensor3(data[44:66])
  mag_x, mag_y, mag_z = handleSensor4(data[66:88])
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
  }
  list_of_dicts.append(dict_data)


df = pd.DataFrame(data=list_of_dicts)
df.to_excel("dados.xlsx", index=False)

file.close()
  
  

# AGORA, TEM QUE RETORNAR OS DADOS QUE ESTÁ SENDO CALCULADO NAS HANDLESENSORS()
# DEPOIS DISSO, TEM QUE CRIAR O DICT COM TODOS OS SENSORES E USAR O PANDAS
