#importing required packages
import math
from Control import *
from Servo import *

#setting variables and ensuring robot is in relax position to ensure the fuction
#runs without error - such as the robot falling over
servo=Servo()
control=Control()
servo.setServoAngle(15,90)

while True:
	#asking for user input for a number between 1-20 - 20 was set as max to avoid overheating
	#the robot
	try:
		question = int(input("Chose the amount of push ups between 1-20: "))
	except ValueError:
		print ('Value must be a number.')
	else:
		if 1 <= question <= 20:
			break
		else:
			print ('Value must be between 1-20.')

#setting the back legs to extend backwards
xyz=[[0,50,0],[-100,23,0],[-100,23,0],[0,50,0]]
for i in range(4):
	xyz[i][0]=(xyz[i][0]-control.point[i][0])/30
	xyz[i][1]=(xyz[i][1]-control.point[i][1])/30
	xyz[i][2]=(xyz[i][2]-control.point[i][2])/30
#setting front legs to set for push ups
for j in range(30):
	for i in range(4):
		control.point[i][0]+=xyz[i][0]
		control.point[i][1]+=xyz[i][1]
		control.point[i][2]+=xyz[i][2]
	control.run()
	time.sleep(0.01)
#the int in the range is the total value of movement - this function is in control of the
#push up movement so the user input variable is called to set the push up amount
for i in range(question): #HERE I THINK!
	for i in range(50,120,1):
		control.point[0][1]=i
		control.point[3][1]=i
		control.run()
	for i in range(120,50,-1):
		control.point[0][1]=i
		control.point[3][1]=i
		control.run()
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
	time.sleep(0.01)
#setting robot back into relax position
servo=Servo()
control=Control()
