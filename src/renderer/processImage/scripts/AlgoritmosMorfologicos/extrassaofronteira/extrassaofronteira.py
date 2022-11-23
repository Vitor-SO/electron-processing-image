
import sys
import cv2
import json
from pgmagick import Image


imgPath = sys.argv[1]
img = Image(imgPath)
img.edge(1)
img.write('./src/renderer/processImage/FilteredImages/extrassaofronteira_'+sys.argv[2]+'.png')


object = [{"url":'./src/renderer/processImage/FilteredImages/extrassaofronteira_'+sys.argv[2]+'.png',"name":"Extracao de Fronteira"}]
print(json.dumps(object))
print('Extracao de Fronteira')
sys.stdout.flush()
