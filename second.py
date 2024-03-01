import cv2
from matplotlib import pyplot as plt

address="data/page_01.jpg"

img=cv2.imread(address)

# cv2.imshow("OG",img)
# cv2.waitKey()

inv_img=cv2.bitwise_not(img)

cv2.imwrite("temp/inv_img.jpg",inv_img)
img=cv2.imread("temp/inv_img.jpg")
cv2.imshow("INV",img)
cv2.waitKey()