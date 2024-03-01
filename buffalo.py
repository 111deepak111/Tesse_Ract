import cv2
import pytesseract

image=cv2.imread("data/sample_mgh.jpg")
base_image=image.copy()

gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
blur=cv2.GaussianBlur(gray,(7,7),0)
thres=cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,50))
dilate=cv2.dilate(thres,kernel,iterations=1)

cv2.imwrite("temp/dilated.png",dilate)