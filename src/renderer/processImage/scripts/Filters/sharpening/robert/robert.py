import cv2
import sys
import numpy as np
import scipy.ndimage as ndimage


imgPath = sys.argv[1]

roberts_cross_v = np.array([[1, 0], [0, -1]])
roberts_cross_h = np.array([[0, 1], [-1, 0]])
img = cv2.imread(imgPath, 0).astype('float64')
img /= 255.0
vertical = ndimage.convolve(img, roberts_cross_v)
horizontal = ndimage.convolve(img, roberts_cross_h)
edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
edged_img *= 255


cv2.imwrite('./src/renderer/processImage/FilteredImages/robert_' +sys.argv[2]+'.png', edged_img)
print('./src/renderer/processImage/FilteredImages/robert_' +sys.argv[2]+'.png')
sys.stdout.flush()