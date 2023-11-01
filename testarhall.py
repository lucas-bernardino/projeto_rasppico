from machine import Pin
import time

hall = Pin(6, Pin.IN, Pin.PULL_UP)

while True:
    print(hall.value())
