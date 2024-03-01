import cv2

address="data/page_01.jpg"

img=cv2.imread(address)

def grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

gray_image=grayscale(img)
cv2.imwrite("temp/gray.jpg",gray_image)

thresh,im_bw=cv2.threshold(gray_image,200,235,cv2.THRESH_BINARY)
cv2.imwrite("temp/bw_img.jpg",im_bw)
