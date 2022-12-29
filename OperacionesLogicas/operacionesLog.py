import numpy as np
import  matplotlib.pyplot as plt
import cv2

def corte(img, alto, ancho):
    cor = img[0:alto, 0:ancho]
    return cor
def verificar(med1, med2):
    if med1== med2:
        med = med1
    elif med1> med2:
        med = med2
    elif med2 > med1:
        med = med1
    return med

def mostrar(imagen, nombre):
    rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)
    plt.title(nombre)
    plt.axis("off")
    plt.show()

def plotear(figura, sp, nombre, imagen):
    plt.figure(figura)
    plt.subplot(sp)
    plt.title(nombre)
    plt.imshow(imagen)


a = input("Ingrese imagen 1: ")
b = input("Ingrese imagen 2:")
imagen1 = cv2.imread(a)
imagen2 = cv2.imread(b)

print(imagen1.shape)
print(imagen2.shape)

al1, an1, c1 = imagen1.shape
al2, an2, c2 = imagen2.shape

if c1 != c2:
    print("La imagenes no tienen los mismos canales")
else:
    x = verificar(an1, an2)
    y = verificar(al1, al2)
    img1 = corte(imagen1, y, x)
    img2 = corte(imagen2, y, x)

bw_and = cv2.bitwise_and(img1, img2)
bw_or = cv2.bitwise_or(img1, img2)
bw_xor = cv2.bitwise_xor(img1, img2)
bw_not = cv2.bitwise_not(imagen1)
bw_not2 = cv2.bitwise_not(imagen2)

rgb1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)
rgb2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB)
rgb_and = cv2.cvtColor(bw_and, cv2.COLOR_BGR2RGB)
rgb_or = cv2.cvtColor(bw_or, cv2.COLOR_BGR2RGB)
rgb_xor = cv2.cvtColor(bw_xor, cv2.COLOR_BGR2RGB)
rgb_not1 = cv2.cvtColor(bw_not, cv2.COLOR_BGR2RGB)
rgb_not2 = cv2.cvtColor(bw_not2, cv2.COLOR_BGR2RGB)

plotear(1, 241, "Imagen1", rgb1)
plotear(1, 242, "Imagen2", rgb2)
plotear(1, 243, "AND", rgb_and)
plotear(1, 244, "OR", rgb_or)
plotear(1, 245, "XOR", rgb_xor)
plotear(1, 246, "not1", rgb_not1)
plotear(1, 247, "not2", rgb_not2)

plt.show()
