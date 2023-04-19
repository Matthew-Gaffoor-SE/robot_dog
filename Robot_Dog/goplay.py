#importing all required packages
import os
import cv2
from PID import *
import numpy as np
from PIL import Image
from Command import COMMAND as cmd
from picamera2 import Picamera2
from Control import *

#camera variable with custom configuration and starting
control = Control()
picam=Picamera2()
picam.preview_configuration.main.size=(1280,720)
picam.preview_configuration.main.format="RGB888"
picam.preview_configuration.align()
picam.configure("preview")
picam.start()


while True:
	#updating loop feedback as robot runs
	pid=Incremental_PID(1,0,0.0025)
	#binding all camera types in frame variable
	frame = picam.capture_array()

	#balls radius and its darkest/lighest colour tone
	MIN_RADIUS=10
	#red
	THRESHOLD_LOW = (0, 200, 200)
	THRESHOLD_HIGH = (5,255,255)

	#creating blur, hsv, black/white camera views to isolate ball colour from frame
	img_filter = cv2.GaussianBlur(frame, (3, 3), 0)
	img_filter = cv2.cvtColor(img_filter, cv2.COLOR_BGR2HSV)
	img_binary = cv2.inRange(img_filter.copy(), THRESHOLD_LOW, THRESHOLD_HIGH)
	img_binary = cv2.dilate(img_binary, None, iterations = 1)
	contours = cv2.findContours(img_binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	radius = 0
	#searching for ball in frame
	if len(contours) > 0:
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		if M["m00"] > 0:
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			if radius < MIN_RADIUS:
				center = None
	#if ball is detected track placement in frame
	if center != None:
		cv2.circle(frame, center, int(radius), (0, 255, 0))
		D=round(2700/(2*radius))  #CM
		x=pid.PID_compute(center[0])
		d=pid.PID_compute(D)
		#changing robots direction based on balls position in frame
		if radius>15:
			if d < 20:
				control.backWard()
				print ("Going Backwards!")
			elif d > 30:
				control.forWard()
				print ("Going Forwards!")
			else:
				if x < 70:
					control.turnLeft()
					control.turnLeft()
					print ("Turning Left!")
				elif x>270:
					control.turnRight()
					control.turnRight()
					print ("Turning Right")
				else:
					control.stop()
					print ("Stopping!")
	else:
		control.stop()
		print ("Stopping!")
		
	#opening camera to display what robot see's
	cv2.imshow('Preview', frame)
	#pressing q ends process
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

#closing frame and process once complete
frame.release()
cv2.destroyAllWindows()
