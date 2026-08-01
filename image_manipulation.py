import cv2
import random
img=cv2.imread('assest/download.jpg',-1)
#how actually image represented
print(img)
print(type(img))
print(img.shape)#row =height,column=width,third=channel
#in open cv color pixel are usually represented blue,green,red
#[[0,0,0]] 0=blue,0=green,0=red
#[[255,0,0]] 255=all blue,green=zero,red=zero
#we can also modify image manually without use of open cv
print(img[128][40:100])#128=row,40:100=40 sy 100 column ky pixel show krwa do
print(img[128,1])
cv2.imshow('image',img)
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
tag=img[100:120,200:230]
img[150:170,90:120]=tag        
cv2.imshow('image',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()       