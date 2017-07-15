# virtual-pen
Requirements 
1.Projector
2.Camera Capable of capturing ir radiation
The virtual pen works by tracking the tip of a pen on a white screen (illuminated by an infrared (ir) source) and projects the track of the pen in the same screen (along the actual track of the pen) using a projector. A menu is provided so that the pen can choose between colours and also clear the screen thus enabling it to be smart.

Working:
We have used an ir filter (to block all other radiations other that ir radiation ) so the camera sees only ir illimination making it easy avoid unecessary background and make the trackin easier
The process starts with taking the average of the background and then subtracting it (background subtraction)
A caliberation is done so as to define the transformation between the camera cordinates with that of the screen.This transformation is used to align the actual track of the pen with that being projected (a homomorphic transformation is used since the pen moves on a plain screen )
Once the caliberaton is done the camera starts to track the pen and and projects its track thus making it a pen 

Note please provide a switch to illuminate the ir source in the pen to avoid tracking it when not necessary
