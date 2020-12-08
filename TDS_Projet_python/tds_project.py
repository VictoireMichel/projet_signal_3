import pytesseract
import cv2
from PIL import Image 
import PIL.ImageOps
 

# Pour le CompteurDeBase --> x < 100
# Pour le compteurRobin --> x < 200
# Et rogner les images
column = Image.open('compteurRobin.jpg')

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

