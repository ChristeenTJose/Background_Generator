import cv2
import numpy as np
import random

#Default Values
BACKGROUND_HEIGHT = 1080
BACKGROUND_WIDTH = 1920
BACKGROUND_NCHANNELS = 3
BACKGROUND_COLOR = (0,40,0)
BACKGROUND_NCHAR = 500
BACKGROUND_CHOICES = ['0','1']
BACKGROUND_FONT = cv2.FONT_HERSHEY_COMPLEX
BACKGROUND_FONTSCALE_MAX = 3
BACKGROUND_TEXTCOLOR_B_MIN = 0
BACKGROUND_TEXTCOLOR_B_MAX = 0
BACKGROUND_TEXTCOLOR_G_MIN = 50
BACKGROUND_TEXTCOLOR_G_MAX = 255
BACKGROUND_TEXTCOLOR_R_MIN = 0
BACKGROUND_TEXTCOLOR_R_MAX = 0
BACKGROUND_FONT_THICKNESS_MIN = 2
BACKGROUND_FONT_THICKNESS_MAX = 5

def Background_Generator():
	image=np.full(shape=(BACKGROUND_HEIGHT,BACKGROUND_WIDTH,BACKGROUND_NCHANNELS),fill_value=BACKGROUND_COLOR,dtype=np.uint8)
	i=1
	nchar_properties=[image.copy()]
	while i<=BACKGROUND_NCHAR:
		
		text = random.choice(BACKGROUND_CHOICES)
		x = random.randint(0,BACKGROUND_WIDTH)
		y = random.randint(0,BACKGROUND_HEIGHT)
		fontScale = random.randint(1,BACKGROUND_FONTSCALE_MAX)
		B = random.randint(BACKGROUND_TEXTCOLOR_B_MIN,BACKGROUND_TEXTCOLOR_B_MAX)
		G = random.randint(BACKGROUND_TEXTCOLOR_G_MIN,BACKGROUND_TEXTCOLOR_G_MAX)
		R = random.randint(BACKGROUND_TEXTCOLOR_R_MIN,BACKGROUND_TEXTCOLOR_R_MAX)
		textColor = (B,G,R)
		fontThickness = random.randint(BACKGROUND_FONT_THICKNESS_MIN,BACKGROUND_FONT_THICKNESS_MAX)
		
		cv2.putText(image,text,(x,y),BACKGROUND_FONT,fontScale,textColor,fontThickness)
		nchar_properties.append([text,(x,y),BACKGROUND_FONT,fontScale,textColor,fontThickness])
		
		i+=1
	return nchar_properties,image

def Transition():
	pass
	
def Help():
	pass
