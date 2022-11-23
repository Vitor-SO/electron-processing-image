import numpy as np
import cv2
import sys
import json

imgPath = sys.argv[1]
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)

th, im_th = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

im_floodfill = im_th.copy()

h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

cv2.floodFill(im_floodfill, mask, (0,0), 255)

im_floodfill_inv = cv2.bitwise_not(im_floodfill)

img_out = im_th | im_floodfill_inv


cv2.imwrite('./src/renderer/processImage/FilteredImages/preenchimentoborda_limiar'+sys.argv[2]+'.png', im_th)
cv2.imwrite('./src/renderer/processImage/FilteredImages/preenchimentoborda_InvertedFloodfilled'+sys.argv[2]+'.png', im_floodfill_inv)
cv2.imwrite('./src/renderer/processImage/FilteredImages/preenchimentoborda_'+sys.argv[2]+'.png', img_out)

object = [{"url":'./src/renderer/processImage/FilteredImages/preenchimentoborda_limiar'+sys.argv[2]+'.png',"name":"Preenchimento de Borda Limiar"},
    {"url":'./src/renderer/processImage/FilteredImages/preenchimentoborda_InvertedFloodfilled'+sys.argv[2]+'.png',"name":"Preenchimento de Borda Inverted Floodfilled"},
    {"url":'./src/renderer/processImage/FilteredImages/preenchimentoborda_'+sys.argv[2]+'.png',"name":"Preenchimento de Borda"}]
print(json.dumps(object))
print('Preenchimento de Borda')
sys.stdout.flush()