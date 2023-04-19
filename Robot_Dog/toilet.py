#importing required packages
from Servo import *
from time import sleep
from Control import *
from random import choice
import time
from threading import Timer
from Led import *
from Ultrasonic import *
import threading

#declaring variables from packages
led=Led()
ultrasonic=Ultrasonic()
control=Control()
#loop ender
hasgone = False
#60 second countdown timer
timeout = time.time() + 60
#turning on red led
led.colorWipe(led.strip, Color(255, 0, 0))

def countdown():
	#displaying on the same line the timer from 60 seconds
	for i in range(60, 0, -1):
		timer = print("Time until i need to go: ", i)
		sleep(1)
#using thread so 2 process can run at the same time
countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()

while True:
	#re-using the code from walkies file to imitate robot pacing
	ultrasonic=Ultrasonic()
	control.speed = 7
	distance = ultrasonic.getDistance()
	left = 0
	right = 0
	clear = 50
	objectDetected = 35

	if (distance < objectDetected):
		
		control.backWard()
		
		control.turnLeft()
		control.turnLeft()
		
		left = ultrasonic.getDistance()
		
		if (left > clear):
			control.forWard()
		else:
			control.turnRight()
			control.turnRight()
			control.turnRight()
			control.turnRight()
			right = ultrasonic.getDistance()
			if (right > clear):
				control.forWard()
			else:
				control.turnLeft()
				control.turnLeft()
				
				control.backWard()
				
				if (right > left):
					control.turnRight()
					control.turnRight()
					right = ultrasonic.getDistance()
					if (right > clear):
						control.forWard()
				else:
					control.turnLeft()
					control.turnLeft()
					left = ultrasonic.getDistance()
					if (left > clear):
						control.forWard()
	else:
		control.forWard()
	#stopping robot once 60 seconds passes to start new function
	if time.time() > timeout:
		break
		
def GoingForPee():
	#setting robot in relax position - all motors set at 90 degrees
	servo=Servo()
	control=Control()
	print("Too late! Going for a wee!")
	#setting led yellow to show toilet type
	led.colorWipe(led.strip, Color(255, 255, 0))
	#lifting 1 leg 90 degrees to the side to 'cock' leg
	for i in range(90):
		servo.setServoAngle(8,90+i)
		time.sleep(0.01)
	#setting robot back to relax mode and turning led off for next command
	servo=Servo()
	control=Control()
	led.colorWipe(led.strip, Color(0, 0, 0))
	#ending loop once complete
	hasgone = True

def GoingForPoo():
	#setting to relax mode
	#as advanced movement is required control is called to control all servo's
	control=Control()
	print("Too late! Going for a poo!")
	#as brown led cant be dont using rgb - i used the closest colour dark orange
	led.colorWipe(led.strip, Color(102, 90, 44))
	#pulling back legs forward
	xyz=[[-20,120,-40],[50,105,0],[50,105,0],[0,120,0]]
	for i in range(4):
		xyz[i][0]=(xyz[i][0]-control.point[i][0])/30
		xyz[i][1]=(xyz[i][1]-control.point[i][1])/30
		xyz[i][2]=(xyz[i][2]-control.point[i][2])/30
	#raising front legs
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
	time.sleep(1)
	#reset back to relax and turn off led for next command
	servo=Servo()
	control=Control()
	led.colorWipe(led.strip, Color(0, 0, 0))
	#ending loop
	hasgone = True

#placing both functions into an array
randomToilet = [GoingForPee, GoingForPoo]

#after the initial 60 seconds, 1 second later one of the functions will be called at random
timerStart = Timer(1, choice(randomToilet))
timerStart.start()
