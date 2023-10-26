from machine import Pin, Timer

import time

period = 5000
counter = 0
U_min = 0

hall = Pin(11, Pin.IN, Pin.PULL_UP)

def hall_trigger(input):
    global counter
    counter +=1

def freq_update(input):
    global counter, U_min
    U_min = int(counter/(period/1000)*60) # RPM
    counter = 0

hall.irq(trigger=Pin.IRQ_FALLING, handler=hall_trigger)

timer = Timer(period=period, mode=Timer.PERIODIC, callback=freq_update)

while True:
    if U_min != 0:
        print(U_min)

#link de onde eu tirei esse codigo: https://www.youtube.com/watch?v=ZY6ydOIJIU4

# outro código que parece ser bom: https://github.com/robert-hh/RP2040-Examples/tree/master/pulses

# tem outro codigo que parece ser bom nesse link: https://raspberrypi.stackexchange.com/questions/62339/measure-rpm-using-hall-sensor-and-pigpio