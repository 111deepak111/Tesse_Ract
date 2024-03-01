import cv2
color=[255,255,255]
t,b,l,r=[150]*4
img=cv2.imread("temp/no_borders.jpg")
image_with_border=cv2.copyMakeBorder(img,t,b,l,r,cv2.BORDER_CONSTANT,value=color)
cv2.imwrite("temp/image_with_bporder.jpg",image_with_border)