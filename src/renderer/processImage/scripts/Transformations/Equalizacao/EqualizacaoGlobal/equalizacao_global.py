import json
import sys
import cv2  
import sys     
        
img = cv2.imread(sys.argv[1])
img_to_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_to_yuv[:, :, 0] = cv2.equalizeHist(img_to_yuv[:, :, 0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)

cv2.imwrite("./src/renderer/processImage/TransformedImages/eq_global_"+sys.argv[2]+".png", hist_equalization_result)

object = [{"url":"./src/renderer/processImage/TransformedImages/eq_global_"+sys.argv[2]+".png","name":"Equalizacao Global"}]
print(json.dumps(object))
print('Equalizacao Global')
sys.stdout.flush()
        