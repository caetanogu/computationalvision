import cv2 as cv
import numpy as np

def findObject(image, template, threshold, method):

    #Carrega a imagem selecionada e o objeto a ser encontrado
    img = cv.imread(image, cv.IMREAD_UNCHANGED)
    temp = cv.imread(template, cv.IMREAD_UNCHANGED)

    #Seleciona o método utilizado para comparação (todos os métodos disponiveis estão na lista abaixo)
    methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]
    
    #Procura o template requisitado na imagem fornecida e com o método escolhido
    result = cv.matchTemplate(img, temp, methods[method])

    #Encontra os valores de maximo e minimo e suas respectivas coordenadas
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

    #Caso o método escolhido seja TM_SQDIFF ou TM_SQDIFF_NORMED pega o valor mínimo
    if method == 4 or method == 5:
        top_left = minLoc

        #Se o valor minimo for menor ou igual ao threshold, imagem encontrada
        if minVal <= threshold:
            print('Imagem encontrada')

            #Calcula o canto direito do retangulo somando as coordenadas x e y com os respectivos tamanhos das suas matrizes
            bottom_right = (top_left[0] + temp.shape[1], top_left[1] + temp.shape[0])

            #Desenha o retângulo a partir das coordenadas encontradas
            cv.rectangle(img, top_left, bottom_right, color=(0, 0, 255), thickness=2, lineType=cv.LINE_4)

        elif minVal > threshold:
            print('Imagem não encontrada')

    else:
        top_left = maxLoc

        #Se o valor máximo for maior ou igual ao threshold, imagem encontrada
        if maxVal >= threshold:
            print('Imagem encontrada')

            #Calcula o canto direito do retangulo somando as coordenadas x e y com os respectivos tamanhos das suas matrizes
            bottom_right = (top_left[0] + temp.shape[1], top_left[1] + temp.shape[0])

            #Desenha o retângulo a partir das coordenadas encontradas
            cv.rectangle(img, top_left, bottom_right, color=(0, 0, 255), thickness=2, lineType=cv.LINE_4)

        elif maxVal < threshold:
            print('Imagem não encontrada')

    #print(minVal, maxVal)
    cv.imshow('Resultado', img)
    cv.waitKey()

#Rotina principal do programa
print('OBJECT DETECTOR ALGORYTHIM USING OPENCV')
print('Author: Gustavo Caetano da Silva')
print('Date: 19/10/21')

imagem = input('Digite o nome da imagem e sua extensão (por exemplo: mario.jpg): ')
pad = input('Digite o nome do arquivo de filtro que será utilizado e sua respectiva extensão: ')

findObject(imagem, pad, 0.2, 5)