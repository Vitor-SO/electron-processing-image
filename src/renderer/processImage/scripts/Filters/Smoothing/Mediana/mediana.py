import cv2 
import sys   

size = 5
if size % 2 == 0:
            size += 1

img = cv2.imread(sys.argv[1])
median_blur = cv2.medianBlur(img, size)
cv2.imwrite('./src/renderer/processImage/FilteredImages/median_'+sys.argv[2]+'.png', median_blur)
print('./src/renderer/processImage/FilteredImages/median_'+sys.argv[2]+'.png')
sys.stdout.flush()