
from visual import *
from copy import deepcopy
import serial
import string
import math
from time import time
from time import sleep



grad2rad = 3.141592/180.0
degree2rad = 0.0174533
# Check your COM port and baud rate
ser = serial.Serial(port='COM5',baudrate=115200, timeout=1)

def cos_sign(angle):
    if angle < 90*degree2rad and angle >= -90*degree2rad:
        return cos(angle)
    elif angle >= 90*degree2rad and angle < 270*degree2rad:
        return -cos(angle)
    elif angle < -90*degree2rad and angle > -270*degree2rad:
        return -cos(angle)
    else:
        return cos(angle)

def move_spine(scene):
    scene.select()
    y1 = l*sin(theta1)
    x1 = l*cos_sign(theta1)

    y2 = y1+l*sin(theta2)
    x2 = x1+l*cos_sign(theta2)
    
    y3 = y2+l*sin(theta3)
    x3 = x2+l*cos_sign(theta3)

    pos1 = (0,-x1,y1)
    pos2 = (0,-x2,y2)
    pos3 = (0,-x3,y3)

    part1.pos = pos1
    part2.pos = pos2
    part3.pos = pos3

#obj.rotate(angle=pi/4, axis=axis, origin=pos)

    spine.pos=[(0,0,0),(0,-x1,y1),(0,-x2,y2),(0,-x3,y3)]


def animate_object(scene):
    scene.select()
    axis=(cos(pitch)*cos(yaw),-cos(pitch)*sin(yaw),sin(pitch)) 
    up=(sin(roll)*sin(yaw)+cos(roll)*sin(pitch)*cos(yaw),sin(roll)*cos(yaw)-cos(roll)*sin(pitch)*sin(yaw),-cos(roll)*cos(pitch))
    platform.axis=axis
    platform.up=up
    platform.length=1.0
    platform.width=0.65
    plat_arrow.axis=axis
    plat_arrow.up=up
    plat_arrow.length=0.8
    p_line.axis=axis
    p_line.up=up
    cil_roll.axis=(0.2*cos(roll),0.2*sin(roll),0)
    cil_roll2.axis=(-0.2*cos(roll),-0.2*sin(roll),0)
    cil_pitch.axis=(0.2*cos(pitch),0.2*sin(pitch),0)
    cil_pitch2.axis=(-0.2*cos(pitch),-0.2*sin(pitch),0)
    arrow_course.axis=(0.2*sin(yaw),0.2*cos(yaw),0)
    L1.text = str(float(words[0]))
    L2.text = str(float(words[1]))
    L3.text = str(float(words[2])) 
    return

# Main scene
scene1=display(title="WOW WHAT A GREAT SPINE")
scene1.range=(1.2,1.2,1.2)
#scene.forward = (0,-1,-0.25)
scene1.forward = (1,0,-0.25)
scene1.up=(0,0,1)

# Second scene (Roll, Pitch, Yaw)
scene2 = display(title='NICE SPINE',x=0, y=0, width=500, height=200,center=(0,0,0), background=(0,0,0))
scene2.range=(1,1,1)
scene.width=500
scene.y=200

scene2.select()
#Roll, Pitch, Yaw
cil_roll = cylinder(pos=(-0.4,0,0),axis=(0.2,0,0),radius=0.01,color=color.red)
cil_roll2 = cylinder(pos=(-0.4,0,0),axis=(-0.2,0,0),radius=0.01,color=color.red)
cil_pitch = cylinder(pos=(0.1,0,0),axis=(0.2,0,0),radius=0.01,color=color.green)
cil_pitch2 = cylinder(pos=(0.1,0,0),axis=(-0.2,0,0),radius=0.01,color=color.green)
#cil_course = cylinder(pos=(0.6,0,0),axis=(0.2,0,0),radius=0.01,color=color.blue)
#cil_course2 = cylinder(pos=(0.6,0,0),axis=(-0.2,0,0),radius=0.01,color=color.blue)
arrow_course = arrow(pos=(0.6,0,0),color=color.cyan,axis=(-0.2,0,0), shaftwidth=0.02, fixedwidth=1)

#Roll,Pitch,Yaw labels
label(pos=(-0.4,0.3,0),text="Roll",box=0,opacity=0)
label(pos=(0.1,0.3,0),text="Pitch",box=0,opacity=0)
label(pos=(0.55,0.3,0),text="Yaw",box=0,opacity=0)
label(pos=(0.6,0.22,0),text="N",box=0,opacity=0,color=color.yellow)
label(pos=(0.6,-0.22,0),text="S",box=0,opacity=0,color=color.yellow)
label(pos=(0.38,0,0),text="W",box=0,opacity=0,color=color.yellow)
label(pos=(0.82,0,0),text="E",box=0,opacity=0,color=color.yellow)
label(pos=(0.75,0.15,0),height=7,text="NE",box=0,color=color.yellow)
label(pos=(0.45,0.15,0),height=7,text="NW",box=0,color=color.yellow)
label(pos=(0.75,-0.15,0),height=7,text="SE",box=0,color=color.yellow)
label(pos=(0.45,-0.15,0),height=7,text="SW",box=0,color=color.yellow)

L1 = label(pos=(-0.4,0.22,0),text="-",box=0,opacity=0)
L2 = label(pos=(0.1,0.22,0),text="-",box=0,opacity=0)
L3 = label(pos=(0.7,0.3,0),text="-",box=0,opacity=0)

# Main scene objects
scene.select()
# Reference axis (x,y,z)
arrow(color=color.green,axis=(1,0,0), shaftwidth=0.02, fixedwidth=1)
arrow(color=color.green,axis=(0,-1,0), shaftwidth=0.02 , fixedwidth=1)
arrow(color=color.green,axis=(0,0,-1), shaftwidth=0.02, fixedwidth=1)
# labels
label(pos=(0,0,0.8),text="Pololu MinIMU-9 + Arduino AHRS",box=0,opacity=0)
label(pos=(1,0,0),text="X",box=0,opacity=0)
label(pos=(0,-1,0),text="Y",box=0,opacity=0)
label(pos=(0,0,-1),text="Z",box=0,opacity=0)
# IMU object
platform = box(length=1, height=0.05, width=1, color=color.blue)
p_line = box(length=1,height=0.08,width=0.1,color=color.yellow)
plat_arrow = arrow(color=color.green,axis=(1,0,0), shaftwidth=0.06, fixedwidth=1)

#scene3 = mydeepcopy(scene)

scene3=display(title="MOTUS S", x=600, y=600)
scene3.range=(3,3,3)
#scene.forward = (0,-1,-0.25)
scene3.forward = (1,0,-0.25)
scene3.up=(0,0,1)
scene3.width=500
scene3.y=200
scene3.select()
# Reference axis (x,y,z)
arrow(color=color.green,axis=(1,0,0), shaftwidth=0.02, fixedwidth=1)
arrow(color=color.green,axis=(0,-1,0), shaftwidth=0.02 , fixedwidth=1)
arrow(color=color.green,axis=(0,0,-1), shaftwidth=0.02, fixedwidth=1)
#part1 = cylinder(pos=(0,0,0),axis=(0,-1,1),radius=0.01,color=color.red,length=1)
#part2 = cylinder(pos=(0,-1/sqrt(2),1/sqrt(2)),axis=(0,1,1),radius=0.01,color=color.red,length=1)
#part3 = cylinder(pos=(0,0,2/sqrt(2)),axis=(0,-1,1),radius=0.01,color=color.red,length=1)
part1 = sphere(pos=(0,0,0),axis=(0,-1,1),radius=0.03,color=color.red,length=1)
part2 = sphere(pos=(0,-1/sqrt(2),1/sqrt(2)),axis=(0,1,1),radius=0.03,color=color.red,length=1)
part3 = sphere(pos=(0,0,2/sqrt(2)),axis=(0,-1,1),radius=0.03,color=color.red,length=1)
spine = curve()
spine.radius = 0.02
# labels
label(pos=(0,0,-2),text="SPINE OF BUGRA",box=0,opacity=0)
label(pos=(1,0,0),text="X",box=0,opacity=0)
label(pos=(0,-1,0),text="Y",box=0,opacity=0)
label(pos=(0,0,-1),text="Z",box=0,opacity=0)
# IMU object
#platform = box(length=1, height=0.05, width=1, color=color.blue)
#p_line = box(length=1,height=0.08,width=0.1,color=color.yellow)
#plat_arrow = arrow(color=color.green,axis=(1,0,0), shaftwidth=0.06, fixedwidth=1)


"""scene4 = scene
scene4.y = 900"""
f = open("Serial"+str(time())+".txt", 'w')
#inp = open("input.txt", 'r')
roll=0
pitch=0
yaw=0
sensor = 0
rt0 = 0
rt1 = 45*degree2rad
rt2 = 135*degree2rad
rt3 = 45*degree2rad
theta0 = 0
theta1 = 45*degree2rad
theta2 = 135*degree2rad
theta3 = 45*degree2rad
l = 1
scene.visible = False
scene2.visible = False
while 1:
    line = ser.readline()
    #line = inp.readline()
    if line.find("!ANG:") != -1:          # filter out incomplete (invalid) lines
        line = line.replace("!ANG:","")   # Delete "!ANG:"
        print line
        f.write(line)                     # Write to the output log file
        words = string.split(line,",")    # Fields split
        if len(words) > 2:
            try:
                roll = float(words[0])*grad2rad
                pitch =float(words[1])*degree2rad
                
                yaw = float(words[2])*grad2rad
                sensor = float(words[3])
            except:
                print "Invalid line"
            #time.sleep(time.localtime(time.time())[5])
            #pitch += 90*degree2rad 
            #animate_object(scene)
            #animate_object(scene3)
            if sensor == 1:
                rt0 = pitch 
                theta1 = rt1 + rt0
                theta2 = rt2 + theta1
                theta3 = rt3 + theta2
                print theta1            
            elif sensor == 2:
                rt1 = pitch #- 90*degree2rad
                theta1 = rt1 + rt0
                theta2 = rt2 + theta1
                theta3 = rt3 + theta2 

            elif sensor == 3:
                rt2 = pitch #- 90*degree2rad
                theta2 = rt2 + theta1
                theta3 = rt3 + theta2 

            elif sensor == 4:
                rt3 = pitch #- 90*degree2rad
                theta3 = rt3 + theta2

            move_spine(scene3)
            

ser.close
f.close
