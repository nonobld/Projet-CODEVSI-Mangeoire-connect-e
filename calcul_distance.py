import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Trig = 23
Echo = 24

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

GPIO.output(Trig, False)

repet = int(input("nombre de repetitions de mesure : "))

for x in range(repet):

    time.sleep(1)

    GPIO.output(Trig,True)
    time.sleep(0.00001)
    GPIO.output(Trig,False)

    while GPIO.input(Echo)==0:
        debutImpulsion = time.time()

    while GPIO.input(Echo)==1:
        finImpulsion = time.time()
    
    distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)

    print("la distance est de : ",distance," cm")
      
GPIO.cleanup()