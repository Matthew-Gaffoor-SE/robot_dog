#Importing all needed packages
import math
from Control import *
from Servo import *
from Led import *
import cv2
import numpy as np
import os
from time import sleep
from PIL import Image
from picamera2 import Picamera2

#Setting camera variable and customising configurations
picam=Picamera2()
picam.preview_configuration.main.size=(1280,720)
picam.preview_configuration.main.format="RGB888"
picam.preview_configuration.align()
picam.configure("preview")
picam.start()

#The 2 names i have pre-set up for the camera to detect faces of
labels = ["Matthew", "Elon Musk"]

#Importing face-structure reader file
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainner.yml")

#Declairing variables
led=Led()
servo=Servo()
control=Control()
servo.setServoAngle(15,90)

#Variable to end loop
happy = False

while not happy:
	try:
		#setting all legs to place robot in a seated position
		xyz=[[-20,120,-40],[50,105,0],[50,105,0],[0,120,0]]
		for i in range(4):
			xyz[i][0]=(xyz[i][0]-control.point[i][0])/30
			xyz[i][1]=(xyz[i][1]-control.point[i][1])/30
			xyz[i][2]=(xyz[i][2]-control.point[i][2])/30
		for j in range(30):
			for i in range(4):
				control.point[i][0]+=xyz[i][0]
				control.point[i][1]+=xyz[i][1]
				control.point[i][2]+=xyz[i][2]
			control.run()
			time.sleep(0.02)
		x3=(80-control.point[3][0])/30
		y3=(23-control.point[3][1])/30
		z3=(0-control.point[3][2])/30
		
		#Turning red led on
		led.colorWipe(led.strip, Color(255, 0, 0))
		
		#Variable to bind all camera types together - Grey, normal
		frame = picam.capture_array()
		
		#Converting normal video to black/white
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
		#detecting facial features using diamentions
		for (x,y,w,h) in faces:
			roi_gray = gray[y:y+h, x:x+w]
			id_, conf = recognizer.predict(roi_gray)
			#if person is detected place red box whith name above on person face
			if conf>=80:
				font = cv2.FONT_HERSHEY_SIMPLEX
				name = labels[id_]
				cv2.putText(frame, name, (x,y), font, 1, (0,0,255), 2)
				#Only perform next function if the person matches my face
				if name == "Matthew":
					#Green led light up
					led.colorWipe(led.strip, Color(0, 255, 0))
					#Controlling to robot to wave using control import
					for j in range(30):
						control.point[3][0]+=x3
						control.point[3][1]+=y3
						control.point[3][2]+=z3
						control.run()
						time.sleep(0.01)
					for i in range(2):
						for i in range(92,120,1):
							servo.setServoAngle(11,i)
							time.sleep(0.01)
						for i in range(120,60,-1):
							servo.setServoAngle(11,i)
							time.sleep(0.01)
						for i in range(60,92,1):
							servo.setServoAngle(11,i)
							time.sleep(0.01)
					xyz=[[55,78,0],[55,78,0],[55,78,0],[55,78,0]]
					for i in range(4):
						xyz[i][0]=(xyz[i][0]-control.point[i][0])/30
						xyz[i][1]=(xyz[i][1]-control.point[i][1])/30
						xyz[i][2]=(xyz[i][2]-control.point[i][2])/30
					for j in range(30):
						for i in range(4):
							control.point[i][0]+=xyz[i][0]
							control.point[i][1]+=xyz[i][1]
							control.point[i][2]+=xyz[i][2]
						control.run()
						time.sleep(0.02)
					for i in range(90,130):
						servo.setServoAngle(15,i)
						time.sleep(0.02)
					for i in range(130,50,-1):
						servo.setServoAngle(15,i)
						time.sleep(0.02)
					for i in range(50,110):
						servo.setServoAngle(15,i)
						time.sleep(0.02)
					#Setting robot back into relaxed position to prevent falling over once complete
					servo=Servo()
					control=Control()
					servo.setServoAngle(15,90)	
					#ending loop once function completes
					happy = True
					led.colorWipe(led.strip, Color(0, 0, 0))
					break
			cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
		#Opening video to desktop so user can see system face testing
		cv2.imshow('Preview', frame)
		#Pressing q ends programme
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break
	#Option force end by pressing ctrl and c	
	except KeyboardInterrupt:
		("Forced End!")
		break

#CLosing camera and programme once complete
frame.release()
cv2.destroyAllWindows()
