import numpy as np
import glob
import matplotlib.pyplot as plt
import imageio.v3 as iio
import skimage.color
import skimage.filters
import skimage.morphology
import sys
import json
import cv2



imgPath = sys.argv[1]

img = cv2.imread(imgPath)

# # Convert the image to gray-scale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # blur the image to denoise
# blurred_image = skimage.filters.gaussian(gray, sigma=1.0)

# # show the histogram of the blurred image
# histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))

# # perform automatic thresholding
# t = skimage.filters.threshold_otsu(blurred_image)

# # create a binary mask with the threshold found by Otsu's method
# binary_mask = blurred_image > t

# # apply the binary mask to select the foreground
# selection = img.copy()
# selection[~binary_mask] = 0

# converte the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur the image to denoise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# show the histogram of the blurred image
ret1, th1 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imwrite('./src/renderer/processImage/FilteredImages/limiarizacao_'+sys.argv[2]+'.png', th1)


object = [{"url":'./src/renderer/processImage/FilteredImages/limiarizacao_'+sys.argv[2]+'.png',"name":"Limiarizacao otsu"}]
print(json.dumps(object))
print('Limiarizacao otsu')
sys.stdout.flush()



# def compute_otsu_criteria(img, th):
#     # create the thresholded image
#     thresholded_im = np.zeros(img.shape)
#     thresholded_im[img >= th] = 1

#     # compute weights
#     nb_pixels = img.size
#     nb_pixels1 = np.count_nonzero(thresholded_im)
#     weight1 = nb_pixels1 / nb_pixels
#     weight0 = 1 - weight1

#     # if one the classes is empty, eg all pixels are below or above the threshold, that threshold will not be considered
#     # in the search for the best threshold
#     if weight1 == 0 or weight0 == 0:
#         return np.inf

#     # find all pixels belonging to each class
#     val_pixels1 = img[thresholded_im == 1]
#     val_pixels0 = img[thresholded_im == 0]

#     # compute variance of these classes
#     var0 = np.var(val_pixels0) if len(val_pixels0) > 0 else 0
#     var1 = np.var(val_pixels1) if len(val_pixels1) > 0 else 0

#     return weight0 * var0 + weight1 * var1

# img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
# # For testing purposes, one can use for example img = np.random.randint(0,255, size = (50,50))

# # testing all thresholds from 0 to the maximum of the image
# threshold_range = range(np.max(img)+1)
# criterias = [compute_otsu_criteria(img, th) for th in threshold_range]

# # best threshold is the one minimizing the Otsu criteria
# best_threshold = threshold_range[np.argmin(criterias)]