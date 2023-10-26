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

  return [mag_x, mag_y, mag_z]

# 55 56 05 8a 01 00 db 0e 00 00 24


sensor_list = "555721d512e3463e0bf076"

def handleSensor5(sensor_list):
    air_press_atm = float((int("0x" + sensor_list[10:12], 16) << 24 ) | int("0x" + sensor_list[8:10], 16) << 16  | int("0x" + sensor_list[6:8], 16) << 8  | int("0x" + sensor_list[4:6], 16)) / 101325  
    altitude_m = float((int("0x" + sensor_list[18:20], 16) << 24 ) | int("0x" + sensor_list[16:18], 16) << 16  | int("0x" + sensor_list[14:16], 16) << 8  | int("0x" + sensor_list[12:14], 16)) / 100
    
    return [altitude_m, air_press_atm]

def handleSensor6(sensor_list):
    longtitude = float((int("0x" + sensor_list[10:12], 16) << 24 ) | int("0x" + sensor_list[8:10], 16) << 16  | int("0x" + sensor_list[6:8], 16) << 8  | int("0x" + sensor_list[4:6], 16))  
    latitude = float((int("0x" + sensor_list[18:20], 16) << 24 ) | int("0x" + sensor_list[16:18], 16) << 16  | int("0x" + sensor_list[14:16], 16) << 8  | int("0x" + sensor_list[12:14], 16))
    return [longtitude, latitude]


print(handleSensor5(sensor_list))
    
# print(int(hex(0xa), 16))