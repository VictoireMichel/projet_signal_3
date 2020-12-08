import re
import cv2
import pytesseract
from pytesseract import Output
from PIL import Image 
import PIL.ImageOps

img = cv2.imread('compteurIgor.png')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



croppedImage = img[y:y+h,x:x+w]
#croppedImage.save('croppedTest.jpg')
cv2.imshow('img', croppedImage)
cv2.waitKey(0)



print(x)
print(w)
print(y)
print(h)

