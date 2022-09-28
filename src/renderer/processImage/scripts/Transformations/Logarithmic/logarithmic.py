import cv2
import numpy as np
import sys
import json

img = cv2.imread(sys.argv[1])
c = 255 / np.log(1 + np.max(img))
image = c * (np.log(img+1))
image = np.array(image, dtype=np.uint8)
cv2.imwrite("./src/renderer/processImage/TransformedImages/log_"+sys.argv[2]+".png", image)

object = [{"url":"./src/renderer/processImage/TransformedImages/log_"+sys.argv[2]+".png","name":"logarithmic"}]
print(json.dumps(object))
print('Logarithmic')
sys.stdout.flush()