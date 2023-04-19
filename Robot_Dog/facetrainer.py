#Importing required packages
import cv2
import numpy as np
import os
from PIL import Image

#variable for face-features recognition
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

#variables to declare name and id of person present
Face_ID = -1
pev_person_name = ""

#arrays of person file id number and connected faces
y_ID = []
x_train = []

#collecting all folders in the Face_Images folder - the names on the folders are the peoples names
Face_Images = os.path.join(os.getcwd(), "Face_Images")
print (Face_Images)

#searching all local folders for the requested folder
for root, dirs, files in os.walk(Face_Images):
	#only accepting the below file types of images and binding name by folder name
	for file in files:
		if file.endswith("jpeg") or file.endswith("jpg") or file.endswith("png"):
			path = os.path.join(root, file)
			person_name = os.path.basename(root)
			print (path, person_name)
			
			#if file name isnt equal to person name then assign name and id to all pictures
			if pev_person_name != person_name:
				Face_ID = Face_ID+1
				pev_person_name = person_name
				
			#cropping all images and converting to black and white
			Gery_Image = Image.open(path).convert("L")
			Crop_Image = Gery_Image.resize((550,550) , Image.ANTIALIAS)
			Final_Image = np.array(Crop_Image, "uint8")
			faces = face_cascade.detectMultiScale(Final_Image, scaleFactor=1.5, minNeighbors=5)
			
			print (Face_ID, faces)
			#binding face-structures and file name/id using haarcascade and storing process
			#in yml file - this file needs re-running every time images/people change
			for (x,y,w,h) in faces:
				roi = Final_Image[y:y+h, x:x+w]
				
				x_train.append(roi)
				
				y_ID.append(Face_ID)
		
#creating file with process
recognizer.train(x_train, np.array(y_ID))

recognizer.save("face-trainner.yml")
