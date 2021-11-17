import RPi.GPIO as GPIO
from flask import Flask

#Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)


LED_PIN_RED = 4
LED_PIN_BLUE = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_RED, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_BLUE, GPIO.OUT)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!</p>
        <a href="/led/redon">RED LED ON</a>
        <a href="/led/redoff">RED LED OFF</a>
        <a href="/led/blueon">BLUE LED ON</a>
        <a href="/led/blueoff">BLUE LED OFF</a>
    '''

@app.route("/led/<op>")
def led_op(op):
    if op == "redon":
        GPIO.output(LED_PIN_RED, GPIO.HIGH)
        return '''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif op == "redoff":
        GPIO.output(LED_PIN_RED, GPIO.LOW)
        return '''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
        '''
    elif op == "blueon":
        GPIO.output(LED_PIN_BLUE, GPIO.HIGH)
        return '''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif op == "blueoff":
        GPIO.output(LED_PIN_BLUE, GPIO.LOW)
        return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''


# 터미널에서 직접 실행시킨 경우
if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
# @app.route("/first")
# def first():
#     return '''
#     <p>LED ON</p>
#     <a href="/">Go Home</a>
#     '''

# @app.route("/second")
# def second():
#     return '''
#     <p>LED OFF</p>
#     <a href="/">Go Home</a>
#     '''