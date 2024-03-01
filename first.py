from PIL import Image

address="data/page_01.jpg"

im=Image.open(address)
im.show() #opening image
im.save(address) #save image