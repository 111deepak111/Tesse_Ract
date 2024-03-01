import pytesseract
from PIL import Image

addr="data/page_01.jpg"
addr2="temp/no_noise.jpg"

img=Image.open(addr)
ocr_res=pytesseract.image_to_string(img)
print(ocr_res)
img=Image.open(addr2)
ocr_res=pytesseract.image_to_string(img)
print(ocr_res)

