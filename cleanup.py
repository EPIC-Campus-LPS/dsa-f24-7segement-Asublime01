import RPi.GPIO as GPIO #Import Modules
list = []
for i in range(54):
    list.append(i)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(list, GPIO.OUT) #Sets GPIO pins as output
GPIO.output(list, GPIO.LOW)


