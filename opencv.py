import cv2
img=cv2.imread('assest/download.jpg',-1)
#img=cv2.resize(img,(100,100))
#img=cv2.resize(img,(0,0),fx=2,fy=2)
#img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new_img.jpg',img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
