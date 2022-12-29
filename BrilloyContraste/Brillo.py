import numpy as np
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import Slider


#Crea nuevos valores para B
def valNuevB(val, imgCopy, g):
    hba= np.zeros((256,1))
    for i in range(alto):
        for j in range (ancho):
            inte = img.item(i, j, 2)
            inte = (inte*g) + val;
            inte = int(inte)
            inte = verifica(inte)
            imgCopy.itemset((i, j, 2), inte)

            hba[inte] = hba[inte]+1
    return hba
#Crea nuevos valores para G
def valNuevG(val, imgCopy, c):
    hga= np.zeros((256,1))
    for i in range(alto):
        for j in range (ancho):
            inte = img.item(i, j, 1)
            inte = (inte*c) + val;
            inte = int(inte)
            inte = verifica(inte)
            imgCopy.itemset((i, j, 1), inte)

            hga[inte] = hga[inte]+1
    return hga
#Crea nuevos valores para R
def valNuevR(val, imgCopy, c):
    hra= np.zeros((256,1))
    for i in range(alto):
        for j in range (ancho):
            inte = img.item(i, j, 0)
            inte = (inte*c) + val;
            inte = int(inte)
            inte = verifica(inte)
            imgCopy.itemset((i, j, 0), inte)

            hra[inte] = hra[inte]+1
    return hra

#verificar el valor de 0 a 255
def verifica(intensidad):
    if(intensidad>255):
        return 255
    elif(intensidad < 0):
        return 0
    else:
        return intensidad;

#cambiar los valores de los histogramas
def val_update(val):
    imgAux = np.copy(img)
    valS = slider2.val
    print("cambiando Brillo")
    nuevosB = valNuevB(valS, imgAux,1)
    nuevosG = valNuevG(valS, imgAux,1)
    nuevosR = valNuevR(valS, imgAux,1)

    print(nuevosB)

    pB.set_ydata(nuevosB)
    pG.set_ydata(nuevosG)
    pR.set_ydata(nuevosR)

    plt.figure(2)
    plt.subplot(2,2,2)
    plt.imshow(imgAux)
    plt.title("Brillo "+str(valS))
    plt.show()

def val_update2(val):
    imgAux2 = np.copy(img)
    valG = slider3.val
    valC = sliderb1.val
    print("cambiando contraste 0-1")

    nuevosB = valNuevB(valC, imgAux2,valG)
    nuevosG = valNuevG(valC, imgAux2,valG)
    nuevosR = valNuevR(valC, imgAux2,valG)


    pBc1.set_ydata(nuevosB)
    pGc1.set_ydata(nuevosG)
    pRc1.set_ydata(nuevosR)

    plt.figure(2)
    plt.subplot(2,2,3)
    plt.imshow(imgAux2)
    plt.title("Cont G "+str(valG) + " C: "+str(valC))
    plt.show()

def val_update3(val):

    imgAux3 = np.copy(img)
    valG = slider4.val
    valC = sliderb2.val
    print("cambiando contraste >1")
    nuevosB = valNuevB(valC, imgAux3, valG)
    nuevosG = valNuevG(valC, imgAux3, valG)
    nuevosR = valNuevR(valC, imgAux3, valG)

    pBc2.set_ydata(nuevosB)
    pGc2.set_ydata(nuevosG)
    pRc2.set_ydata(nuevosR)

    plt.figure(2)
    plt.subplot(2,2,4)
    plt.imshow(imgAux3)
    plt.title("Cont G: "+str(valG) + " C: "+str(valC))
    plt.show()


#pedir el nombre de la imagen
imagen = input("Ingresa el nombre de la imagen: ")
img = plt.imread(imagen)

print( img.shape )
print( img.size )
alto, ancho = img.shape[0:2]

print(alto)
print(ancho)

#crear matrices para el histograma
hb= np.zeros((256,1))
hg= np.zeros((256,1))
hr= np.zeros((256,1))

#calcular los pixeles de cada intensidad
for i in range(alto):
    for j in range (ancho):
        b = img.item(i, j, 2)
        g = img.item(i, j, 1)
        r = img.item(i, j, 0)
        hb[b] = hb[b]+1
        hg[g] = hg[g]+1
        hr[r] = hr[r]+1

#FIGURA1 HISTOGRAMAS PARA EL BRILLO
plt.figure(1)
plt.subplot(3,1,1)
pB, = plt.plot(hb,color = 'blue')
plt.title("Azul")
plt.subplot(3,1,2)
pG, = plt.plot(hg, color = 'green')
plt.title("Verde")
plt.subplot(3,1,3)
pR, = plt.plot(hr,color = 'red')
plt.title("Rojo")

#creación y posición del slider
axSlider2 = plt.axes([0.1,0.005, 0.8, 0.05])
slider2 = Slider(ax = axSlider2, label = "Brillo", valmin=-255, valmax=255, valinit=0, valfmt='%1.2f', valstep =1,  closedmax = True, color = 'cyan')
slider2.on_changed(val_update)

#FIGURA2 IMAGENES MODIFICADAS POR CONTRASTE Y BRILLO
plt.figure(2)
plt.subplot(2,2,1)
plt.title("ORIGINAL")
plt.imshow(img)

#FIGURA3 HISTOGRAMAS PARA EL CONTRASTE
plt.figure(3)
plt.subplot(3,2,1)
pBc1, = plt.plot(hb,color = 'blue')
plt.title("Contraste 1")

plt.subplot(3,2,3)
pGc1, = plt.plot(hg, color = 'green')
plt.subplot(3,2,5)
pRc1, = plt.plot(hr,color = 'red')

plt.subplot(3,2,2)
pBc2, = plt.plot(hb,color = 'blue')
plt.title("Contraste 2")

plt.subplot(3,2,4)
pGc2, = plt.plot(hg, color = 'green')
plt.subplot(3,2,6)
pRc2, = plt.plot(hr,color = 'red')


axSlider3 = plt.axes([0.2,0.005, 0.3, 0.01])
slider3 = Slider(ax = axSlider3, label = "Gama1", valmin=0, valmax=1, valinit=0, valfmt='%1.2f', valstep =0.1,  closedmax = True, color = 'yellow')
slider3.on_changed(val_update2)

axSliderb1 = plt.axes([0.6,0.005, 0.3, 0.01])
sliderb1 = Slider(ax = axSliderb1, label = "C1", valmin=-255, valmax=255, valinit=0, valfmt='%1.2f', valstep =1,  closedmax = True, color = 'yellow')
sliderb1.on_changed(val_update2)

axSlider4 = plt.axes([0.2,0.05, 0.3, 0.01])
slider4 = Slider(ax = axSlider4, label = "Gama2", valmin=2, valmax=255, valinit=0, valfmt='%1.2f', valstep =1,  closedmax = True, color = 'pink')
slider4.on_changed(val_update3)

axSliderb2 = plt.axes([0.6,0.05, 0.3, 0.01])
sliderb2 = Slider(ax = axSliderb2, label = "C2", valmin=-255, valmax=255, valinit=0, valfmt='%1.2f', valstep =1,  closedmax = True, color = 'pink')
sliderb2.on_changed(val_update3)

plt.show()
