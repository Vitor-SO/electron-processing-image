import json
import cv2
import sys
import numpy as np

img = cv2.imread(sys.argv[1])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
result = np.vstack([img, lap])
cv2.imwrite('./src/renderer/processImage/FilteredImages/laplacian_'+sys.argv[2]+'.png', result)


object = [{"url":'./src/renderer/processImage/FilteredImages/laplacian_'+sys.argv[2]+'.png',"name":"laplaciana"}]
print(json.dumps(object))
print('Laplaciana')
sys.stdout.flush()