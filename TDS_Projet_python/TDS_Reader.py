import re
import cv2
import pytesseract
from pytesseract import Output
from PIL import Image 
import PIL.ImageOps
import sys

#Pour compteurIgor.png et compteurRobin.jpg --> x < 100

#Recuperation d'une image en argumant 
img = cv2.imread(sys.argv[1])
d = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(d.keys())

#Creation de la box pour le detourrage 
n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        #Dessiner le rectangle vert 
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#Detourrage en fonction du rectangle vert 
croppedImage = img[y:y+h,x:x+w]

#Recuperation d'une image cropped 
cv2.imwrite("croppedImage.jpg", croppedImage)
column = Image.open("croppedImage.jpg")

#Mettre l'image en NB (2 dimmensions)
gray = column.convert('L')
gray.save('etape1.jpg')

#Enlever les nuances de gris
blackwhite = gray.point(lambda x: (0) if x < 100 else 255, '1')
blackwhite.save("etape2.jpg")

#Inverser les couleurs de l'image 
image = Image.open('etape2.jpg') 
inverted_image = PIL.ImageOps.invert(image) 
inverted_image.save('etape3.jpg')
img = cv2.imread('etape3.jpg')

custom_config = r'-c tessedit_char_whitelist=0123456789 --psm 6'

output = pytesseract.image_to_string(img, config=custom_config)
newOutput = ''


#Prendre en compte uniquement des chiffres 
compteur = 0
for x in output:
    if(x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9'):
        compteur += 1
        if (compteur < 8):
            newOutput += x
#Arreter a 7 chiffres max sur le compteur
if (compteur > 7):
    compteur = 7

finalOutput = ''
newCompteur = 0
for x in newOutput:
    newCompteur += 1
    if(newCompteur < compteur):
        finalOutput += x

#Ajouter une virgule 
print(finalOutput + ',' + newOutput[compteur - 1]) 

#Afficher le resultat dans un fichier data.txt
fichier = open("data.txt", "a")
fichier.write("\n" + finalOutput +','+newOutput[compteur - 1])
fichier.close()
