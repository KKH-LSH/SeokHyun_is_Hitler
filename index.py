import RPi.GPIO as GPIO
import time

LED = 8
GPIO.setwarnings(False) #GPIO 사용 중 발생하는 경고 메시지 표시하지 않음
GPIO.setmode(GPIO.BOARD) #라즈베리파이에 실제로 적혀 있는 물리적인 핀 번호 사용
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW) #8번핀 출력 핀, 이니셜 - 초기설정: 로우

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)

        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt: #ctrl + C 받을 때
    GPIO.output(LED, GPIO.LOW)
