import json
from skimage.io import imread,imsave
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import sys
import cv2

# def decimalToBinary(n):  
#     return bin(n).replace("0b", "")

# def preencherComZeros(binary, qtdBits):
#     bits = []
#     sobra = 0
#     if(len(binary) < qtdBits):
#         sobra = qtdBits - len(binary)
#     c = 0
#     for i in range(qtdBits):
#         if(i <= sobra-1):
#             bits.append(0)
#         else:
#             bits.append(int(binary[c]))
#             c += 1
#     return bits

# def binaryToDecimal(n): 
#     num = n; 
#     dec_value = 0; 
      
#     # Initializing base  
#     # value to 1, i.e 2 ^ 0 
#     base = 1; 
      
#     temp = num; 
#     while(temp): 
#         last_digit = temp % 10; 
#         temp = int(temp / 10); 
          
#         dec_value += last_digit * base; 
#         base = base * 2; 
#     return dec_value;

def planoDeBits(img, qtdBits):
    
#     camadas = []
#     for i in range(qtdBits):
#         camadas.append(img.copy())
        
#     for i in range(img.shape[0]):
#         for j in range(img.shape[1]):
#             binary = decimalToBinary(int(img[i][j]*256))
#             bits = preencherComZeros(binary, qtdBits)
#             for k in range(qtdBits):
#                 camadas[k][i][j] = bits[qtdBits-1-k]

        bit_image = img.copy()
        bit_image = bit_image >> qtdBits
        bit_image = bit_image & 1
        bit_image = bit_image * 255
        cv2.imwrite("./src/renderer/processImage/TransformedImages/bps7_"+sys.argv[2]+".png", bit_image)
                
    
    
    # plt.imsave("./src/renderer/processImage/TransformedImages/bps_"+sys.argv[2]+".png",camadas[0],cmap = 'gray')
    # plt.imsave("./src/renderer/processImage/TransformedImages/bps1_"+sys.argv[2]+".png",camadas[1],cmap = 'gray')
    # plt.imsave("./src/renderer/processImage/TransformedImages/bps2_"+sys.argv[2]+".png",camadas[2],cmap = 'gray')
    # plt.imsave("./src/renderer/processImage/TransformedImages/bps3_"+sys.argv[2]+".png",camadas[3],cmap = 'gray')
    # plt.imsave("./src/renderer/processImage/TransformedImages/bps4_"+sys.argv[2]+".png",camadas[4],cmap = 'gray')
    # plt.imsave("./src/renderer/processImage/TransformedImages/bps5_"+sys.argv[2]+".png",camadas[5],cmap = 'gray')
    # plt.imsave("./src/renderer/processImage/TransformedImages/bps6_"+sys.argv[2]+".png",camadas[6],cmap = 'gray')
    # plt.imsave("./src/renderer/processImage/TransformedImages/bps7_"+sys.argv[2]+".png",camadas[7],cmap = 'gray')

image = imread(sys.argv[1])
img = rgb2gray(image)
planoDeBits(img, 8)


# object = [
# # {"url":"./src/renderer/processImage/TransformedImages/bps_"+sys.argv[2]+".png","name":"camada 1"},
# # {"url":"./src/renderer/processImage/TransformedImages/bps1_"+sys.argv[2]+".png","name":"camada 2"},
# # {"url":"./src/renderer/processImage/TransformedImages/bps2_"+sys.argv[2]+".png","name":"camada 3"},
# # {"url":"./src/renderer/processImage/TransformedImages/bps3_"+sys.argv[2]+".png","name":"camada 4"},
# # {"url":"./src/renderer/processImage/TransformedImages/bps4_"+sys.argv[2]+".png","name":"camada 5"},
# # {"url":"./src/renderer/processImage/TransformedImages/bps5_"+sys.argv[2]+".png","name":"camada 6"},
# # {"url":"./src/renderer/processImage/TransformedImages/bps6_"+sys.argv[2]+".png","name":"camada 7"},
# {"url":"./src/renderer/processImage/TransformedImages/bps7_"+sys.argv[2]+".png","name":"camada 8"}
# ]
# print(json.dumps(object))
print("./src/renderer/processImage/TransformedImages/bps_"+sys.argv[2]+".png")
sys.stdout.flush()