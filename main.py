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

w = 128
h = 64
# x = 0

i2c_u1 = SoftI2C(scl=Pin(5), sda=Pin(4))
addr_u1 = i2c_u1.scan()[0]
oled_u1 = SSD1306_I2C(w, h, i2c_u1, addr_u1)

i2c_u2 = SoftI2C(scl=Pin(7), sda=Pin(6))
addr_u2 = i2c_u2.scan()[0]
oled_u2 = SSD1306_I2C(w, h, i2c_u2, addr_u2)

i2c_u3 = SoftI2C(scl=Pin(9), sda=Pin(8))
addr_u3 = i2c_u3.scan()[0]
oled_u3 = SSD1306_I2C(w, h, i2c_u3, addr_u3)

i2c_u4 = I2C(1, scl=Pin(11), sda=Pin(10), freq=200000)
addr_u4 = i2c_u4.scan()[0]
oled_u4 = SSD1306_I2C(w, h, i2c_u4, addr_u4)

i2c_u5 = I2C(0, scl=Pin(13), sda=Pin(12), freq=200000)
addr_u5 = i2c_u5.scan()[0]
oled_u5 = SSD1306_I2C(w, h, i2c_u5, addr_u5)

i2c_u6 = SoftI2C(scl=Pin(15), sda=Pin(14))
addr_u6 = i2c_u6.scan()[0]
oled_u6 = SSD1306_I2C(w, h, i2c_u6, addr_u6)

i2c_u7 = SoftI2C(scl=Pin(17), sda=Pin(16))
addr_u7 = i2c_u7.scan()[0]
oled_u7 = SSD1306_I2C(w, h, i2c_u7, addr_u7)

i2c_u8 = SoftI2C(scl=Pin(27), sda=Pin(26))
addr_u8 = i2c_u8.scan()[0]
oled_u8 = SSD1306_I2C(w, h, i2c_u8, addr_u8)

i2c_u9 = SoftI2C(scl=Pin(21), sda=Pin(20))
addr_u9 = i2c_u9.scan()[0]
oled_u9 = SSD1306_I2C(w, h, i2c_u9, addr_u9)

i2c_u10 = SoftI2C(scl=Pin(19), sda=Pin(18))
addr_u10 = i2c_u10.scan()[0]
oled_u10 = SSD1306_I2C(w, h, i2c_u10, addr_u9)

while True:
    # x += 1

    drawTextLines(oled_u1, ["U1-05/04", "free mem", str(gc.mem_free()), str(addr_u1)])
    drawTextLines(oled_u2, ["U2-07/06", "free mem", str(gc.mem_free()), str(addr_u2)])
    drawTextLines(oled_u3, ["U3-09/08", "free mem", str(gc.mem_free()), str(addr_u3)])
    drawTextLines(oled_u4, ["U4-11/10", "free mem", str(gc.mem_free()), str(addr_u4)])
    drawTextLines(oled_u5, ["U5-13/12", "free mem", str(gc.mem_free()), str(addr_u5)])
    drawTextLines(oled_u6, ["U6-15/14", "free mem", str(gc.mem_free()), str(addr_u6)])
    drawTextLines(oled_u7, ["U7-17/16", "free mem", str(gc.mem_free()), str(addr_u7)])
    drawTextLines(oled_u8, ["U8-27/26", "free mem", str(gc.mem_free()), str(addr_u9)])
    drawTextLines(oled_u9, ["U9-21/20", "free mem", str(gc.mem_free()), str(addr_u9)])
    drawTextLines(oled_u10, ["U0-19/18", "free mem", str(gc.mem_free()), str(addr_u9)])

    utime.sleep_ms(1)  # keep device responsive to code upload, etc...
