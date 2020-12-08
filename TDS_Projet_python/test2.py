import re
import cv2
import pytesseract
from pytesseract import Output
from PIL import Image 
import PIL.ImageOps
import sys

img = cv2.imread(sys.argv[1])
d = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(d.keys())

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



croppedImage = img[y:y+h,x:x+w]
 

# Pour le CompteurDeBase --> x < 100
# Pour le compteurRobin --> x < 200
# Et rogner les images
cv2.imwrite("croppedImage.jpg", croppedImage)
column = Image.open("croppedImage.jpg")

gray = column.convert('L')
gray.save('test1.jpg')
blackwhite = gray.point(lambda x: (0) if x < 180 else 255, '1')

blackwhite.save("compteurRobin1.jpg")

image = Image.open('compteurRobin1.jpg') 
inverted_image = PIL.ImageOps.invert(image) 
inverted_image.save('compteurRobin2.jpg')

img = cv2.imread('compteurRobin2.jpg')

custom_config = r'-c tessedit_char_whitelist=0123456789 --psm 6'

output = pytesseract.image_to_string(img, config=custom_config)
newOutput = ''

compteur = 0
# print(output)
for x in output:
    if(x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9'):
        newOutput += x
        compteur += 1

finalOutput = ''
newCompteur = 0
for x in newOutput:
    newCompteur += 1
    if(newCompteur < compteur):
        finalOutput += x


print(finalOutput + ',' + newOutput[compteur - 1]) 
fichier = open("data.txt", "a")
fichier.write("\n" + finalOutput +','+newOutput[compteur - 1])
fichier.close()
