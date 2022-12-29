import cv2
import numpy as np
import matplotlib.pyplot as plt

def plano(img, c1, c2):
    al, an = img.shape[0:2]
    auxImg = np.zeros((al,an,3),np.uint8)

    for i in range(al):
        for j in range(an):
            c11 = img.item(i,j, c1)
            c22 = img.item(i, j, c2)
            auxImg.itemset((i,j, c1), c11)
            auxImg.itemset((i,j, c2), c22)

    return auxImg

def rgb(img, c1):
    al, an = img.shape[0:2]
    auxImg = np.zeros((al,an,3),np.uint8)

    for i in range(al):
        for j in range(an):
            c11 = img.item(i,j,c1)
            auxImg.itemset((i,j,c1), c11)

    return auxImg

def rgbTohsv(img):
    al, an = img.shape[0:2]
    auxImg = np.zeros((al,an,3),np.uint8)
    matriz = np.zeros((al*an,3))
    cont = 0
    for i in range(al):
        for j in range(an):
            r = img.item(i,j,0)
            g = img.item(i,j,1)
            b = img.item(i,j,2)

            r = r/255
            g = g/255
            b = b/255

            rgb = [r,g,b]
            cmax = max(rgb)
            cmin = min(rgb)
            delta = cmax - cmin

            if delta==0:
                h=0
            elif cmax == r and delta!=0:
                h = round(60*(((g-b)/delta)%6))
            elif cmax== g and delta!=0:
                h = round(60*(((b-r)/delta)+2))
            elif cmax == b  and delta!=0:
                h = round(60*(((r-g)/delta)+4))

            if cmax==0:
                s=0
            else:
                s = delta/cmax;
            v = cmax

            matriz[cont] = [h,s,v]
            cont+=1
    return matriz

def hsvTorgb(mat, img):
    al, an = img.shape[0:2]
    auxImg = np.zeros((al,an,3),np.uint8)
    cont = 0
    rp = 0
    gp=0
    bp=0
    for i in range(al):
        for j in range(an):
            e = mat[cont]
            c = e[2]*e[1]
            x = c*(1-abs((e[0]/60)%2 - 1))
            m = e[2] - c
            if e[0]>=0 and e[0] < 60:
                rp = c
                gp = x
                ap = 0
            elif e[0]>=60 and e[0] <120:
                rp = x
                gp = c
                bp = 0
            elif e[0]>=120 and e[0]<180:
                rp = 0
                gp = c
                bp = x
            elif e[0]>=180 and e[0]<240:
                rp = 0
                gp = x
                bp = c
            elif e[0]>=240 and e[0]<300:
                rp = x
                gp = 0
                bp = c
            elif e[0]>=300 and e[0]<360:
                rp = c
                gp = 0
                bp = x
            r = round((rp + m)*255)
            g = round((gp + m)*255)
            b = round((bp + m)*255)

            auxImg[i,j] = [r,g,b]

            cont+=1
    return auxImg

nombre = input("Ingresa el nombre de la imagen: ")
imagen = plt.imread(nombre)
ima2 = cv2.imread(nombre)
hsv = cv2.cvtColor(ima2, cv2.COLOR_BGR2HSV)



planoAm = plano(imagen, 0,1)
planoCian = plano(imagen, 2, 1)
planoMag = plano(imagen,0,2)

planoR = rgb(planoAm, 0)
planoV = rgb(planoCian, 1)
planoA = rgb(planoMag, 2)

matHSV = rgbTohsv(imagen)
hsvAbgr = hsvTorgb(matHSV, imagen)


titles = ['Plano Amarillo', 'Plano Cian','Plano Magenta']
images = [planoAm, planoCian, planoMag]
plt.figure(figsize = (20, 15))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

titles = ['Plano Rojo', 'Plano Verde','Plano Azul']
images = [planoR, planoV, planoA]
plt.figure(figsize = (20, 15))

for i in range(3):
    print(i)
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

plt.figure("HSV to BGR")
plt.imshow(hsvAbgr)
plt.show()


print("Original")
print(imagen)

#print(matHSV)

cv2.imshow("Original",ima2)
cv2.imshow("hsv", hsv)
cv2.waitKey()
cv2.destroyAllWindows()
