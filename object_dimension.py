import numpy as np
import cv2
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        roi_gray=gray[y:y+w,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
         cv2.rectangle(
        roi_color,
        (ex, ey),
        (ex+ew, ey+eh),
        (0, 255, 0),
        2
    )
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()


# img=cv2.imread('assest/img.jpg')
# template=cv2.imread('assest/img 1.PNG')
# h,w,_=template.shape

# methods=[cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,
#          cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

# for method in methods:
#     img2=img.copy()
#     result=cv2.matchTemplate(img2,template,method) 
#     min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
#     if method in [cv2.TM_SQDIFF_NORMED]:
#         location=min_loc
#     else:
#         location=max_loc
#     bottom_right=(location[0]+w ,location[1]+h)
#     cv2.rectangle(img2,location,bottom_right,255,5) 
#     cv2.imshow('match template',img2)  
cv2.waitKey(0) 
cv2.destroyAllWindows()    

