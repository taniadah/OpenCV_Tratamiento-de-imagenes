import numpy as np
import matplotlib.pyplot as plt
import cv2


def segColRoj(img):
    al, an = img.shape[0:2]
    seg = np.zeros(img.shape,np.uint8)
    for i in range(al):
        for j in range(an):
            if img.item(i,j,1)>1:
                seg[i,j] = [255,255,255]
            else:
                seg[i,j] = [0,0,0]

    return seg

def colB(imgS, imagenBN, imgNormal):
    al, an = imgS.shape[0:2]
    aux = np.zeros(imgS.shape,np.uint8)
    for i in range(al):
        for j in range(an):
            if imgS.item(i,j,1) == 255:
                aux[i,j] = imagenBN[i,j]
                #print("si", aux[i,j])
            else:
                aux[i,j] = imgNormal[i,j]


    return aux

def blancoNegro(imagen):
    al, an = imagen.shape[0:2]
    bgr = np.zeros((al,an,3),np.uint8)
    auxImg = bgr
    for i in range(al):
        for j in range(an):
            b = imagen.item(i,j, 2)
            g = imagen.item(i,j, 1)
            r = imagen.item(i,j, 0)
            prom = int((b+g+r)/3)
            auxImg.itemset((i,j, 0), prom)
            auxImg.itemset((i,j, 1), prom)
            auxImg.itemset((i,j, 2), prom)
    return auxImg


imagen = plt.imread("flowers.jpg")
print(imagen.shape)

segm = segColRoj(imagen)

imagenBN = blancoNegro(imagen)

color = colB(segm, imagenBN, imagen)


plt.figure("normal")
plt.imshow(imagen)

plt.figure("seg")
plt.imshow(segm)

plt.figure("COL")
plt.imshow(color)
plt.show()
