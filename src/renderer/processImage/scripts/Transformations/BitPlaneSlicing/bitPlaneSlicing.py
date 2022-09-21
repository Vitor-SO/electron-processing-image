from skimage.io import imread,imsave
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import sys
# import random
# import math
# import numpy as np

def decimalToBinary(n):  
    return bin(n).replace("0b", "")

def preencherComZeros(binary, qtdBits):
    bits = []
    sobra = 0
    if(len(binary) < qtdBits):
        sobra = qtdBits - len(binary)
    c = 0
    for i in range(qtdBits):
        if(i <= sobra-1):
            bits.append(0)
        else:
            bits.append(int(binary[c]))
            c += 1
    return bits

def binaryToDecimal(n): 
    num = n; 
    dec_value = 0; 
      
    # Initializing base  
    # value to 1, i.e 2 ^ 0 
    base = 1; 
      
    temp = num; 
    while(temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
          
        dec_value += last_digit * base; 
        base = base * 2; 
    return dec_value;

def planoDeBits(img, qtdBits):
    
    camadas = []
    for i in range(qtdBits):
        camadas.append(img.copy())
        
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            binary = decimalToBinary(int(img[i][j]*256))
            bits = preencherComZeros(binary, qtdBits)
            for k in range(qtdBits):
                camadas[k][i][j] = bits[qtdBits-1-k]
                
    
    
    plt.imsave("./src/renderer/processImage/TransformedImages/bps_"+sys.argv[2]+".png",camadas[7],cmap = 'gray')
        

image = imread(sys.argv[1])
img = rgb2gray(image)
planoDeBits(img, 8)