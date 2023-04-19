# robot_dog
Welcome to robot dog 2.0 inspired by Freenove's Robot Dog Kit for Raspberry Pi
https://github.com/Freenove/Freenove_Robot_Dog_Kit_for_Raspberry_Pi

Freenove developed a robot dog which could be controlled headless to put the user in the body of a robot dog. With the robot dog 2.0 we have taken the foundations from the predecessor and created a robot dog which can perform functions automatically - The inspiration was to simulate a real dog experience where 2 users can interact with the dog.

Has your child or partner suggested getting a dog and has had no real life experience previously with actually owning a dog?

Now with robot dog 2.0 you are in charge. With simple commands you can control the dog to perform actions a real dog would do with the other user having to respond, which the result will ensure they are truely ready to own a dog

Robot dog 2.0 requires:

1 x Micro-HDMI to HDMI cable
1 x wired keyboard
1 x wired mouse
1 x monitor or laptop
1 x micro memory card (Provided)
2 x Rechargeable batteries (Provided)
1 x USB-C cable (Provided)
1 x Red ball (Provided)

*PLEASE NOTE - Due to issues with VNC Viewer (screen sharing to allow wireless) not currently being compatible with media sharing which impacts FPS when using the camera, using a monitor to display the screen when performing operations is the perferred option.

*PLEASE NOTE - Running operations rapidly can cause the robot dog to overheat and not function as intended. Allow around 1 minute rest period before performing the next operation (This does not apply to the camera function).

*PLEASE NOTE - Please ensure the robot dog is on a solid surface at all times, away from any heights as if the robot dog falls from any heights, it could potentially break.

Robot dog 2.0 is plug and play - meaning all that is required is to connect all the devices into their allocated slots and the robot dog 2.0 is ready.

Pugging a USB-C charger into the shield (lower board) will charge the batteries when required. This takes approx. 4 hours for a full charge.

Please visit tutorial on Freenove's github to see how the robot dog can be operated manually.

HOW TO PLAY:

After connecting all the cables press the CTRL and LOAD buttons on the robot dog (2 red buttons) and check if both green lights, light up.

On the desktop press the terminal application (blue and black box with >_ in the center).
Then type or copy and paste - cd Robot_Dog

The terminal should appear to say: 

pi@raspberrypi:~/Robot_Dog $

This means you are at the right place.

Now the following commands can be entered or copy and pasted to run one of the many functions:

sudo python camera.py

This will open a window and display what the robot dog see's, after 5 seconds a picture will be taken. You can find the image by opening the folder icon and on the right clicking Robot_dog where the file called Test.jpg can be found. double click this to view the image.

sudo python video.py

Similarly to the camera, this will instead take a 10 second video. The video can be found in the same place but will be called test.h264.

sudo python alertdog.py start

The robot dog will act in the place of a security camera and activate the camera and record for 15 seconds if it detects movement in front of it. All recordings can be found in the Robot_Dog folder, and the names will display the time/date of the recording. *If this function is used often please remove any old/unwanted recordings to avoid storage issues.

sudo python goplay.py

Running this command will cause the robot dog to turn on the camera view on the monitor and will track the red ball provided. By holding the ball at the robot dog's head level and moving the ball in different directions will cause the robot dog's body to follow the ball *Ensure the room is well lit and no clear red objects in view to allow better tracking.

sudo python toilet.py

This will cause the robot dog to panic and pace around the room for 60 seconds, the time remaining can be seen in the terminal. After 60 seconds the robot dog will then do one of the following:
- Go for a pee - where it will lift one leg and a yellow led can be seen
- Go for a poo - The robot dog will take a seated position with a dark orange led.
The aim of this operation is to train the second user to stop whatever they are doing and take the robot dog to the desired toilet location in the house before 60 seconds finishes.

sudo python walkies.py

Owning a dog requires regular exersize. Running this operation will cause the robot dog to run around the room until it is satisfied (when the user ends the process pressing ctrl + c).

sudo python workout.py

Along with walking the robot dog can also work out. The terminal will ask for a number between 1-20, the robot will then perform the required amount of push ups.

sudo python attention.py

This operation requires multiple steps:

- Upload portfolio pictures of the second user into the Face_Images - Authorized folder (6 minimum but 15+ reccomended for accurate results and in different face views such as slighly angled). 
*Make sure the face is in clear view in the center of the image and is well lit.
*If you dont have acess to a camera then the camera.py operation can be used, which each image file name should be renamed to allow many images placed in the correct folder (right click file, click rename).
- Run: sudo python facetrainer.py
- Run: sudo python facerecognition.py. position the authorized user in from of the camera and check if their face gets detected as authorized.

Now running: sudo python attention.py will cause the robot dog to sit down with the camera displayed on the monitor with a red led on display. The robot dog will then wait until the authorized user is seen on the camera (ensure the room is well lit) to which it will then display a green led and wave at the user then return to a relaxed position.


*PLEASE NOTE: Entering either 'q' when the camera is used or ctrl + c in the terminal will force end any of the operations

If you wish to control the dog manually or run the robot dog without cables follow the instructions on Freenove's tutorial page (PAGE 87 and PAGE 94-100): https://github.com/Freenove/Freenove_Robot_Dog_Kit_for_Raspberry_Pi

*PLEASE NOTE: all the software and set-up has already been sorted on the raspberry dog and SHOULD NOT be tampered with. You only need to download the external client and follow the instructions for the external client.

Robot Dog 2.0 IP number for external client: 192.168.0.23
