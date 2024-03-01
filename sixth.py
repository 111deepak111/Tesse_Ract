import cv2
import numpy as np

img = cv2.imread("ocr_python_textbook/temp/no_noise.jpg")

def remove_borders(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    contours, heiarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntSorted=sorted(contours,key=lambda x:cv2.contourArea(x))
    cnt = cntSorted[-1]
    x,y,width,height=cv2.boundingRect(cnt)
    crop=img[y:y+height,x:x+width]
    thresh,crop=cv2.threshold(crop,200,235,cv2.THRESH_BINARY)
    return (crop)

no_borders=remove_borders(img)
cv2.imwrite("temp/no_borders.jpg",no_borders)