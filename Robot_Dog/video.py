#importing required packages
from picamera2.encoders import H264Encoder
from picamera2 import Picamera2, Preview
import time

#setting camera variable with custom configuration
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(video_config)
#setting the custom feedback bitrate
encoder = H264Encoder(bitrate=10000000)
output = "test.h264"
#opening the video and recording for 10 seconds
picam2.start_preview(Preview.QTGL)
picam2.start_recording(encoder, output)
time.sleep(10)
#ending video camera and recording
picam2.stop_recording()
picam2.stop_preview()
