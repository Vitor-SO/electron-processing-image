
import cv2
import sys
from matplotlib import pyplot as plt

imgPath = sys.argv[1]

img = cv2.imread(imgPath)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram, color = col)
    plt.xlim([0, 256])
plt.title('Histogram')
plt.xlabel('Pixels')
plt.ylabel('Intensity')
plt.grid(True)
# plt.show()

# salvar o grafico como imagem
cv2.imwrite('./src/renderer/processImage/TransformedImages/histogram_'+sys.argv[2]+'.png',histogram)
