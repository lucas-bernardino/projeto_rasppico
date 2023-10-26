from machine import Pin
import time

hall = Pin(11, Pin.IN, Pin.PULL_UP)

while True:
    print(hall.value())
    time.sleep(.1)
