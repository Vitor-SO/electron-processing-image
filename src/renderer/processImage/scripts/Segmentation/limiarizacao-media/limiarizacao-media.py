import numpy as np
import cv2
import sys
import json


imgPath = sys.argv[1]
img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur the image to denoise

img_blur = cv2.medianBlur(gray, 5)

# apply adaptive thresholding

th = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imwrite('./src/renderer/processImage/FilteredImages/limiarizacao-media_'+sys.argv[2]+'.png', th)

object = [{"url":'./src/renderer/processImage/FilteredImages/limiarizacao-media_'+sys.argv[2]+'.png',"name":"Limiarização Média"}]
print(json.dumps(object))
print('Limiarização Média')
sys.stdout.flush()
