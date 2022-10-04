import json
import cv2
import sys

img = cv2.imread(sys.argv[1], 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(10, 10))
cl1 = clahe.apply(img)
cv2.imwrite("./src/renderer/processImage/TransformedImages/eq_local_"+sys.argv[2]+".png", cl1)


object = [{"url":"./src/renderer/processImage/TransformedImages/eq_local_"+sys.argv[2]+".png","name":"Equalizacao Local"}]
print(json.dumps(object))
print('Equalizacao Local')
sys.stdout.flush()