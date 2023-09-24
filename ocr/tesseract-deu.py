import cv2
import numpy as np
from matplotlib import pyplot as plt

# read the image
img = cv2.imread('ocr/img/tesseract-sample.png', 0)
# cv2.imshow('Original image', img)
# wait 3 seconds
# key = cv2.waitKey(3000)

# simple thresholding
ret,thresh1 = cv2.threshold(img,210,255,cv2.THRESH_BINARY)
# cv2.imshow('Threshold', thresh1)
# wait 3 seconds
# key = cv2.waitKey(3000)

# tesseract
print('--- Tesseract')
import pytesseract
from pytesseract import Output

# img = cv2.imread('receipt.jpg')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('Tesseract', img)
key = cv2.waitKey(1000)

extracted_text = pytesseract.image_to_string(img, lang = 'deu')
print('Extracted text', extracted_text)
input('Press Enter to continue...')
