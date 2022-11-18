import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import json
import sys
import cv2
imgPath = sys.argv[1]

img = cv2.imread(imgPath)
img = cv.medianBlur(img,5)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

result = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

cv2.imwrite('./src/renderer/processImage/FilteredImages/gradient_'+sys.argv[2]+'.png', result)

object = [{"url":'./src/renderer/processImage/FilteredImages/gradient_'+sys.argv[2]+'.png',"name":"gradient"}]
print(json.dumps(object))
print('Gradient')
sys.stdout.flush()

