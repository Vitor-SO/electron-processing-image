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

#aply erode filter
kernel = np.ones((4,4),np.uint8)

img_dilate = cv2.dilate(image,kernel,iterations=2)
img_dilate2 = cv2.dilate(image,kernel,iterations=4)
img_dilate3 = cv2.dilate(image,kernel,iterations=6)
img_dilate4 = cv2.dilate(image,kernel,iterations=8)
img_dilate5 = cv2.dilate(image,kernel,iterations=10)

cv2.imwrite('./src/renderer/processImage/FilteredImages/dilate_'+sys.argv[2]+'.png', img_dilate) 
cv2.imwrite('./src/renderer/processImage/FilteredImages/dilate2_'+sys.argv[2]+'.png', img_dilate2) 
cv2.imwrite('./src/renderer/processImage/FilteredImages/dilate3_'+sys.argv[2]+'.png', img_dilate3) 
cv2.imwrite('./src/renderer/processImage/FilteredImages/dilate4_'+sys.argv[2]+'.png', img_dilate4) 
cv2.imwrite('./src/renderer/processImage/FilteredImages/dilate5_'+sys.argv[2]+'.png', img_dilate5) 
object = [
{"url":"./src/renderer/processImage/FilteredImages/dilate_"+sys.argv[2]+".png","name":"dilate"},
{"url":"./src/renderer/processImage/FilteredImages/dilate2_"+sys.argv[2]+".png","name":"dilate2"},
{"url":"./src/renderer/processImage/FilteredImages/dilate3_"+sys.argv[2]+".png","name":"dilate3"},
{"url":"./src/renderer/processImage/FilteredImages/dilate4_"+sys.argv[2]+".png","name":"dilate4"},
{"url":"./src/renderer/processImage/FilteredImages/dilate5_"+sys.argv[2]+".png","name":"dilate5"}
]
print(json.dumps(object))
print('Cars')
sys.stdout.flush()