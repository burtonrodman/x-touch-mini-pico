import time
from machine import Pin

# led = Pin('LED', Pin.OUT)
led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
    