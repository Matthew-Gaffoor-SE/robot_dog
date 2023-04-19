#Importing all packages
from Ultrasonic import *
ultrasonic=Ultrasonic()
import time
from Led import *
led=Led()
from datetime import datetime
from picamera2.encoders import H264Encoder
from picamera2 import Picamera2, Preview

#Setting camera variable and screen size
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(video_config)
encoder = H264Encoder(bitrate=10000000)
output = ".h264"
             
def test_Ultrasonic():
	try:
		#Taking the initial max distance value
		data=ultrasonic.getDistance() - 5
		print ("Obstacle distance is "+str(data)+"CM")
		while True:
			#Live reading distances to see if the second reading differs from the first
			danger=ultrasonic.getDistance()
			#If an object is detected closer from the max value
			if danger < data:
				#binding datetime to variable to save new file names seperately
				timestamp = datetime.now().strftime("%H%M%S_%d%m%y")
				#red led to show camera will start recording
				led.colorWipe(led.strip, Color(255, 0, 0)) 
				print ("Object detected at "+str(danger)+"CM Away!")
				#Opening video camera for 15 seconds and saving recording to folder
				picam2.start_preview(Preview.QTGL)
				picam2.start_recording(encoder, str(timestamp)+(output))
				time.sleep(15)
				#Stopping led and video
				led.colorWipe(led.strip, Color(0, 0, 0))
				picam2.stop_recording()
				picam2.stop_preview()
	#forcing application to close ends all processes
	except KeyboardInterrupt:
		led.colorWipe(led.strip, Color(0, 0, 0))
		print ("\nEnd of program")
        
# Main program logic follows, project starts by adding start at end of terminal command:
if __name__ == '__main__':
	print ('Program is starting ... ')
	import sys
	if sys.argv[1] == 'start':
		test_Ultrasonic()
