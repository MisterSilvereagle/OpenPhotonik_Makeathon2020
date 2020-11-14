print('\n### OpenPhotonik_Makeathon2020\n')

import time, utime
from machine_esp32_heltec_LoRa32 import *
from machine import Pin, I2C
from scd30 import SCD30
from time import sleep
from definition_led import *
from ssd1306 import SSD1306_I2C

scl_pin_scd30   = Pin(pin_I2C_SCL, Pin.IN, Pin.PULL_UP)
sda_pin_scd30   = Pin(pin_I2C_SDA, Pin.IN, Pin.PULL_UP)

reset_pin_oled = Pin(pin_OLED_RST,Pin.OUT, value=1)
scl_pin_oled   = Pin(pin_OLED_SCL, Pin.IN, Pin.PULL_UP)
sda_pin_oled   = Pin(pin_OLED_SDA, Pin.IN, Pin.PULL_UP)

i2c_scd30 = I2C(scl=scl_pin_scd30, sda=sda_pin_scd30, freq=50000)

led_off()

i2c_oled = I2C(scl=scl_pin_oled, sda=sda_pin_oled,  freq=400000)

idev_oled = i2c_oled.scan()
print("idev=");
print(idev_oled)

### debug scan i2c_scd30-bus and print found devices
idev_scd30 = i2c_scd30.scan()
print("idev= ", end='');
print(idev_scd30)
time.sleep_ms(200)

### attach to sensor
scd30 = SCD30(i2c_scd30, 0x61)
scd30.soft_reset()
time.sleep_ms(1000)

oled = SSD1306_I2C(128,64,i2c_oled)

# Diese Funktion dient unserer Bequemlichkeit
def text_line(text, line, pos = 0):
    x = 10 * pos;
    y = line * 11
    oled.text(text,x,y)

###
fw_version = scd30.get_firmware_version()
print("SCD30 Firmware Version: major=0x%02x minor=0x%02x" %  fw_version)

scd30.set_measurement_interval(2)
time.sleep_ms(100)

scd30.start_continous_measurement()
time.sleep_ms(100)

cnt = 0
err = 0
start_time = utime.ticks_ms()
while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    diff = utime.ticks_ms() - start_time
    try:
        while scd30.get_status_ready() != 1:
            time.sleep_ms(200)
        cnt += 1
        result = scd30.read_measurement()
    except OSError:
        err += 1
        result = 'skipped'
    if err:
        quot = cnt/err
    else:
        quot = 0
    print("%6d.%03d: " % (diff/1000,diff%1000), end = '')
    print("%3d/%3d/%3d, " % (cnt,err, quot), end = '')
    print( result )

    
    if result != "skipped":
        x = result[0]
       
    oled.fill(0)
    text_line("Der aktuelle Sauer-",0,1)
    text_line("stoffgehalt in",1,3)
    text_line("diesem Raum beträgt",2,0)
    text_line(str(x),4,2)
    oled.rect(0,38,128,20,1)
    oled.show()
    
    if x < 1000:
        led_color("green")
    elif (x >= 1000) and (x < 1500):
        led_color("yellow")
    elif (x >= 1500) and (x < 1800):
        led_color("red")
    elif (x >= 1800) and (x < 2000):
        led_color("red")
        blink(2)
    elif x >= 2000:
        led_color("red")
        blink(4)
    else:
        led_off()
