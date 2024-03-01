import cv2
import numpy as np

address="temp/no_noise.jpg"
image=cv2.imread(address)
def thin_font(image):
    image=cv2.bitwise_not(image)
    kernel=np.ones((2,2),np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    image=cv2.bitwise_not(image)
    return image

thin = thin_font(image)
cv2.imwrite("temp/thin_font.jpg",thin)
image=cv2.imread(address)
def thick_font(image):
    image=cv2.bitwise_not(image)
    kernel=np.ones((2,2),np.uint8)
    image=cv2.dilate(image,kernel,iterations=1)
    image=cv2.bitwise_not(image)
    return image
thick =thick_font(image)

cv2.imwrite("temp/thick_font.jpg",thick)