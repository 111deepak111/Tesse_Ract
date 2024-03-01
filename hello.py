import pytesseract
import cv2
from PIL import Image

addr="data/index_02.jpg"
img=cv2.imread(addr)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imwrite("temp/index_grey.jpg",gray)

blur=cv2.GaussianBlur(gray,(7,7),0)
# cv2.imwrite("temp/index_blur.jpg",blur)

thres=cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
# cv2.imwrite("temp/thresh_index.jpg",thres)

kernels=cv2.getStructuringElement(cv2.MORPH_RECT,(3,13))

dilate=cv2.dilate(thres,kernels,iterations=1)
# cv2.imwrite("temp/dilate_index.jpg",dilate)

cnts=cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cnts=cnts[0] if len(cnts)==2 else cnts[2]
cnts=sorted(cnts,key=lambda x:cv2.boundingRect(x)[0])
result=[]
for c in cnts:
    x,y,w,h=cv2.boundingRect(c)
    if (h>200 and w>20):
        roi=img[y:y+h,x:x+w]
        cv2.imwrite("temp/index_roi.jpg",roi)
        ocr_res=pytesseract.image_to_string(roi)
        ocr_res=ocr_res.split("\n")
        for i in ocr_res:
            result.append(i)
        cv2.rectangle(img,(x,y),(x+w,y+h),(36,255,12),2)

cv2.imwrite("temp/bounding_index.jpg",img)

entities=[]
for i in result:
    if len(i)>0:
        sentence=i.split(" ")[0]
        if len(sentence)>0 and sentence[0].isupper() and "-" not in sentence:
            sentence=sentence.replace(",","").replace(".","").replace(";","")
            if(len(sentence)>2):
                entities.append(sentence)    

entities=list(set(entities))
entities.sort()
print(entities)