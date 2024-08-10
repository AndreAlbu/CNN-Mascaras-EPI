import cv2 
import numpy as np

def tecnica_ajuste(imagem, altura_desejada, largura_desejada):

    imagem_ajustada = cv2.resize(imagem, (largura_desejada, altura_desejada))

    return imagem_ajustada

def tecnica_espelhamento(imagem, modo):
    
    '''
    modo -> O valor 0 indica que a imagem deve ser espelhada em torno do eixo horizontal (invertida verticalmente), 
                o valor de 1 indica que a imagem deve ser espelhada em torno do eixo vertical (invertida horizontalmente) 
                e um valor de -1 indica que a imagem deve ser espelhada em torno de ambos os eixos.
    '''
    
    imagem_espelhada = cv2.flip(imagem, modo)
    
    return imagem_espelhada
    

def tecnica_rotacao(imagem, angulo):

    altura, largura = imagem.shape[:2]

    centro = (largura / 2, altura / 2)

    matriz_rotacao = cv2.getRotationMatrix2D(centro, angulo, 1.0)

    imagem_rotacionada = cv2.warpAffine(imagem, matriz_rotacao, (largura, altura))
    
    return imagem_rotacionada

