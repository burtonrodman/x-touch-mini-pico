from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

class Display:
    def __init__(self, sda, scl, text):
        self.sda = sda
        self.scl = scl
        self.text = text

w = 64
h = 32

x = 0

displays = [
    Display(16, 17, "16/17"),
    Display(20, 21, "20/21")
]

while True:
    x += 1
    print(x)
    for d in displays:
        i2c = I2C(0, scl=Pin(d.scl), sda=Pin(d.sda), freq=200000)
        addr = i2c.scan()[0]
        oled = SSD1306_I2C(w, h, i2c, addr)
        oled.fill(0)
        oled.text(d.text, 0, 0)
        oled.text(str(x), 0, 8)
        oled.show()

        Pin(d.scl, Pin.IN, Pin.PULL_DOWN)
        Pin(d.sda, Pin.IN, Pin.PULL_DOWN)
        
        utime.sleep(1)