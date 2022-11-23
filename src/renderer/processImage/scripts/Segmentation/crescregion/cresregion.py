import numpy as np
import cv2
import sys
import json


def region_growing(img, seed):
    # Parameters for region growing
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    region_threshold = 0.2
    region_size = 1
    intensity_difference = 0
    neighbor_points_list = []
    neighbor_intensity_list = []

    # Mean of the segmented region
    region_mean = img[seed]

    # Input image parameters
    height, width = img.shape
    image_size = height * width

    # Initialize segmented output image
    segmented_img = np.zeros((height, width, 1), np.uint8)

    # Region growing until intensity difference becomes greater than certain
    #  threshold
    while (intensity_difference < region_threshold) & (region_size < image_size):
        # Loop through neighbor pixels
        for i in range(4):
            # Compute the neighbor pixel position
            x_new = seed[0] + neighbors[i][0]
            y_new = seed[1] + neighbors[i][1]

            # Boundary Condition - check if the coordinates are
            # inside the image
            check_inside = (x_new >= 0) & (y_new >= 0) & (x_new < height) & (y_new < width)

            # Add neighbor if inside and not already in segmented_img
            if check_inside:
                if segmented_img[x_new, y_new] == 0:
                    neighbor_points_list.append([x_new, y_new])
                    neighbor_intensity_list.append(img[x_new, y_new])
                    segmented_img[x_new, y_new] = 255

        # Add pixel with intensity nearest to the mean to the region
        distance = abs(neighbor_intensity_list-region_mean)
        pixel_distance = min(distance)
        index = np.where(distance == pixel_distance)[0][0]
        segmented_img[seed[0], seed[1]] = 255
        region_size += 1

        # New region mean
        region_mean = (region_mean*region_size +
                       neighbor_intensity_list[index])/(region_size+1)

        # Update the seed value
        seed = neighbor_points_list[index]
        # Remove the value from the neighborhood lists
        neighbor_intensity_list[index] = neighbor_intensity_list[-1]
        neighbor_points_list[index] = neighbor_points_list[-1]

    return segmented_img


imgPath = sys.argv[1]
img = cv2.imread(imgPath, 0)

resized = cv2.resize(img, (256, 256))
seed = (100, 100)
segmented_img = region_growing(resized, seed)

cv2.imwrite('./src/renderer/processImage/FilteredImages/crescimento_'+sys.argv[2]+'.png', segmented_img)

object = [{"url":'./src/renderer/processImage/FilteredImages/crescimento_'+sys.argv[2]+'.png',"name":"crescimento regiao"}]
print(json.dumps(object))
print('Crescimento regiao')
sys.stdout.flush()

# import matplotlib.pyplot as plt
# import numpy as np
# from collections import deque
# from scipy import signal as sg
# import math

# import sys
# import cv2
# import json

# def get_slices(img):
#     h, w = img.shape
#     slices = []
#     for i in range(h):
#         if img[i, 0] == 255:
#             slices.append(i)
#     return slices

# def get_vizinhos(x, y, w, h):
#     lista = deque()
#     pontos = [(x-1,y), (x+1, y), (x,y-1), (x,y+1),
#               (x-1,y+1), (x+1, y+1), (x-1,y-1), (x+1,y-1),
#              ]
#     for p in pontos:
#         if (p[0]>=0 and p[1]>=0 and p[0]<w and p[1]<h):
#             lista.append((p[0], p[1]))        
#     return lista

# def get_coor_slices (img, slices):
    
#     count = 0
#     w, h = img.shape
#     fila = deque()
    
#     for x in range(w):
#         for y in range(h):
#             if slices[x,y]==255:
#                 count = count+1
#                 fila.append((x,y))
#     return fila

# def get_maior_dif(img, pixel, slices):
#     x, y = pixel
#     h, w = img.shape # ou img.shape
#     vizinhos = get_vizinhos(x, y, w, h)
#     difs = np.zeros(len(vizinhos))
#     for i in range(len(vizinhos)):
#         difs[i] = abs(img[pixel] - img[vizinhos[i]])        
#     return difs.mean()

# def get_epsilon (img):
#     semente = get_slices(img)
#     coor_p_semente = get_coor_slices(img, semente)
#     difs = np.zeros(len(coor_p_semente))
#     for i in range(len(coor_p_semente)):
#         pixel = coor_p_semente.pop()
#         difs[i] = get_maior_dif(img, pixel, semente)
    
#     return difs.mean().round(5)

# def get_area(img):
#     w, h = img.shape
#     area = 0
#     for i in range (w):
#         for j in range (h):
#             if img[i, j] == 255:
#                 area = area + 1
#     return area

# def ver_vizinho_branco(img, x, y):
#     h, w = img.shape
#     vizinhos = get_vizinhos(x, y, w, h)
#     for i in range(len(vizinhos)):
#         if img[vizinhos[i]]==0 and img[x, y]==255:
#             return True
#         return False

# def get_coor_ps (img):
#     # Após a imagem passar pelo processo de convolucao sao perdirdos
#     # 4 pixeis
#     w, h = img.shape
#     coor = deque()
#     for i in range (w-2):
#         for j in range (h-2):
#             if img[i, j] == 255:
#                 coor.append((i, j))
#     return coor

# def get_perimetro(img):
#     h, w = img.shape
#     perimetro = 0
#     for i in range (h):
#         for j in range (w):
#             if ver_vizinho_branco(img, i, j):
#                 perimetro = perimetro + 1
#     return perimetro+1 # Quando ocorrem erros na segmentacao

# def get_circularidade (img):
    
#     return ((4*math.pi*get_area(img)/(get_perimetro(img)**2)))


# def get_desvioP (img, img_seg):
#     #w, h = img_seg.shape
#     coor_ps = get_coor_ps(img_seg)
#     intensi_pix = np.zeros(len(coor_ps))
#     for i in range (intensi_pix.size):
#         intensi_pix[i] = img[coor_ps[i]]
    
#     return intensi_pix.std()

# def get_razao_ap (img):
#     return (get_area(img))/(get_perimetro(img))


# def obterSemente(image):
#     w, h = image.shape
#     semente = np.zeros((w, h))
#     semente[:, :3] = 255 # Lateral esquerda
#     semente[:, (h-3):] = 255 # Lateral direita
    
#     return semente

# def vizinhos(x, y, w, h):
#     lista = deque()
    
#     pontos = [(x-1,y), (x+1, y), (x,y-1), (x,y+1),
#               (x-1,y+1), (x+1, y+1), (x-1,y-1), (x+1,y-1),
#              ]
#     for p in pontos:
#         if (p[0]>=0 and p[1]>=0 and p[0]<w and p[1]<h):
#             lista.append((p[0], p[1]))
            
#     return lista
    
# def crescerRegiao(image, reg, epsilon=5):
#     w, h = image.shape
    
#     fila = deque()
#     for x in range(w):
#         for y in range(h):
#             if reg[x,y]==255:
#                 fila.append((x,y))
                
#     while fila: 
#         ponto = fila.popleft()
#         x = ponto[0]
#         y = ponto[1]

#         v_list = vizinhos(x, y, w, h)
#         for v in v_list:
#             v_x = v[0]
#             v_y = v[1]
#             if( (reg[v_x][v_y]!=255) and (abs(image[x][y]-image[v_x][v_y])<epsilon)):
#                 reg[v_x][v_y] = 255
#                 fila.append((v_x,v_y))
#     return reg
                
# # def plots(p1, p2, pil):
# #     fig = plt.figure(figsize=(9,3), dpi=80)
# #     a = fig.add_subplot(1,3,1)
# #     a.axis('off')
# #     plt.imshow(p1, cmap=plt.cm.gray)
# #     a.set_title('Original em tons de cinza')

# #     a = fig.add_subplot(1,3,2)
# #     a.axis('off')
# #     plt.imshow(p2, cmap=plt.cm.gray)
# #     a.set_title('Imagem segmentada')

# #     a = fig.add_subplot(1,3,3)
# #     a.axis('off')
# #     plt.imshow(p1, cmap=plt.cm.gray)
# #     plt.imshow(p2, alpha=0.5)
# #     a.set_title('Região Segmentada')

# #     plt.savefig('resultados/'+pil+'/('+x+').jpg')

# #     plt.show()
    
# def inv_img (img):
#     h, w = img.shape
#     for i in  range(h):
#         for j in  range(w):
#             if img[i, j] == 0:
#                 img[i, j] = 255
#             else:
#                 img[i, j] = 0
#     return img

    
# k = 0
# pil = 'WB' 
# qtd_imgs = 1
# area_media = 0
# circ_media = 0
# razao_ap_media = 0
# desv_padrao_medio = 0

# imgPath = sys.argv[1]

# for x in range(qtd_imgs):
#     img = cv2.imread(imgPath, 0)
#     img = ( img * 255).round().astype(np.uint8)
#     semente = obterSemente(img)
#     media = [[1./9., 1./9., 1./9.], 
#           [1./9., 1./9., 1./9.],
#           [1./9., 1./9., 1./9.]]
#     c_media =  sg.convolve(img, media, 'valid')
#     v = get_epsilon(c_media)
#     regiao = crescerRegiao(c_media, semente, v)
#     regiao = inv_img(regiao)
#     regiao = regiao.astype(np.uint8)
#     regiao = cv2.medianBlur(regiao, 3)
  
    


# cv2.imwrite('./src/renderer/processImage/FilteredImages/crescimento_'+sys.argv[2]+'.png', regiao)

# object = [{"url":'./src/renderer/processImage/FilteredImages/crescimento_'+sys.argv[2]+'.png',"name":"crescimento regiao"}]
# print(json.dumps(object))
# print('Crescimento regiao')
# sys.stdout.flush()


