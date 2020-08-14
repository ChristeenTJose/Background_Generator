import cv2
from background_generator import Background_Generator
Transition_speed = 1 #Default: 50
n=int(input('How many Transition States do you want: '))
FourCC=cv2.VideoWriter_fourcc('m','p','4','v')
video=cv2.VideoWriter('Matrix.mp4',FourCC,30,(1920,1080))
PROPERTIES,TS1=Background_Generator()
if n==0:
	cv2.imwrite('Wallpaper.png',TS1)
T=1
while T<=n:
	Frame = PROPERTIES[0].copy()
	for i in range(1,len(PROPERTIES)):
		cv2.putText(Frame,PROPERTIES[i][0],(PROPERTIES[i][1][0],(PROPERTIES[i][1][1]+10*T)%1080),PROPERTIES[i][2],PROPERTIES[i][3],PROPERTIES[i][4],PROPERTIES[i][5])
	video.write(Frame)
	print('Finished Processing Transition State: ',T,'/',n)
	T+=1
video.release()

