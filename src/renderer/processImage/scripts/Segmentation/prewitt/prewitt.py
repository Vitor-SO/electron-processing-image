import numpy as np
import cv2
import sys
import json

imgPath = sys.argv[1]
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

# prewitt
kernelx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernely = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)


cv2.imwrite('./src/renderer/processImage/FilteredImages/prewittx_'+sys.argv[2]+'.png', img_prewittx)
cv2.imwrite('./src/renderer/processImage/FilteredImages/prewitty_'+sys.argv[2]+'.png', img_prewitty)

object = [{"url":'./src/renderer/processImage/FilteredImages/prewittx_'+sys.argv[2]+'.png',"name":"Prewitt - X"},
        {"url":'./src/renderer/processImage/FilteredImages/prewitty_'+sys.argv[2]+'.png',"name":"Prewitt - Y"}]
print(json.dumps(object))
print('Prewitt')
sys.stdout.flush()
