import json
import cv2 
import sys   

size = 5
if size % 2 == 0:
            size += 1

img = cv2.imread(sys.argv[1])
median_blur = cv2.medianBlur(img, size)
cv2.imwrite('./src/renderer/processImage/FilteredImages/median_'+sys.argv[2]+'.png', median_blur)

object = [{"url":"./src/renderer/processImage/FilteredImages/median_"+sys.argv[2]+".png","name":"mediana"}]
print(json.dumps(object))
print('Mediana')
sys.stdout.flush()