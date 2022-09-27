import json
import cv2
import sys

imgPath = sys.argv[1]

img = cv2.imread(imgPath)
resultant_image = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for i in range(1, img.shape[0]-1):
    for x in range(1, img.shape[1]-1):
            blur_factor = (img[i-1, x-1] + img[i-1, x] + img[i-1, x+1] + img[i, x-1] + img[i, x] + img[i, x+1] + img[i+1, x+1] + img[i+1, x] + img[i+1, x+1])/9
            mask = 1 * img[i, x] - blur_factor
            resultant_image[i, x] = img[i, x] + mask

cv2.imwrite('./src/renderer/processImage/FilteredImages/hightboost_'+sys.argv[2]+'.png', resultant_image)

object = [{"url":'./src/renderer/processImage/FilteredImages/hightboost_'+sys.argv[2]+'.png',"name":"high boost"}]
print(json.dumps(object))
print('High Boost')
sys.stdout.flush()