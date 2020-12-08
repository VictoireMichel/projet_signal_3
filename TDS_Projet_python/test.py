#from PIL import Image
import pytesseract
import cv2


from PIL import Image 
import PIL.ImageOps


#image = Image.open('compteurIgor3.jpg') 
#inverted_image = PIL.ImageOps.invert(image) 
#inverted_image.save('compteurIgor4.jpg')

#column = Image.open('compteurIgor.png')
#gray = column.convert('L')
#blackwhite = gray.point(lambda x: 0 if x < 100 else 255, '1')
#blackwhite.save("compteurIgor3.jpg")

#img = Image.open('compteurIgorBis.jpg')
#print(pytesseract.image_to_string(img))

img = cv2.imread('compteurRobin.jpg')

#custom_config = r'-c tessedit_char_blacklist="(+" --psm 6'
custom_config = r'-c tessedit_char_whitelist=0123456789 --psm 6'

#custom_config = r'--oem 3 --psm 6 outputbase digits'
print(pytesseract.image_to_string(img, config=custom_config))