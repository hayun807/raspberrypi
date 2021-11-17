import RPi.GPIO as GPIO
import time
BUZZER_PIN = 2
GPIO.setmode (GPIO.BCM)
GPIO.setup (BUZZER_PIN, GPIO.OUT)

#주파수 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(50) #dutty cycle (0~100)

song = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294,392, 392, 440, 440, 392, 392, 330, 392, 330, 294, 330, 262]
jump = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 1.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5]
try:
    for i in range(25):
        pwm.ChangeFrequency(song[i])
        time.sleep(jump[i])


finally:
    pwm.stop()
    GPIO.cleanup()