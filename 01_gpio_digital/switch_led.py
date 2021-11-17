import RPi.GPIO as GPIO

LED_PIN_1 = 12
LED_PIN_2 = 16
LED_PIN_3= 21
SWITCH_PIN_1 = 23
SWITCH_PIN_2 = 24
SWITCH_PIN_3 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1 , GPIO.OUT)
GPIO.setup(SWITCH_PIN_1 , GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_2 , GPIO.OUT)
GPIO.setup(SWITCH_PIN_2 , GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_3 , GPIO.OUT)
GPIO.setup(SWITCH_PIN_3 , GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try : 
    while True : 
        val_1 = GPIO.input(SWITCH_PIN_1) #누르지 않았을때 0 눌었을때 1
        print (val_1)
        GPIO.output(LED_PIN_1, val_1) #GPIO.HIGH = 1
        val_2 = GPIO.input(SWITCH_PIN_2) #누르지 않았을때 0 눌었을때 1
        print (val_2)
        GPIO.output(LED_PIN_2, val_2) #GPIO.HIGH = 1
        val_3 = GPIO.input(SWITCH_PIN_3) #누르지 않았을때 0 눌었을때 1
        print (val_3)
        GPIO.output(LED_PIN_3, val_3) #GPIO.HIGH = 1
finally : 
    GPIO.cleanup()
    print('cleanup and exit')