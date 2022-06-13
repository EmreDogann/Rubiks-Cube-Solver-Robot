# Update (13/6/2022):
While working on this project I decided that it would be best to work on a version 2 instead as then I could address some of the other issues I had with this initial design. So I am currently working on a version 2 of the solver. When it is ready I will be posting it to my Github as well as my [Printables page](https://www.printables.com/social/261266-dwo/about).

# Rubik Cube Solver Robot
Robot that solves any scramble given to it.

Apart from solving a scrambled Rubik's cube, the main objectives for this robot were:
- No modifications are allowed to cube in any way (no drilling holes, so sticking magnets, etc.) The cube should remain unmodified/in stock condition before and after the cube solving.
- The color detection should be an automated process, requiring no additional input/intervention from the user.

The robot is entirely 3d-printed. Housing 6 stepper motors (one for each face of the cube), 2 USB webcams + LED lights with diffusers all around for even, soft lighting. The machine is controlled by an Arduino Uno which is plugged in to a computer which has the server running on it.

The webcams capture 2 images on opposite corners of the cube, and extract the face colours using OpenCV's Python library. This colour information is encoded in a known format and is then passed into Kociemba's algorithm (using this library https://github.com/muodov/kociemba), which will output a series of face turns to perform where the end result will be a solved cube. This output information is then used to direct the Arduino on which motors to turn.

As of right now, the computer vision aspect of this project is very unreliable. The color detection has issues when there are reflections that change the lightness of the color. I have taken certain precautions both in software and on the hardware side to mitigate this (using YUV color space, having even soft lighting on the cube, etc...) but it is still unreliable. My goal in the future is to fix this while still keeping the same speed of colour detection.

WORK-IN-PROGRESS
![Image](https://user-images.githubusercontent.com/48212096/140772096-749fb196-8c32-43e2-9fe0-f88561fa48ba.png)
