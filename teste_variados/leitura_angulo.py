import machine
from binascii import hexlify

# Initialize UART for Sensor A on GP0 and GP1
uart_sensor_A = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

# Initialize UART for Sensor B on GP8 and GP9
uart_sensor_B = machine.UART(1, baudrate=9600, tx=machine.Pin(8), rx=machine.Pin(9))

while True:
    # Read data from Sensor A
    data_A = uart_sensor_A.read()  # Read up to 10 bytes
    if data_A:
        hex_str = hexlify(data_A).decode('utf-8')
        print("Data from Sensor A:", hex_str)

    # Read data from Sensor B
    data_B = uart_sensor_B.read()  # Read up to 10 bytes
    if data_B:
        # hex_str = hexlify(data_B).decode('utf-8')
        # data_B_temp = data_B.replace("b'Angle:", "")
        sensor_data_decoded = data_B.decode('utf-8')
        print(sensor_data_decoded)
        