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

threshold, img_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

#aply closing filter
kernel = np.ones((5,5), np.uint8)

img_close = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('./src/renderer/processImage/FilteredImages/closing_'+sys.argv[2]+'.png', img_close) 

object = [
{"url":"./src/renderer/processImage/FilteredImages/closing_"+sys.argv[2]+".png","name":"Fechamento"},
]
print(json.dumps(object))
print('Cars')
sys.stdout.flush()
