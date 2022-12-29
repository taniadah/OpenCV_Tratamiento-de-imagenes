import numpy as np
import matplotlib.pyplot as plt
import cv2
import math as m

def pngTojpg(img):
    al, an = img.shape[0:2]
    bgr = np.zeros((al,an,3),np.uint8)
    for i in range(al):
        for j in range(an):
            b = img.item(i,j,2)
            g = img.item(i,j,1)
            r = img.item(i,j,0)
            b = int(b*255)
            g = int(g*255)
            r = int(r*255)
            bgr[i,j] = [r,g,b]
    return bgr

def rotacion(img, grados):

    al,an = img.shape[0:2]
    grados = m.radians(grados)
    sen = m.sin(grados)
    cose = m.cos(grados)

    bgr = np.zeros((imagen.shape),np.uint8)
    auxImg = bgr

    for i in range(an):
        for j in range(al):
            x = i * cose - j*sen -(an/2)*cose +(al/2)*sen+(an/2)
            y = i * sen + j*cose -(an/2)*sen-(al/2)*cose+(al/2)
            x = int(x)
            y= int(y)
            if (x<an and y<al and x>0 and y>0):
                b = img.item(j, i, 0)
                g = img.item(j, i, 1)
                r = img.item(j, i, 2)
                auxImg.itemset((y,x,0),b)
                auxImg.itemset((y,x,1),g)
                auxImg.itemset((y,x,2),r)
    return auxImg

def plotear(titulo, img, i):
    plt.figure(titulo)
    plt.subplot(3,3,i)
    plt.imshow(img)

def promediar(imagenes, img):
    al, an = img.shape[0:2]
    imgAux =  np.zeros(img.shape,np.uint8)

    for i in range(al):
        for j in range(an):
            sumaB = 0
            sumaG = 0
            sumaR = 0
            for k in range(9):
                b = imagenes[k].item(i,j,2)
                g = imagenes[k].item(i,j,1)
                r = imagenes[k].item(i,j,0)
                sumaB += b
                sumaG += g
                sumaR += r
                promB = int(sumaB/9)
                promG = int(sumaG/9)
                promR = int(sumaR/9)
                imgAux[i,j] = [promR, promG, promB]

    return imgAux

jpg = plt.imread("pruebaR.jpg")
imagen = jpg
#print(imagen.shape)

##jpg = pngTojpg(imagen)

imagenes = []

for i in range(9):
    grad = -40*i
    imagenes.append(rotacion(jpg, grad))


plt.figure("Imagen")
plt.imshow(jpg)

prom = promediar(imagenes,jpg)


for i in range(9):
    plotear("Rotaciones", imagenes[i], i+1)

plt.figure("Promediado")
plt.imshow(prom)

# axSlider2 = plt.axes([0.1,0.005, 0.8, 0.05])
# slider2 = Slider(ax = axSlider2, label = "Rotación", valmin=0, valmax=360, valinit=0, valfmt='%1.2f', valstep =18,  closedmax = True, color = 'cyan')
# slider2.on_changed(val_update)

plt.show()
