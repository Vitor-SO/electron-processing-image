import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio
import skimage.color
import skimage.filters
import skimage.measure

import sys
import cv2
import json
sigma = 0.1
t = 0.5
connectivity = 2

imgPath = sys.argv[1]
image = cv2.imread(imgPath, cv2.IMREAD_COLOR)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred_image = skimage.filters.gaussian(gray_image, sigma=sigma)

binary_mask = blurred_image < t

label_image = skimage.measure.label(binary_mask, connectivity=connectivity)


cv2.imwrite('./src/renderer/processImage/FilteredImages/componentesconexos_'+sys.argv[2]+'.png', label_image)

object = [{"url":'./src/renderer/processImage/FilteredImages/componentesconexos_'+sys.argv[2]+'.png',"name":"componentes conexos"}]
print(json.dumps(object))
print('Componentes conexos')
sys.stdout.flush()


