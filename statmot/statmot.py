#!/usr/bin/python

# use a Tkinter label as a panel/frame with a background image
# note that Tkinter only reads gif and ppm images
# use the Python Image Library (PIL) for other image formats
# free from [url]http://www.pythonware.com/products/pil/index.htm[/url]
# give Tkinter a namespace to avoid conflicts with PIL
# (they both have a class named Image)

import Tkinter as tk
from PIL import Image, ImageTk
from ttk import Frame, Button, Style
import time
from copy import deepcopy
import serial
import string
import math
import os
from time import time
from time import sleep



grad2rad = 3.141592/180.0
degree2rad = 0.0174533
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

#inp = open("input.txt", 'r')

# Check your COM port and baud rate
ser = serial.Serial(port='COM3',baudrate=115200, timeout=1)

class Example():
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('Current Position')

		# pick an image file you have .bmp  .jpg  .gif.  .png
		# load the file and covert it to a Tkinter image object
		#imageFile = "babyAce.jpg"
		#self.image1 = ImageTk.PhotoImage(Image.open(imageFile))
		self.image111 = ImageTk.PhotoImage(Image.open("111-min.png"))
		self.image112 = ImageTk.PhotoImage(Image.open("112-min.png"))
		self.image113 = ImageTk.PhotoImage(Image.open("113-min.png"))

		self.image121 = ImageTk.PhotoImage(Image.open("121-min.png"))
		self.image122 = ImageTk.PhotoImage(Image.open("122-min.png"))
		self.image123 = ImageTk.PhotoImage(Image.open("123-min.png"))

		self.image131 = ImageTk.PhotoImage(Image.open("131-min.png"))
		self.image132 = ImageTk.PhotoImage(Image.open("132-min.png"))
		self.image133 = ImageTk.PhotoImage(Image.open("133-min.png"))


		self.image211 = ImageTk.PhotoImage(Image.open("211-min.png"))
		self.image212 = ImageTk.PhotoImage(Image.open("212-min.png"))
		self.image213 = ImageTk.PhotoImage(Image.open("213-min.png"))

		self.image221 = ImageTk.PhotoImage(Image.open("221-min.png"))
		self.image222 = ImageTk.PhotoImage(Image.open("222-min.png"))
		self.image223 = ImageTk.PhotoImage(Image.open("223-min.png"))

		self.image231 = ImageTk.PhotoImage(Image.open("231-min.png"))
		self.image232 = ImageTk.PhotoImage(Image.open("232-min.png"))
		self.image233 = ImageTk.PhotoImage(Image.open("233-min.png"))


		self.image311 = ImageTk.PhotoImage(Image.open("311-min.png"))
		self.image312 = ImageTk.PhotoImage(Image.open("312-min.png"))
		self.image313 = ImageTk.PhotoImage(Image.open("313-min.png"))

		self.image321 = ImageTk.PhotoImage(Image.open("321-min.png"))
		self.image322 = ImageTk.PhotoImage(Image.open("322-min.png"))
		self.image323 = ImageTk.PhotoImage(Image.open("323-min.png"))

		self.image331 = ImageTk.PhotoImage(Image.open("331-min.png"))
		self.image332 = ImageTk.PhotoImage(Image.open("332-min.png"))
		self.image333 = ImageTk.PhotoImage(Image.open("333-min.png"))

		# get the image size
		w = self.image111.width()
		h = self.image111.height()

		# position coordinates of root 'upper left corner'
		x = 0
		y = 0

		# make the root window the size of the image
		self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))

		# root has no image argument, so use a label as a panel
		self.panel1 = tk.Label(self.root, image=self.image111)
		self.display = self.image111
		self.panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
		print "Display image1"
		self.root.after(10, self.update_image)
		self.root.mainloop()

	def update_image(self):
		e1 = 10
		e2 = 20
		
		global	grad2rad 
		global	degree2rad
		global	roll
		global	pitch
		global	yaw
		global	sensor 
		global	rt0 
		global	rt1 
		global	rt2 
		global	rt3 
		global	theta0 
		global	theta1 
		global	theta2 
		global	theta3 
		line = ser.readline()
		#print line
		#line = inp.readline()
		#print line
		if line.find("!ANG:") != -1:          # filter out incomplete (invalid) lines
			line = line.replace("<!ANG:","")   # Delete "!ANG:"
			#print line
			#f.write(line)                     # Write to the output log file
			words = string.split(line,",")    # Fields split
			if len(words) > 2:
				try:
					roll = float(words[0])
					pitch =float(words[1])
					
					yaw = float(words[2])
					sensor = float(words[3][0])
					print line
				except:
					print "Invalid line"
				#time.sleep(time.localtime(time.time())[5])
				#pitch += 90*degree2rad 
				#animate_object(scene)
				#animate_object(scene3)
				if sensor == 1:
					rt0 = pitch 
					theta0 = pitch -rt0
	         
				elif sensor == 2:
					rt1 = pitch #- 90*degree2rapn
					theta1 = pitch -rt0
					theta1 = abs(theta1)
					theta2 = abs(theta2)
					theta3 = abs(theta3)	

					print theta1  
					print theta2
					print theta3 

				elif sensor == 3:
					rt2 = pitch #- 90*degree2rad
					theta2 = pitch-rt0
					theta1 = abs(theta1)
					theta2 = abs(theta2)
					theta3 = abs(theta3)	

				elif sensor == 4:
					rt3 = pitch #- 90*degree2rad
					theta3 = pitch-rt0
					theta1 = abs(theta1)
					theta2 = abs(theta2)
					theta3 = abs(theta3)	

				if theta1 < e1 :
					if theta2 < e1 :
						if theta3 < e1:
							self.panel1.configure(image=self.image111)
							self.display = self.image111
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image112)
							self.display = self.image112
						elif theta3 > e2:							
							self.panel1.configure(image=self.image113)
							self.display = self.image113
					elif theta2 < e2 and theta2 >e1:
						if theta3 <  e1:
							self.panel1.configure(image=self.image121)
							self.display = self.image121
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image122)
							self.display = self.image122
						elif theta3 > e2:							
							self.panel1.configure(image=self.image123)
							self.display = self.image123
					elif theta2 > e2:
						if theta3 <  e1:
							self.panel1.configure(image=self.image131)
							self.display = self.image131
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image132)
							self.display = self.image132
						elif theta3 > e2:							
							self.panel1.configure(image=self.image133)
							self.display = self.image133					
				elif theta1 > e1 and theta1 < e2:
					if theta2 < e2 and theta2 > e1:
						if theta3 <  e1:
							self.panel1.configure(image=self.image211)
							self.display = self.image211
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image212)
							self.display = self.image212
						elif theta3 > e2:							
							self.panel1.configure(image=self.image213)
							self.display = self.image213
					elif theta2 < e2 and theta2 >e1:
						if theta3 <  e1:
							self.panel1.configure(image=self.image221)
							self.display = self.image221
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image222)
							self.display = self.image222
						elif theta3 > e2:							
							self.panel1.configure(image=self.image223)
							self.display = self.image223
					elif theta2 > e2:
						if theta3 <  e1:
							self.panel1.configure(image=self.image231)
							self.display = self.image231
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image232)
							self.display = self.image232
						elif theta3 > e2:							
							self.panel1.configure(image=self.image233)
							self.display = self.image233
				elif theta1 > e2:
					if theta2 <  e1:
						if theta3 <  e1:
							self.panel1.configure(image=self.image311)
							self.display = self.image311
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image312)
							self.display = self.image312
						elif theta3 > e2:							
							self.panel1.configure(image=self.image313)
							self.display = self.image313
					elif theta2 < e2 and theta2 >e1:
						if theta3 < e1:
							self.panel1.configure(image=self.image321)
							self.display = self.image321
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image322)
							self.display = self.image322
						elif theta3 > e2:							
							self.panel1.configure(image=self.image323)
							self.display = self.image323
					elif theta2 > e2:
						if theta3 < e1:
							self.panel1.configure(image=self.image331)
							self.display = self.image331
						elif theta3 < e2 and theta3 > e1:
							self.panel1.configure(image=self.image332)
							self.display = self.image332
						elif theta3 > e2:							
							self.panel1.configure(image=self.image333)
							self.display = self.image333

		self.root.after(20, self.update_image)       # Set to call again in 30 seconds

def main():
	#f = open("Serial"+str(time())+".txt", 'w')



	
	app = Example()



	#ser.close
	#f.close


if __name__ == '__main__':
	main()

