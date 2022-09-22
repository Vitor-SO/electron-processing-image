import cv2 
import numpy as np 
import sys   
from PIL import Image      
      
size = 5
img = cv2.imread(sys.argv[1])
blur = cv2.blur(img, (size, size))
cv2.imwrite('./src/renderer/processImage/FilteredImages/media_'+sys.argv[2]+'.png', blur) 