import RPi.GPIO as GPIO
import time


pins = [14,15,18,23,24]
GPIO.setmode(GPIO.BCM)
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)


for pin in pins:
	for i in range(3):
		GPIO.output(pin, GPIO.HIGH )
		time.sleep(1)
		GPIO.output(pin, GPIO.LOW )
		time.sleep(1)
