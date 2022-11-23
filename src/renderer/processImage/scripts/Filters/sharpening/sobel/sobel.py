import json
import cv2
import sys

imgPath = sys.argv[1]



img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray, (3, 3), 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
cv2.imwrite("./src/renderer/processImage/FilteredImages/sobelx_" +sys.argv[2]+'.png', sobelx)
cv2.imwrite("./src/renderer/processImage/FilteredImages/sobely_" +sys.argv[2]+'.png', sobely)


object = [
{"url":"./src/renderer/processImage/FilteredImages/sobelx_" +sys.argv[2]+'.png',"name":"sobel X"},
{"url":"./src/renderer/processImage/FilteredImages/sobely_" +sys.argv[2]+'.png',"name":"sobel Y"}
]
print(json.dumps(object))
print('Sobel')
sys.stdout.flush()