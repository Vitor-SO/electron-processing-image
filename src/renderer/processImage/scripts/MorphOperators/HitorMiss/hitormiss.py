import matplotlib.pyplot as plt
import cv2
import numpy as np
import json
import sys


def isGray(imgPath):
#read img
  img = cv2.imread(imgPath)
  if len(img.shape) == 3 :  return cv2.imread(imgPath,0)
  if len(img.shape) < 3 : return img

image = isGray(sys.argv[1])

threshold, img_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

#aply hiit or miss filter
kernel = np.array((
        [0, 1, 0],
        [1, -1, 1],
        [0, 1, 0]), np.uint8)

# kernel2 = np.ones((5,5),np.uint8)

output_image = cv2.morphologyEx(img_thresh, cv2.MORPH_HITMISS, kernel)


cv2.imwrite('./src/renderer/processImage/FilteredImages/closing_'+sys.argv[2]+'.png', output_image) 

object = [
{"url":"./src/renderer/processImage/FilteredImages/closing_"+sys.argv[2]+".png","name":"Hit or Miss"},
]
print(json.dumps(object))
print('Cars')
sys.stdout.flush()