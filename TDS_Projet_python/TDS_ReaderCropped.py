import re
import cv2
import pytesseract
from pytesseract import Output
from PIL import Image 
import PIL.ImageOps
import sys


# Pour compteurIgor.png et compteurRobin.jpg --> x < 100
# Pour compteurL.png --> x < 200
# Pour compteurF.png --> x < 120

#Recuperation d'une image en argumant 
img = cv2.imread(sys.argv[1])
cv2.imwrite("readImage.png", img)
column = Image.open("readImage.png")

#Mettre l'image en NB (2 dimmensions)
gray = column.convert('L')
gray.save('etape1.jpg')

#Enlever les nuances de gris
blackwhite = gray.point(lambda x: (0) if x < 200 else 255, '1')
blackwhite.save("etape2.jpg")

#Inverser les couleurs de l'image 
image = Image.open('etape2.jpg') 
inverted_image = PIL.ImageOps.invert(image) 
inverted_image.save('etape3.jpg')
img = cv2.imread('etape3.jpg')

output = pytesseract.image_to_string(img)
newOutput = ''

#Prendre en compte uniquement des chiffres 
compteur = 0
for x in output:
    if(x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9'):
        compteur += 1
        if (compteur < 8):
            newOutput += x
#arreter a 7 chiffres max sur le compteur
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
