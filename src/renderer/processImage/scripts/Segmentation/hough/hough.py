import numpy as np
from matplotlib import pyplot as plt
import sys
import json
import cv2


imgPath = sys.argv[1]

# Read image
img = cv2.imread(imgPath) # road.png is the filename
# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector

edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
# edges = cv2.Canny(gray, 50, 200)
# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

# Draw lines on the image
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
# Show result

cv2.imwrite('./src/renderer/processImage/FilteredImages/hough_'+sys.argv[2]+'.png', img)

object = [{"url":'./src/renderer/processImage/FilteredImages/hough_'+sys.argv[2]+'.png',"name":"Hough"}]
print(json.dumps(object))
print('Hough')
sys.stdout.flush()