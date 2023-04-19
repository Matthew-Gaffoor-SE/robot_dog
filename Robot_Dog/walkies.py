#importing required packages
from Control import *
from Ultrasonic import *
import time
import sys

#setting the variables
ultrasonic = Ultrasonic()
control = Control()

while True:
	try:
		#setting speed of robot
		control.speed = 7
		#variable for distance detection
		distance = ultrasonic.getDistance()
		print("Distance: ", distance)
		#variables for object detection including direction
		left = 0
		right = 0
		clear = 50
		objectDetected = 35
		
		#if an object is closer then 35 the robot avoids by going backwards and turning
		if (distance < objectDetected):
			print ("Object Detected!")
			
			control.backWard()
			
			control.turnLeft()
			control.turnLeft()
			#checking if object is not detected on the left
			left = ultrasonic.getDistance()
			
			print ("Looking if left is clear: ", clear)
			#if not object carry on moving foward
			if (left > clear):
				control.forWard()
			else:
				#if there is, turn right to go in different direction
				#command is called 4 times to ensure robot makes a complete turn
				control.turnRight()
				control.turnRight()
				control.turnRight()
				control.turnRight()
				#checking if object is detected on the right
				right = ultrasonic.getDistance()
				print ("Looking if right is clear: ", right)
				#if not object is detected then move forward
				if (right > clear):
					control.forWard()
				else:
					#if there is an object detected turn left
					control.turnLeft()
					control.turnLeft()
					control.turnLeft()
					control.turnLeft()
					
					control.backWard()
					#checking which direction does not contain and object in the path
					#then following that path
					if (right > left):
						control.turnRight()
						control.turnRight()
						right = ultrasonic.getDistance()
						print ("Looking right: ", right)
						if (right > clear):
							control.forWard()
					else:
						control.turnLeft()
						control.turnLeft()
						left = ultrasonic.getDistance()
						print ("Looking Left: ", left)
						if (left > clear):
							control.forWard()
		else:
			#if not object is detected at all the robot will carry on moving forward
			print ("Going Forwards!")
			control.forWard()
	#pressing ctrl + c will end the process
	except KeyboardInterrupt:
		("Stopping Walk!")
		control.relax()
		break
