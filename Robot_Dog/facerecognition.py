#Importing all packages
import cv2
import numpy as np
import os
from time import sleep
from PIL import Image
from picamera2 import Picamera2

#Setting up camera configurations and starting
picam=Picamera2()
picam.preview_configuration.main.size=(1280,720)
picam.preview_configuration.main.format="RGB888"
picam.preview_configuration.align()
picam.configure("preview")
picam.start()

#two face's im looking for - Elon Musk is used as a random face as 2 faces were needed
labels = ["Matthew", "Elon Musk"]

#setting up cv2 face-structure recognition
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainner.yml")

while True:
	#converting cv2 camera to picamera2 and binding all camera views to variable
	frame = picam.capture_array()
	
	#changing camera to black/white and detecting all present faces
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	#checking face diamentions for imported faces
	for (x,y,w,h) in faces:
		roi_gray = gray[y:y+h, x:x+w]
		id_, conf = recognizer.predict(roi_gray)
		#if face is present place red box and name on the persons face
		if conf>=80:
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = labels[id_]
			cv2.putText(frame, name, (x,y), font, 1, (0,0,255), 2)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
	#opening camera to view the system detecting the face
	cv2.imshow('Preview', frame)
	#pressing q ends the process
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
#closing all cameras and the programme once complete
frame.release()
cv2.destroyAllWindows()
