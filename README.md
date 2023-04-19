# robot_dog
Welcome to robot dog 2.0 inspired by Freenove's Robot Dog Kit for Raspberry Pi
https://github.com/Freenove/Freenove_Robot_Dog_Kit_for_Raspberry_Pi

Freenove developed a robot dog which can be controlled wireless. With the robot dog 2.0 we have taken the foundations from the predecessor and created a robot dog 2.0 which can perform functions automatically. The aim is to simulate a real dog experience where 2 users can interact with the robot dog 2.0.

Has your child or partner suggested getting a dog but has had no real life dog ownership experience?

Now with robot dog 2.0 it is possible to get a taste of that dog ownership experince you might be missing. With simple commands you can control the robot dog 2.0 and set it to perform actions a real dog would do. You will know if you are ready for the real deal after this experience!

Robot dog 2.0 requires:

1 x Micro-HDMI to HDMI cable
1 x wired keyboard
1 x wired mouse
1 x monitor or laptop
1 x micro memory card (Provided)
2 x Rechargeable batteries (Provided)
1 x USB-C cable (Provided)
1 x Red ball (Provided)

*PLEASE NOTE - Due to issues with VNC Viewer (screen sharing to allow wireless) not currently being compatible with media sharing (FPS impacted when using the camera), using a monitor to display the screen when performing operations is recommended.

*PLEASE NOTE - Running operations rapidly can cause the robot dog 2.0 to overheat and not function as intended. Allow 1 minute rest period before performing the next operation (This does not apply to the camera function).

*PLEASE NOTE - Please operate robot dog 2.0 on smooth floor surface only. Please ensure the robot dog 2.0 is only opearted on floor level. Falling from a height will damage the robot dog 2.0 resulting in errors. 

*PLEASE NOTE - Robot dog 2.0 is intended for inside use only. Damp conditions and water will create irreversible damage.

Robot dog 2.0 is plug and play - once the keyboard, mouse and monitor are connected the robot dog 2.0 is ready. 

Plugging a USB-C charger into the shield (lower board) will charge the batteries when required. This takes approximately 4 hours for a full charge.

Please visit tutorial on Freenove's github to see how the robot dog 2.0 can be operated manually.

HOW TO PLAY:

After connecting all the cables press the CTRL and LOAD buttons on the robot dog 2.0 (2 red buttons) and check that both LEDs light up green.

On the desktop, press the terminal application (blue and black box with >_ in the center).
Then type or copy and paste - cd Robot_Dog

The terminal should appear to say: 

pi@raspberrypi:~/Robot_Dog $

Now the following commands can be entered or copy and pasted to run one of the many functions:

sudo python camera.py

This command will open a window and display what the robot dog 2.0 sees and after 5 seconds a picture will be taken. You can find the image by opening the folder icon and selecting Robot_dog from the drop down menu on the left. The image will be labeled Test.jpg.

sudo python video.py

This command will open a window and the robot dog 2.0 will record a 10 second video clip. You can find the video by opening the folder icon and selecting Robot_dog from the drop down menu on the left. The video will be labeled Test.h264.

sudo python alertdog.py start

This command will start the security camera action, recording a 15 second video clip if the robot dog 2.0 detects any movement in its vicinity. You can find the video by opening the folder icon and selecting Robot_dog from the drop down menu on the left. These videos will be labeled with the time and date the recording was taken.
*If this function is used often please remove any old/unwanted recordings to avoid storage issues.

sudo python goplay.py

This command will turn on the camera view on the monitor and enable the robot dog 2.0 to track the red ball provided. Hold the ball in front of the robot dog 2.0 at head level. Move the ball in the right or left direction to enable the robot dog 2.0 to follow the ball. The robot dog 2.0 will walk towards the ball.
*Ensure the room is well lit and no clear red objects are in view to allow better tracking.

sudo python toilet.py

This command will make the robot dog 2.0 pace around the room for 60 seconds. The coundown can be tracked in the terminal. After 60 seconds the robot dog 2.0 will then do one of the following:
- Go for a pee - The robot dog 2.0 will lift one leg and the LED will glow yellow
- Go for a poo - The robot dog 2.0 will take a seated position and the LED will glow dark orange
The aim of this command is to ensure that the users are quick to attend to the robot dog's 2.0 needs, just as you would need to do if it was a real dog!

sudo python walkies.py

This command enables the robot dog 2.0 to run around until it is satisfied (to end the process press ctrl + c). We suggest walking with the robot dog 2.0 during this operation just as you would with a real dog. 

sudo python workout.py

This command enables the robot dog 2.0 to work out! Input a number between 1-20 and watch your robot dog 2.0 perform the set number of push ups.
*This is an extra added fun feature. Please do not expect a real dog to perform push ups. 

sudo python attention.py

This operation requires multiple steps:

- Upload photos of the user into the Face_Images - Authorized folder.
  (6 minimum but 15+ reccomended for more accurate results). 
*Make sure the face is in clear view in the center of the image and the image is well lit.
*If you don't have acess to a camera, the camera.py operation can be used. Each image file name should be renamed to allow many images placed in the correct folder (right click file, click rename).
- Run: sudo python facetrainer.py
- Run: sudo python facerecognition.py
- Position the user in front of the camera and check that the robot dog 2.0 is detecting the user's face.
- 
This command will enable the robot dog 2.0 to sit down, displaying what it sees on the monitor and the LED will glow red. The robot dog 2.0 will detect the autorised user via the camera (the LED will glow green) and wave to the authorized user. The robot dog 2.0 will then return to a neutral position.  

*PLEASE NOTE: Entering either 'q' when the camera is used or ctrl + c in the terminal will force end any of the operations.

An *optional* additional feature allows the robot dog 2.0 to recognise the user by name by doing the following (Case sensitive):
- go to following folder Robot_Dog -> Face_Images and rename the folder 'Authorized' to the users name
- In the Robot_Dog folder open facetrainer.py. On line 6 change "Authorized" to the users name
- Open attention.py. On line 22 and 76 change "Authorized" to users name
The video will now display the users name when recognized and only respond to them.

If you wish to control the robot dog 2.0 manually or run the robot dog 2.0 without cables follow the instructions on Freenove's tutorial page (PAGE 87 and PAGE 94-100): https://github.com/Freenove/Freenove_Robot_Dog_Kit_for_Raspberry_Pi

*PLEASE NOTE: All the software is installed on the robot dog 2.0 and SHOULD NOT be tampered with. You only need to download the external client and follow the instructions for the external client.

Robot Dog 2.0 IP number for external client: 192.168.0.23
