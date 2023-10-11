from machine import Pin
import time

interrupt_flag = True
debounce_time = 0
button = Pin(20, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

count = 0

def callback(pin):
    global interrupt_flag, debounce_time
    if (time.ticks_ms()-debounce_time) > 500:
        interrupt_flag = True
        debounce_time=time.ticks_ms()

button.irq(trigger=Pin.IRQ_FALLING, handler=callback)

while True:
    if interrupt_flag:
        interrupt_flag = False
        led.toggle()
