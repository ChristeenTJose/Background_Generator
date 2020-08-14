import cv2
from background_generator import Background_Generator
Transition_speed = 50 #Default: 50
n=int(input('How many Transition States do you want: '))
FourCC=cv2.VideoWriter_fourcc('m','p','4','v')
video=cv2.VideoWriter('Matrix.mp4',FourCC,30,(1920,1080))
TS1=Background_Generator()
if n==0:
	cv2.imwrite('Wallpaper.png',TS1)
T=1
while T<=n:
	TS2=Background_Generator()
	for i in range(Transition_speed):
		weight=i/Transition_speed
		Frame=cv2.addWeighted(TS1,1-weight,TS2,weight,0)
		video.write(Frame)
	for i in range(3):
		video.write(Frame)
	print('Finished Processing Transition State: ',T,'/',n)
	T+=1
	TS1=TS2
video.release()

