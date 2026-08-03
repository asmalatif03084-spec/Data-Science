import numpy as np
import cv2
cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture('video')
while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    img=cv2.line(frame,(0,0),(width,height),(255,0,0),10  )
    img=cv2.line(img,(0,height),(width,0),(0,255,0),20)
    img=cv2.rectangle(img,(100,100),(200,200),(128,128,128),5)
    img=cv2.circle(img,(300,300),60,(0,0,255),-1)
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img,'asma is great!',(200,height-10),font,4,(0,0,255),5,cv2.LINE_AA)
    # image=np.zeros(frame.shape,np.uint8)
    # smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    # image[:height//2 , :width//2]=smaller_frame
    # image[height//2: , :width//2]=smaller_frame
    # image[:height//2 , width//2:]=smaller_frame
    # image[height//2: , width//2:]=smaller_frame

    # image[:height//2 , :width//2]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    # image[height//2: , :width//2]=smaller_frame
    # image[:height//2 , width//2:]=cv2.rotate(smaller_frame,cv2.ROTATE_180)
    # image[height//2: , width//2:]=smaller_frame

    #cv2.imshow('frame',image)
    cv2.imshow('frame',img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    