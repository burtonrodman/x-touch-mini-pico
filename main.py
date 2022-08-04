from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
import utime

w = 64
h = 32
x = 0

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
addr = i2c.scan()[0]
oled = SSD1306_I2C(w, h, i2c, addr)

si2c = SoftI2C(scl=Pin(21), sda=Pin(20))
saddr = si2c.scan()[0]
soled = SSD1306_I2C(w, h, si2c, saddr)

while True:
    x += 1

    oled.fill(0)
    oled.text("BUS13/14", 0, 0)
    oled.text("08 BURT ", 0, 8)
    oled.text("LAV GRN ", 0, 16)
    oled.text("XXXXXXXX", 0, 24)
    oled.show()

    soled.fill(0)
    soled.text("21/20", 0, 0)
    soled.text(str(x), 0, 8)
    soled.show()

    utime.sleep_ms(1)