from machine import UART
import binascii

uart = UART(0, 9600)
uart.init(9600, bits=8, parity=None, stop=1)
arquivo = open("dados.txt", "a")

cont = 0

while True:
  data = uart.read()
  if data:
    hex_str = binascii.hexlify(data).decode('utf-8')
    if len(hex_str) == 88:
      print(hex_str)
      if cont == 100:
        break
      arquivo.write(hex_str)
      arquivo.write("\n")
      cont += 1

arquivo.close()
