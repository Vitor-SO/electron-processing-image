import cv2
import numpy as np


import sys
import json

imgPath = sys.argv[1]

# Load in image, convert to gray scale, and Otsu's threshold
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)

    # noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown == 255] = 0
# reduce /conver channels to 3
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

markers = cv2.watershed(img, markers)

img[markers == -1] = [255, 0, 0]

cv2.imwrite('./src/renderer/processImage/FilteredImages/watersheds_'+sys.argv[2]+'.png', img)
object = [{"url":'./src/renderer/processImage/FilteredImages/watersheds_'+sys.argv[2]+'.png',"name":"watersheds"}]

print(json.dumps(object))
print('Watersheds')
sys.stdout.flush()
