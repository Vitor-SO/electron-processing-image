import cv2
import numpy as np
import json
import sys
import cv2

# block_size = 41
# C = 10

# img = cv2.imread(sys.argv[1])
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# lap = cv2.Laplacian(img, cv2.CV_64F)
# lap = np.uint8(np.absolute(lap))
# result_img = np.vstack([img, lap])

# imgNormalthresh =cv2.threshold(lap, 50, 255, cv2.THRESH_BINARY)
# imgAdaptivethresh = cv2.adaptiveThreshold(lap, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C)
# imgAdapGauss = cv2.adaptiveThreshold(lap, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)

# imgNormalthresh_gray = cv2.cvtColor(imgNormalthresh, cv2.COLOR_GRAY2BGR)
# imgAdaptivethresh_gray = cv2.cvtColor(imgAdaptivethresh, cv2.COLOR_GRAY2BGR)
# imgAdapGauss_gray = cv2.cvtColor(imgAdapGauss, cv2.COLOR_GRAY2BGR)

# imgNormalthresh_blur = cv2.GaussianBlur(imgNormalthresh_gray,(5, 5), 0)
# imgAdaptivethresh_blur = cv2.GaussianBlur(imgAdaptivethresh_gray, (5, 5), 0)
# imgAdapGauss_blur = cv2.GaussianBlur(imgAdapGauss_gray,(5, 5), 0)

# imgNormalthresh_otsu = cv2.threshold(imgNormalthresh_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# imgAdaptivethresh_otsu = cv2.threshold(imgAdaptivethresh_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# imgAdapGauss_otsu = cv2.threshold(imgAdapGauss_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# img = cv.medianBlur(img,5)
# ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
# th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

# result = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

# cv2.imwrite('./src/renderer/processImage/FilteredImages/gradient_thnormal'+sys.argv[2]+'.png', imgNormalthresh_otsu)
# cv2.imwrite('./src/renderer/processImage/FilteredImages/gradient_thadaptivemean'+sys.argv[2]+'.png', imgAdaptivethresh_otsu)
# cv2.imwrite('./src/renderer/processImage/FilteredImages/gradient_thadaptivegauss'+sys.argv[2]+'.png', imgAdapGauss_otsu)


# object = [{"url":'./src/renderer/processImage/FilteredImages/gradient_thnormal'+sys.argv[2]+'.png',"name":"THRESH_BINARY"},
#         {"url":'./src/renderer/processImage/FilteredImages/gradient_thadaptivemean'+sys.argv[2]+'.png',"name":"ADAPTIVE_THRESH_MEAN_C"},
#         {"url":'./src/renderer/processImage/FilteredImages/gradient_thadaptivegauss'+sys.argv[2]+'.png',"name":"ADAPTIVE_THRESH_GAUSSIAN_C"}
# ]
# print(json.dumps(object))
# print('Gradient')
# sys.stdout.flush()
# def abs_sobel_thresh(img, sobel_kernel=3,orient='x', thresh=(0,255)):
#     # Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Apply x or y gradient with the OpenCV Sobel() function
#     # and take the absolute value
#     if orient == 'x':
#         abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel))
#     if orient == 'y':
#         abs_sobel = np.absolute(cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel))
#     # Rescale back to 8 bit integer
#     scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
#     # Create a copy and apply the threshold
#     binary_output = np.zeros_like(scaled_sobel)
#     # Here I'm using inclusive (>=, <=) thresholds, but exclusive is ok too
#     binary_output[(scaled_sobel >= thresh[0]) & (scaled_sobel <= thresh[1])] = 1

#     #cv2.imshow('SobelThresh',binary_output*255)
#     # Return the result
#     return binary_output*255

# def dir_threshold(img, sobel_kernel=3, thresh=(0, np.pi/2)):
#     # Grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Calculate the x and y gradients
#     sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
#     sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
#     # Take the absolute value of the gradient direction, 
#     # apply a threshold, and create a binary image result
#     absgraddir = np.arctan2(np.absolute(sobely), np.absolute(sobelx))

#     #scale_factor = np.max(absgraddir)/255
#     #absgraddir = (absgraddir/scale_factor).astype(np.uint8)
#     #cv2.imshow('absgradir',absgraddir)

#     binary_output =  np.zeros_like(absgraddir)
#     binary_output[(absgraddir >= thresh[0]) & (absgraddir <= thresh[1])] = 1

#     #cv2.imshow('DirThresh',binary_output)
#     # Return the binary image
#     return binary_output

# def mag_thresh(img, sobel_kernel=3, mag_thresh=(30, 100)):
#     # Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Take both Sobel x and y gradients
#     sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
#     sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
#     #cv2.imshow('sobelx',sobelx)
#     #cv2.imshow('sobely',sobely)

#     # Calculate the gradient magnitude
#     gradmag = np.sqrt(sobelx**2 + sobely**2)
    
#     # Rescale to 8 bit
#     scale_factor = np.max(gradmag)/255
#     gradmag = (gradmag/scale_factor).astype(np.uint8) 
#     #cv2.imshow('gradmag',gradmag)
#     # Create a binary image of ones where threshold is met, zeros otherwise
#     binary_output = np.zeros_like(gradmag)
#     binary_output[(gradmag >= mag_thresh[0]) & (gradmag <= mag_thresh[1])] = 1

#     #binary_output = cv2.cvtColor(binary_output,cv2.COLOR_GRAY2BGR)
#     #cv2.imshow('MagThresh',binary_output*255)
#     # Return the binary image
#     return binary_output*255

# def combined_gradient_thresholds(img,sobel_thresh = (30,120),magnitude_thresh = (30,120),direction_thresh=(0.8,1.2),display=False):
#     ksize=3

#     gradx = abs_sobel_thresh(img, orient='x', sobel_kernel=ksize, thresh=sobel_thresh)
#     grady = abs_sobel_thresh(img, orient='y', sobel_kernel=ksize, thresh=sobel_thresh)
    

#     mag_binary = mag_thresh(img, sobel_kernel=ksize, mag_thresh=magnitude_thresh)
#     dir_binary = dir_threshold(img, sobel_kernel=ksize, thresh=direction_thresh)
#     if (display):
#         cv2.imshow('SobelThreshX',gradx)
#         cv2.imshow('SobelThreshY',grady)
#         cv2.imshow('MagThresh',mag_binary)
#         cv2.imshow('Dir_thresh',dir_binary)
   
#     combined = np.zeros_like(dir_binary)
#     combined[((gradx >= 240) & (grady >= 240)) | ((mag_binary >= 240) & (dir_binary >= 240))] = 255

#     return combined


imgpath = sys.argv[1]
ddepth = cv2.CV_16S
kernelsize = 3

img = cv2.imread(imgpath)

#laplace
img = cv2.GaussianBlur(img, (3, 3), 0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(img_gray, ddepth, ksize = kernelsize)
abs_lap = cv2.convertScaleAbs(lap)

#adaptive
laplac = cv2.medianBlur(abs_lap, 5)
th1 = cv2.adaptiveThreshold(abs_lap, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#otsu
blur = cv2.GaussianBlur(abs_lap, (5, 5), 0)
ret2, th2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite('./src/renderer/processImage/FilteredImages/adapt_'+sys.argv[2]+'.png', th1)
cv2.imwrite('./src/renderer/processImage/FilteredImages/otsu_'+sys.argv[2]+'.png', th2)

object = [{"url":'./src/renderer/processImage/FilteredImages/adapt_'+sys.argv[2]+'.png',"name":"Limiarizacao adapt"}, 
    {"url":'./src/renderer/processImage/FilteredImages/otsu_'+sys.argv[2]+'.png',"name":"Limiarizacao otsu"},
]
print(json.dumps(object))
print('Limiarizacao com gradiente')
sys.stdout.flush()

