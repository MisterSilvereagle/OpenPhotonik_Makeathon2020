from scd30 import SCD30
from machine import Pin, I2C
from machine_esp32_heltec_LoRa32 import *
import time

reset_pin = Pin(pin_OLED_RST,Pin.OUT, value=1)
scl_pin   = Pin(pin_I2C_SCL, Pin.IN, Pin.PULL_UP)
sda_pin   = Pin(pin_I2C_SDA, Pin.IN, Pin.PULL_UP)

i2c = I2C(scl = scl_pin, sda = sda_pin, freq=50000)
scd30 = SCD30(i2c, 0x61)

print(str("SCD30 Firmware Version is: ") + str(scd30.get_firmware_version()))

scd30.start_continous_measurement()
scd30.set_measurement_interval(2)

while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    while scd30.get_status_ready() != 1:
        time.sleep_ms(200)
    print(scd30.read_measurement())