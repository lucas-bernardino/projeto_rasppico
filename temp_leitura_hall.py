from machine import Pin, Timer

import time

period = 5000
counter = 0
U_min = 0

hall = Pin(10, Pin.IN, Pin.PULL_UP)

def hall_trigger(input):
    global counter
    counter +=1

def freq_update(input):
    global counter, U_min
    U_min = int(counter/(period/1000)*60)
    counter = 0

hall.irq(trigger=Pin.IRQ_FALLING, handler=hall_trigger)

timer = Timer(period=period, mode=Timer.PERIODIC, callback=freq_update)

while True:
    time.sleep(1)
    print(U_min)
