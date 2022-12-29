import numpy as np
import matplotlib.pyplot as plt
import cv2

def bn(imagen):
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(imagen)
    histo = cv2.calcHist([imagen], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([eq], [0], None, [256], [0,256])
    cv2.imshow("Diferencias", np.hstack([imagen, eq]))
    plt.plot(histo, color = 'yellow')
    plt.plot(hist2, color = 'red')
    plt.xlim([0,256])
    return imagen

def nuevoHis(imagen):
    alto, ancho = imagen.shape[0:2]
    matriz = np.zeros((256,1))
    for i in range(alto):
        for j in range (ancho):
            col = imagen.item(i, j, 0)
            matriz[col] = matriz[col]+1
    return matriz


def validar(nuevaIntensidad):
    if nuevaIntensidad>255:
        return 255
    else:
        return nuevaIntensidad

def ecualizacion(imagen, imgNu):
    alto, ancho = imagen.shape[0:2]
    imagenBN = bn(imagen)
    imagenBN = cv2.cvtColor(imagenBN, cv2.COLOR_BGR2RGB)
    histo = nuevoHis(imagenBN)
    acum = 0
    histoAux = np.zeros((256,1))

    for i in range(0,255):
        acum += histo[i]/(alto*ancho)
        histoAux[i] = acum


    for i in range(alto):
        for j in range(ancho):
            inte = imagenBN.item(i, j, 0)
            ni = int(histoAux[inte]*255)
            ni = validar(ni)
            imgNu.itemset((i,j,0), ni)
            imgNu.itemset((i,j,1), ni)
            imgNu.itemset((i,j,2), ni)
    return imgNu, imagenBN
