import numpy as np
import matplotlib.pyplot as plt
import cv2
import tkinter as tk
import Ecualizacion as ec


def creaMatriz(color, img):
    alto, ancho = img.shape[0:2]
    #crear matrices para el histograma
    matriz = np.zeros((256,1))

    #calcular los pixeles de cada intensidad
    for i in range(alto):
        for j in range (ancho):
            col = img.item(i, j, color)
            matriz[col] = matriz[col]+1

    return matriz


def plotearHist(matriz, col, titulo):
    plt.plot(matriz,color = col)
    plt.title(titulo)
    plt.xlim([0,256])
    plt.show()

imagen = input("Ingresa el nombre de la imagen: ")
img = plt.imread(imagen)

# print( img.shape )
# print( img.size )
alto, ancho = img.shape[0:2]
# 
# print(alto)
# print(ancho)

#crear matrices para el histograma
hb= creaMatriz(2, img)
hg= creaMatriz(1, img)
hr= creaMatriz(0, img)



plotearHist(hb, 'b', "Azul")
plotearHist(hg, 'g', "Verde")
plotearHist(hr, 'r', "Rojo")

imgNu = np.zeros((alto, ancho, 3), np.uint8)

imgNu , imgBN= ec.ecualizacion(img, imgNu)
heq= creaMatriz(2, imgNu)
plotearHist(heq, 'gray', "Equalizado")


plt.figure("Original")
plt.imshow(img)
plt.figure("Blaco.Negro")
plt.imshow(imgBN)
plt.figure("Con ecualizacion")
plt.imshow(imgNu)
plt.show()



#Obtener histograma. ravel regresa un arreglo continuo

plt.hist( blue.ravel(), bins=256 )  #8by
plt.title("azul")
plt.show()
#
plt.hist( green.ravel(), bins=256 )  #8by
plt.title("Verde")
plt.show()
plt.hist( red.ravel(), bins=256 )  #8by
plt.title("Rojo 256")
plt.show()
