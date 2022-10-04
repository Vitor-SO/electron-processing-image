import json
import sys
import matplotlib.pyplot as plt
import cv2
from skimage.color import rgb2gray

def decimalToBinary(n):
    return bin(n).replace("0b", "")


def fillWithZeros(binary, qtdBits):
    bits = []
    s = 0
    if len(binary) < qtdBits:
        s = qtdBits - len(binary)
    c = 0
    for i in range(qtdBits):
        if i <= s - 1:
            bits.append(0)
        else:
            bits.append(int(binary[c]))
            c += 1
    return bits


def binaryToDecimal(n):
    num = n
    dec_value = 0

    # Initializing base
    # value to 1, i.e 2 ^ 0
    base = 1

    temp = num
    while temp:
        last_digit = temp % 10
        temp = int(temp / 10)
        dec_value += last_digit * base
        base = base * 2
    return dec_value


def planoDeBits(img, qtdBits):
    camadas = []
    for i in range(qtdBits):
        camadas.append(img.copy())

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            binary = decimalToBinary(int(img[i][j] * 256))
            bits = fillWithZeros(binary, qtdBits)
            for k in range(qtdBits):
                camadas[k][i][j] = bits[qtdBits - 1 - k]


    plt.imsave("./src/renderer/processImage/TransformedImages/bps1_"+sys.argv[2]+".png", camadas[1],cmap='gray')
    plt.imsave("./src/renderer/processImage/TransformedImages/bps2_"+sys.argv[2]+".png", camadas[2],cmap='gray')
    plt.imsave("./src/renderer/processImage/TransformedImages/bps3_"+sys.argv[2]+".png", camadas[3],cmap='gray')
    plt.imsave("./src/renderer/processImage/TransformedImages/bps4_"+sys.argv[2]+".png", camadas[4],cmap='gray')
    plt.imsave("./src/renderer/processImage/TransformedImages/bps5_"+sys.argv[2]+".png", camadas[5],cmap='gray')
    plt.imsave("./src/renderer/processImage/TransformedImages/bps6_"+sys.argv[2]+".png", camadas[6],cmap='gray')
    plt.imsave("./src/renderer/processImage/TransformedImages/bps7_"+sys.argv[2]+".png", camadas[7],cmap='gray')

object = [{"url":"./src/renderer/processImage/TransformedImages/bps1_"+sys.argv[2]+".png","name":"Camada 1"},
{"url":"./src/renderer/processImage/TransformedImages/bps2_"+sys.argv[2]+".png","name":"Camada 2"},
{"url":"./src/renderer/processImage/TransformedImages/bps3_"+sys.argv[2]+".png","name":"Camada 3"},
{"url":"./src/renderer/processImage/TransformedImages/bps4_"+sys.argv[2]+".png","name":"Camada 4"},
{"url":"./src/renderer/processImage/TransformedImages/bps5_"+sys.argv[2]+".png","name":"Camada 5"},
{"url":"./src/renderer/processImage/TransformedImages/bps6_"+sys.argv[2]+".png","name":"Camada 6"},
{"url":"./src/renderer/processImage/TransformedImages/bps7_"+sys.argv[2]+".png","name":"Camada 7"}
]
print(json.dumps(object))
print('Plano de bits')
sys.stdout.flush()


image = cv2.imread(sys.argv[1])
img = rgb2gray(image)
planoDeBits(img, 8)

