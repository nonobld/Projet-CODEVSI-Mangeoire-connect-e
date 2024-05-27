import RPi.GPIO as GPIO
import time

import libcamera
from picamera2 import Picamera2, Preview

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Trig = 23
Echo = 24
EXIT = 0

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

GPIO.output(Trig, False)

time.sleep(0.5)

picam = None

def initialize_camera():
    global picam
    picam = Picamera2()
 
def capture_photo():
    if picam is None :
        initialize_camera()
    
    picam.stop()
    config = picam.create_preview_configuration(main={"size": (1600,1200)})
    config["transform"] = libcamera.Transform()
    picam.configure(config)

    picam.start_preview(Preview.QTGL)

    picam.start()
    time.sleep(2)

    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = f"photo-{timestamp}.jpg"

    picam.capture_file(filename)
    picam.stop_preview()
    time.sleep(2)
    
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
        
        if distance <= 10 :
             capture_photo()
             time.sleep(5)



except KeyboardInterrupt:
    GPIO.cleanup()



   

   
