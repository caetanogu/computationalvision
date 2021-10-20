import cv2 as cv
import numpy as np

#Carrega as imagens e o template requisitado
img = cv.imread('albion.jpg', cv.IMREAD_UNCHANGED)
temp = cv.imread('cabbage_a.jpg', cv.IMREAD_UNCHANGED)

#Carrega a lista de métodos possíveis a serem utilizados
methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

#Aplica o filtro na imagem
result = cv.matchTemplate(img,temp,methods[5])

#Determina a confianca da imagem
threshold = 0.14

#Encontra as posições dos objetos desejados
locations = np.where(result <= threshold)
locations = list(zip(*locations[::-1]))
#print(locations)

if locations:
    print('Imagem encontrada')

    #Loop para encontrar as posições dos retângulos
    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + temp.shape[1], top_left[1] + temp.shape[0])

        #Desenha os retangulos nas posições encontradas
        cv.rectangle(img, top_left, bottom_right, color=(0, 0, 255), thickness=2, lineType=cv.LINE_4)
    
    cv.imshow('Display', img)
    cv.waitKey()

else:
    print('Imagem não encontrada')