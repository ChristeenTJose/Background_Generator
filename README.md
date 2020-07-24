# Matrix-Animation-Using-Python
## A bit of fun with Python Programming. I tried applying linear interpolation for smooth image transition between n different randomly generated matrix like images

Modules Required:
* Opencv
* Random
* NumPy

### Source Code:

```
import cv2
import numpy as np
import random

n=int(input('How many Transition States do you want: '))

FourCC=cv2.VideoWriter_fourcc('m','p','4','v')
video=cv2.VideoWriter('Matrix.mp4',FourCC,30,(1920,1080))

def Transition_state():
	image=np.full(shape=(1080,1920,3),fill_value=(0,50,0),dtype=np.uint8)
	i=1
	while i<=500:
		cv2.putText(image,random.choice(['0','1']),(random.randint(0,1920),random.randint(0,1080)),cv2.FONT_HERSHEY_COMPLEX,random.randint(1,3),(0,random.randint(50,255),0),random.randint(2,5))
		i+=1
	return image

TS1=Transition_state()

T=1
while T<=n:
	TS2=Transition_state()
	for i in range(50):
		weight=0.02*i
		Frame=cv2.addWeighted(TS1,1-weight,TS2,weight,0)
		video.write(Frame)
	for i in range(3):
		video.write(Frame)
	print('Finished Processing Transition State: ',T,'/',n)
	T+=1
	TS1=TS2
video.release()
```
