from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Wir benötigen eine I2C - Schnittstelle
i2c = I2C(scl=Pin(15), sda=Pin(4), freq=1000)

# Aktivieren des Moduls
pin16 = Pin(16,Pin.OUT)
pin16.on()

# Das OLED wird initialisiert
oled = SSD1306_I2C(128,64,i2c)

# Diese Funktion dient unserer Bequemlichkeit
def text_line(text, line, pos = 0):
    x = 10 * pos;
    y = (line) * 11
    oled.text(text,x,y)
    
# Das Hauptprogramm    
oled.fill(0)
text_line("Hallo! Ich bin",0,1)
text_line("ein ESP32,",1,3)
text_line("programmiert in",2,0)
text_line("Micropython",4,2)
oled.rect(0,38,128,20,1)
oled.show()
