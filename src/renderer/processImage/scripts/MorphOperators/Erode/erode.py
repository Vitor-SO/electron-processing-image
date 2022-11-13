import sys  
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import numpy as np
import json

def isGray(imgPath):
#read img
  img = cv2.imread(imgPath)
  if len(img.shape) == 3 :  return cv2.imread(imgPath,0)
  if len(img.shape) < 3 : return img


image = isGray(sys.argv[1])

#cv2 threshold and transform in gray
threshold, img_thresh = cv2.threshold(image, 127,255,cv2.THRESH_BINARY_INV)

#aply erode filter
kernel = np.ones((4,4),np.uint8)

img_erode = cv2.erode(img_thresh,kernel,iterations=1)
img_erode2 = cv2.erode(img_thresh,kernel,iterations=2)
img_erode3 = cv2.erode(img_thresh,kernel,iterations=3)
# img_erode4 = cv2.erode(img_thresh,kernel,iterations=4)
# img_erode5 = cv2.erode(img_thresh,kernel,iterations=5)

cv2.imwrite('./src/renderer/processImage/FilteredImages/erode_'+sys.argv[2]+'.png', img_erode) 
cv2.imwrite('./src/renderer/processImage/FilteredImages/erode2_'+sys.argv[2]+'.png', img_erode2) 
cv2.imwrite('./src/renderer/processImage/FilteredImages/erode3_'+sys.argv[2]+'.png', img_erode3) 
object = [
{"url":"./src/renderer/processImage/FilteredImages/erode_"+sys.argv[2]+".png","name":"erode"},
{"url":"./src/renderer/processImage/FilteredImages/erode2_"+sys.argv[2]+".png","name":"erode2"},
{"url":"./src/renderer/processImage/FilteredImages/erode3_"+sys.argv[2]+".png","name":"erode3"}
]
print(json.dumps(object))
print('Cars')
sys.stdout.flush()
