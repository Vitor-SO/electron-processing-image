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
kernel = np.array([[0,1,1,0], [1,1,1,1],[0,1,1,0]], np.uint8)

img_open = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imwrite('./src/renderer/processImage/FilteredImages/opening_'+sys.argv[2]+'.png', img_open) 

object = [
{"url":"./src/renderer/processImage/FilteredImages/opening_"+sys.argv[2]+".png","name":"Abertura"},
]
print(json.dumps(object))
print('Cars')
sys.stdout.flush()