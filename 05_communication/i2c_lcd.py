import time
import Adafruit_DHT
import datetime
from lcd import drivers

display = drivers.Lcd()

sensor = Adafruit_DHT.DHT11
PIN = 5

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            now = datetime.datetime.now()

            printa = (now.strftime("%x%X"))
            
            display.lcd_display_string(printa,1)
            display.lcd_display_string(( f"{temperature:.1f}C,{humidity:.1f}%"), 2)

        else:
            print("Read error")
        time.sleep(1)

finally:
    print("End of Program")
    display.lcd_clear()
# try:
#     display.lcd_display_string("Hello, World!!", 1)
#     while True:
#         display.lcd_display_string("** WELCOME **", 2)
#         time.sleep(2)
#         display.lcd_display_string("   WELCOME   ", 2)
#         time.sleep(2)
# finally:
#     display.lcd_clear()
