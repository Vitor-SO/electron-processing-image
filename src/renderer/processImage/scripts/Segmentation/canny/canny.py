import sys
import json
import cv2
import numpy as np

imgPath = sys.argv[1]
img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

img = cv2.Canny(img, 100, 200)

cv2.imwrite('./src/renderer/processImage/FilteredImages/canny_'+sys.argv[2]+'.png', img)


object = [{"url":'./src/renderer/processImage/FilteredImages/canny_'+sys.argv[2]+'.png',"name":"Canny"}]
print(json.dumps(object))
print('Canny')
sys.stdout.flush()
