import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

LEDstatus = False

while True:
    if LEDstatus == False:
        GPIO.output(4, GPIO.HIGH)
        LEDstatus = True
    else:
        GPIO.output(4, GPIO.LOW)
        LEDstatus = False
    time.sleep(1)
    print(GPIO.input(26))
        
