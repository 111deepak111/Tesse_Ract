import cv2
import numpy as np

def noise_removal(image):
    kernel=np.ones((1,1),dtype=np.uint8)
    image=cv2.dilate(image,kernel,iterations=1)
    kernel=np.ones((1,1),dtype=np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    image=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
    image=cv2.medianBlur(image,3)
    return (image)

addr="temp/bw_img.jpg"
bw=cv2.imread(addr)
image=noise_removal(bw)
cv2.imwrite("temp/no_noise.jpg",image)