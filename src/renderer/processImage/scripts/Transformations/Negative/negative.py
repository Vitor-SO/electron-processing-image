import sys
from PIL import Image
import json
import cv2
        
img = cv2.imread(sys.argv[1])
image = (255-img)
cv2.imwrite("./src/renderer/processImage/TransformedImages/negative_"+sys.argv[2]+".png", image)


# # print("./src/renderer/processImage/TransformedImages/negative_"+sys.argv[2]+".png")
object = [{"url":"./src/renderer/processImage/TransformedImages/negative_"+sys.argv[2]+".png","name":"negative"}]
print(json.dumps(object))
print('Negative')
sys.stdout.flush()