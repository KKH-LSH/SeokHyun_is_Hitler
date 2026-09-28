from flask import Flask, render_template
import RPi.GPIO as GPIO
import db_model  # DB 모델 불러오기

app = Flask(__name__)

LED_PIN = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on')
def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    db_model.add_status('on')  # DB에 저장
    return 'LED ON'

@app.route('/off')
def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    db_model.add_status('off') # DB에 저장
    return 'LED OFF'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
