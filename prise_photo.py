import time, libcamera
from picamera2 import Picamera2, Preview

picam = Picamera2()

config = picam.create_preview_configuration(main={"size": (1600,1200)})
config["transform"] = libcamera.Transform()
picam.configure(config)

picam.start_preview(Preview.QTGL)

picam.start()
time.sleep(2)

timestamp = time.strftime("%Y%m%d%H%M%S")
filename = f"photo-{timestamp}.jpg"

picam.capture_file(filename)

picam.close()
