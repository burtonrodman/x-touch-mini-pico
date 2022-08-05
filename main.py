from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
import utime
import gc

def drawTextLines(oled, text):
    y = 0
    oled.fill(0)
    for line in text:
        oled.text(line, 0, y); y += 8;
    oled.show()

w = 64
h = 32
x = 0

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
addr = i2c.scan()[0]
oled = SSD1306_I2C(w, h, i2c, addr)

si2c = SoftI2C(scl=Pin(21), sda=Pin(20))
saddr = si2c.scan()[0]
soled = SSD1306_I2C(w, h, si2c, saddr)

ei2c = SoftI2C(scl=Pin(13), sda=Pin(12))
eaddr = ei2c.scan()[0]
eoled = SSD1306_I2C(w, h, ei2c, eaddr)

while True:
    x += 1

    drawTextLines(oled, ["BUS13/14", "08 BURT ", "LAV GRN ", "drawBus"])
    drawTextLines(soled, ["21/20", "free mem", str(gc.mem_free()), "drawText"])
    drawTextLines(eoled, ["13/12", str(x), "", "drawText"])

    utime.sleep_ms(1)  # keep device responsive to code upload, etc...
