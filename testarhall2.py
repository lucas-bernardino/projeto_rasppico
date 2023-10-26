from machine import Pin
import time
import math

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
sensor = Pin(11, Pin.IN, Pin.PULL_UP)
pulse = 0
start_timer = time.ticks_ms()

def init_interrupt():
    sensor.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=calculate_elapse)

def calculate_elapse(pin):
    global pulse, start_timer, elapse
    pulse += 1
    elapse = time.ticks_diff(time.ticks_ms(), start_timer)
    start_timer = time.ticks_ms()

def calculate_speed(r_cm):
    global pulse, elapse, rpm, dist_km, dist_meas, km_per_hour
    if elapse != 0:
        rpm = 1 / (elapse / 60000)
        circ_cm = 2 * math.pi * r_cm
        dist_km = circ_cm / 100000
        km_per_sec = dist_km / (elapse / 1000)
        km_per_hour = km_per_sec * 3600
        dist_meas = (dist_km * pulse) * 1000
        return km_per_hour

if __name__ == '__main__':
    init_interrupt()
    while True:
        calculate_speed(20)  # call this function with wheel radius as a parameter
        print('rpm:{0:.0f}-RPM kmh:{1:.0f}-KMH dist_meas:{2:.2f}m pulse:{3}'.format(rpm, km_per_hour, dist_meas, pulse))
        time.sleep(0.1)
