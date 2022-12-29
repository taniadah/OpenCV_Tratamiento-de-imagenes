import numpy as np
import cv2
import matplotlib.pyplot as plt
import math as m



def espejo(imagen):
    cont = 0
    alto, ancho = img.shape[0:2]
    imagenAu = np.copy(imagen)
    #recorrer la imagen y obtener sus intensidades
    for i in range(alto):
        for j in range(ancho):
            b = imagen.item(i, j, 0)
            g = imagen.item(i, j, 1)
            r = imagen.item(i, j, 2)

            #va a intercambar los pixeles empezando de derecha a la izquiera en la nueva imagen
            imagenAu.itemset((i, ancho-j-1, 0), b)
            imagenAu.itemset((i, ancho-j-1, 1), g)
            imagenAu.itemset((i, ancho-j-1, 2), r)

    return imagenAu


def barrido(al, an, grados):
    sen = m.sin(grados)
    cose = m.cos(grados)
    pan= an-1
    pal =al-1

#para el recorrimientod e pixeles sacamos los nuevos puntos de las esquinas de la imagen, tendremos 4 cordenadas en total pN representa los valores para lo ancho y pNN para los valores a lo alto
    p1 = int( -(an/2)*cose +(al/2)*sen+(an/2))
    p11 = int(-(an/2)*sen-(al/2)*cose+(al/2))
    p2 =  int(- pal*sen -(an/2)*cose +(al/2)*sen+(an/2))
    p22 =  int(pal*cose -(an/2)*sen-(al/2)*cose+(al/2))
    p3 =  int(pan * cose  -(an/2)*cose +(al/2)*sen+(an/2))
    p33 =  int(pan * sen -(an/2)*sen-(al/2)*cose+(al/2))
    p4 = int(pan * cose - pal*sen -(an/2)*cose +(al/2)*sen+(an/2))
    p44 = int(pan * sen + pal*cose -(an/2)*sen-(al/2)*cose+(al/2))

#imprime los punto obtenidos
    print("p1", p1, "p11", p11, "p2", p2, "p22", p22, "p3", p3 , "p33", p3,"p4", p4, "p44", p44)

    x = 0;
    y = 0

#comparamos si los valores son menores a 0 para obtener los valores de x y y en este caso se tomara en cuenta el menor
    if p1<x:
        x = p1
    if p2<x:
        x = p2
    if p3<x:
        x = p3
    if p4<x:
        x = p4
    if p11<y:
        y = p11
    if p22<y:
        y = p22
    if p33<y:
        y = p33
    if p44<y:
        y = p44

#se multiplica por -1 para obtener un valor positivo
    x = (-1)*x
    y = (-1)*y
#se imprime el nuevo valor de las 4 esquinas en este caso ya no sale ningun negativo
    print("p1", p1+x, "p11", p11+y, "p2", p2+x, "p22", p22+y, "p3", p3+x , "p33", p33+y,"p4", p4+x, "p44", p44+y)

    #funcion que define ahora que dimensiones tendra a imagen resultado
    d1, d2 = defineDim(p1+x, p11+y, p2+x, p22+y, p3+x, p33+y, p4+x, p44+y)

    print("x :", x ,"y",y)
    return x, y, d1, d2

def defineDim(p1, p11, p2, p22, p3, p33, p4,p44):
    #para esta funcion se comparan las nuevas dimensiones obtenidas en la anterior funcion donde se obtiene ahora el menor y mayor valor para x e y
    dimX = 0
    dimY = 0
    if p1>dimX:
        dimX = p1
    if p2>dimX:
        dimX = p2
    if p3>dimX:
        dimX = p3
    if p4>dimX:
        dimX = p4
    if p11>dimY:
        dimY = p11
    if p22>dimY:
        dimY = p22
    if p33>dimY:
        dimY = p33
    if p44>dimY:
        dimY = p44
    return dimX, dimY

#es para rotar la imagen, recibe imagen y grados a rotar
def rotacion(imagen, grados):
    #se trabaja con esa funcion radians de lo contrario se rota pero no al angulo que se quiere
    al,an = imagen.shape[0:2]
    grados = m.radians(grados)
    #se define el seno y coseno
    sen = m.sin(grados)
    cose = m.cos(grados)

    #la funcion de abrrido es solo para recorrer la imagen en caso de que salga un numero negativo por ejemplo si da -131 en y entonces para cada pixel en la imagen rotada recorreremos esos 131 a lo ancho para que aparezca toda la imagen, lo mismo para y
    rx,ry, dx, dy =barrido(al, an, grados)

    # en la funcion barrido se hace uso de otra funcion para obtener las dimensiones de nuestra nueva imagen en donde dx corresponde a la dimension de lo ancho y dy de lo alto y se crea una matriz en ceros
    bgr = np.zeros((dy+1,dx+1,3),np.uint8)
    auxImg = bgr

    #se recorre la imagen y co la matriz de trasformacion ( de senos y cosenos consultada en: https://www.nibcode.com/es/blog/1137/algebra-lineal-y-el-procesamiento-digital-de-imagenes-parte-iii-transformaciones-afines#:~:text=Si%20queremos%20rotar%20la%20imagen,nuevamente%20a%20su%20posici%C3%B3n%20original  donde se traslada la imagen para girarla desde el centro y despues se vuelve a trasladar) cabe mencionar que aui ya esta resuleta la matriz para x e y solo igualamos los resultados

    for i in range(an):
        for j in range(al):
            x = i * cose - j*sen -(an/2)*cose +(al/2)*sen+(an/2)
            y = i * sen + j*cose -(an/2)*sen-(al/2)*cose+(al/2)
            x = int(x)
            y= int(y)
            if (x<dx and y<dy):
                b = img.item(j, i, 0)
                g = img.item(j, i, 1)
                r = img.item(j, i, 2)
                auxImg.itemset((y+ry,x+rx,0),b)
                auxImg.itemset((y+ry,x+rx,1),g)
                auxImg.itemset((y+ry,x+rx,2),r)
    return auxImg


imagen = input("Ingresa el nombre de la imagen: ")
img = plt.imread(imagen)

grad = int(input("Ingresa cuantos grados la deseas rotar: "))

print( img.shape )
print( img.size )
alto, ancho = img.shape[0:2]

rotar = rotacion(img, grad)

imgMirror = espejo(img)

plt.figure("Mirror")
plt.imshow(imgMirror)

plt.figure("Original")
plt.imshow(img)

plt.figure("Rotado")
plt.imshow(rotar)
plt.show()
