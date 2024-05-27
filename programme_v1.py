import RPi.GPIO as GPIO
import time
import os

from subprocess import call

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Trig = 23
Echo = 24
EXIT = 0

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

GPIO.output(Trig, False)

time.sleep(0.5)

def measure_distance() :
    GPIO.output(Trig,True)
    time.sleep(0.00001)
    GPIO.output(Trig,False)

    while GPIO.input(Echo)==0:
        debutImpulsion = time.time()

    while GPIO.input(Echo)==1:
        finImpulsion = time.time()
    
    distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)
    return distance

try :
    while EXIT == 0 :
        
        distance = measure_distance()
        
        if distance <= 100 :
            timestamp = time.strftime("%Y%m%d%H%M%S")
            photo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Photo", "photo_" + timestamp)
            call(["libcamera-still -o "+photo_path+".jpg -t 100"], shell = True)
            time.sleep(20)
            distance = measure_distance()


except KeyboardInterrupt:
    GPIO.cleanup()


