import numpy as np
import cv2

img=cv2.imread('assest/download.jpg')
img=cv2.resize(img,(0,0),fx=0.75,fy=0.75)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



corners=cv2.goodFeaturesToTrack(gray,100,0.01,10 )
print(corners)
corners=np.int32(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)


for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1=tuple(corners[i][0])
        corner2=tuple(corners [j][0])
        color=tuple(map(lambda x:int(x),np.random.randint(0,255,size=3)))
        cv2.line(img,corner1,corner2,color,1) 
# cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture('video')
# while True:
#     ret,frame=cap.read()
#     width=int(cap.get(3))
#     height=int(cap.get(4))
    # hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # lower_blue=np.array([90,50,50])
    # upper_blue=np.array([120,255,255])

    # mask=cv2.inRange(hsv,lower_blue,upper_blue)
    # result=cv2.bitwise_and(frame,frame,mask=mask)


    # cv2.imshow('frame',result)
    # cv2.imshow('mask',mask)
    # if cv2.waitKey(1)==ord('q'):
    #     break
cv2.imshow('frame',img)
cv2.waitKey(0) 
#cap.release()
cv2.destroyAllWindows()   