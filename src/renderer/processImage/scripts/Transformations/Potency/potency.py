from skimage import exposure
from skimage import io
import sys
import json
# from pylab import *

img = io.imread(sys.argv[1])
gamma_corrected1 = exposure.adjust_gamma(img, 0.3)
gamma_corrected2 = exposure.adjust_gamma(img, 0.4)
gamma_corrected3 = exposure.adjust_gamma(img, 0.6)

io.imsave("./src/renderer/processImage/TransformedImages/potency_"+sys.argv[2]+".png",gamma_corrected1)
io.imsave("./src/renderer/processImage/TransformedImages/potency1_"+sys.argv[2]+".png",gamma_corrected2)
io.imsave("./src/renderer/processImage/TransformedImages/potency2_"+sys.argv[2]+".png",gamma_corrected3)


object = [{"url":"./src/renderer/processImage/TransformedImages/potency_"+sys.argv[2]+".png","name":"Potencia 0.3"},
{"url":"./src/renderer/processImage/TransformedImages/potency1_"+sys.argv[2]+".png","name":"Potencia 0.4"},
{"url":"./src/renderer/processImage/TransformedImages/potency2_"+sys.argv[2]+".png","name":"Potencia 0.6"}]
print(json.dumps(object))
print('Potencia')
sys.stdout.flush()
