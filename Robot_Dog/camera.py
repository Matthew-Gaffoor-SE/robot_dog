#importing required packages
from picamera2 import Picamera2, Preview
import time

#settimg camera variable and using custom configuration
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (1080, 720)}, display="lores")
picam2.configure(camera_config)
#opening the camera preview
picam2.start_preview(Preview.QTGL)
picam2.start()
#allowing 5 seconds before the picture is taken
time.sleep(5)
#file saved under custom name
picam2.capture_file("test.jpg")
