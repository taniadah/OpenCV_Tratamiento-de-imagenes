import numpy as np
import matplotlib.pyplot as plt
import random
import cv2


def salP(imagen, prob):
    al, an = img.shape[0:2]
    imgAux = np.zeros((al,an,3),np.uint8)
    thres = 1-prob
    for i in range(al):
        for j in range(an):
            alt = random.random()
            #print(alt)
            if alt<prob:
                imgAux.itemset((i,j,0), 0)
                imgAux.itemset((i,j,1), 0)
                imgAux.itemset((i,j,2), 0)
            elif alt>thres:
                imgAux.itemset((i,j,0),255)
                imgAux.itemset((i,j,1),255)
                imgAux.itemset((i,j,2),255)
            else:
                imgAux.itemset((i,j,0),imagen.item(i,j,0))
                imgAux.itemset((i,j,1),imagen.item(i,j,1))
                imgAux.itemset((i,j,2),imagen.item(i,j,2))
    return imgAux


def ruidoGau(image, mean = 0, var =0.001):
    mean = 0
    #var=0.001
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)

    return out

def filter2Df(img, mas):
        al, an = img.shape[0:2]
        bgr = np.zeros((al,an,3),np.uint8)
        auxImg = bgr
        if mas%2 == 0:
            mas-=1
        mas2 = int(mas/2)
        cont = 0
        aux =( mas*mas )
        vector = np.zeros(aux)
        vectorG = np.zeros(aux)
        vectorB = np.zeros(aux)

        for i in range(al):
            for j in range(an):
                for k in range(i-mas2, i+mas2+1):
                    for l in range(j-mas2, j+mas2+1):
                        if  k>=0 and k<al and l<an and l>=0:
                            vector[cont] = img.item(k,l, 0)
                            vectorG[cont] = img.item(k,l, 1)
                            vectorB[cont] = img.item(k,l, 2)

                            cont+=1
                vector.sort()
                vectorG.sort()
                vectorB.sort()
                a = int(aux/2)
                nuvR = int(vector[a])
                nuvG = int(vectorG[a])
                nuvB = int(vectorB[a])

                auxImg.itemset((i,j, 0), nuvR)
                auxImg.itemset((i,j, 1), nuvG)
                auxImg.itemset((i,j, 2), nuvB)
                cont = 0
        return auxImg



imagen = input("Ingresa el nombre de la imagen: ")
img = plt.imread(imagen)


print( img.shape )
print( img.size )
alto, ancho = img.shape[0:2]

print(alto)
print(ancho)
ruidoSP = salP(img, .09)

#ruidoSP = cv2.cvtColor(ruidoSP, cv2.COLOR_BGR2RGB)
gaussNo = ruidoGau(img, mean=0, var=0.09)

#gaussNo = cv2.cvtColor(gaussNo, cv2.COLOR_BGR2RGB)
out1 = salP(img, 0.02)

kernel = np.ones((3,3),np.float32)/9
processed_image = cv2.filter2D(ruidoSP,-1,kernel)

# Agregue ruido gaussiano con un valor medio de 0 y una varianza de 0.01
out2 = ruidoGau(img, mean=0, var=0.01)
fil2D = filter2Df(ruidoSP, 3)

# Mostrar imagen
titles = ['Imagen original', 'Sal y pimienta','Ruido Gauseano']
images = [img, ruidoSP, processed_image]

plt.figure(figsize = (20, 15))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

ruidoSP = cv2.cvtColor(ruidoSP, cv2.COLOR_BGR2RGB)
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fil2D = cv2.cvtColor(fil2D, cv2.COLOR_BGR2RGB)
cv2.imwrite("Resultado.jpg",np.hstack([img, ruidoSP, fil2D]))

cv2.imshow("ORIGINAL, RUIDO, ELIMINACION DE RUIDO", np.hstack([img, ruidoSP, fil2D]))
cv2.waitKey();
