import matplotlib.pyplot as plt
import cv2
import numpy as np
import json
import sys

#verifing if img is gray 

def isGray(imgPath):
#read img
  img = cv2.imread(imgPath)
  if len(img.shape) == 3 :  return cv2.imread(imgPath,0)
  if len(img.shape) < 3 : return img

image = isGray(sys.argv[1])

#cv2 threshold and transform in gray
threshold, img_thresh = cv2.threshold(image, 127,255,cv2.THRESH_BINARY_INV)

#aply erode filter
kernel = np.ones((1,1),np.uint8)
kernel2 = np.ones((3,3),np.uint8)
kernel3 = np.ones((5,5),np.uint8)

img_erode = cv2.erode(image,kernel,iterations=1)
img_dilate = cv2.dilate(img_erode,kernel,iterations=1)
img_dilate2 = cv2.dilate(img_erode,kernel2,iterations=1)
img_dilate3 = cv2.dilate(img_erode,kernel3,iterations=1)

cv2.imwrite('./src/renderer/processImage/FilteredImages/dilate_'+sys.argv[2]+'.png', img_dilate) 
cv2.imwrite('./src/renderer/processImage/FilteredImages/dilate2_'+sys.argv[2]+'.png', img_dilate2) 
cv2.imwrite('./src/renderer/processImage/FilteredImages/dilate3_'+sys.argv[2]+'.png', img_dilate3) 
object = [
{"url":"./src/renderer/processImage/FilteredImages/dilate_"+sys.argv[2]+".png","name":"dilate"},
{"url":"./src/renderer/processImage/FilteredImages/dilate2_"+sys.argv[2]+".png","name":"dilate2"},
{"url":"./src/renderer/processImage/FilteredImages/dilate3_"+sys.argv[2]+".png","name":"dilate3"},
]
print(json.dumps(object))
print('Cars')
sys.stdout.flush()