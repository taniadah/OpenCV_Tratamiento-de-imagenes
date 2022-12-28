import cv2

def centroM(name):
    img = cv2.imread(name) # lee la imagen
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convierte la imagen a escala de grises
    ret, thresh1 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV +  cv2.THRESH_OTSU)
    edges = cv2.Canny(img,10,150)
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_BGR2RGB)
    ret,thresh = cv2.threshold(gray,120,255,0)
    M = cv2.moments(thresh)
    cX = 0
    cY = 0

    if M["m00"]!=0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    return cX, cY


img = cv2.imread("poligonos.png")
bn = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(bn, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
c,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

tabla = []

for i in c:
    e = 0.01 * cv2.arcLength(i, True)
    ap = cv2.approxPolyDP(i, e, True)
    x,y,w,h = cv2.boundingRect(ap)

    if len(ap)==3:
        cv2.putText(img,"Triangulo", (x,y-5),1, 1,(0, 255,0),1)
        fig = "Triangulo.png"
    elif len(ap)==4:
        aspect_ratio = float(w)/h
        if aspect_ratio == 1:
            cv2.putText(img, "Cuadrado", (x,y-5),1, 1,(0, 255,0),1)
            fig = "Cuadrado.png"

        else:
            cv2.putText(img, "Rectangulo", (x,y-5),1, 1,(0, 255,0),1)
            fig = "Rectangulo.png"

    elif len(ap)==5:
        cv2.putText(img, "Pentagono", (x,y-5),1, 1,(0, 255,0),1)
        fig = "Pentagono.png"

    elif len(ap) == 6:
        cv2.putText(img, "Hexagono", (x,y-5),1, 1,(0, 255,0),1)
        fig = "Hexagono.png"

    elif len(ap)>10:
        cv2.putText(img, "Circulo", (x,y-5),1, 1,(0, 255,0),1)
        fig = "Circulo.png"

    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite(fig,crop_img)

    cX, cY = centroM(fig)
    cv2.circle(img, (x+cX, y+cY), 2, (0, 0, 255), -1)

    tabla.append(["Número de lados",len(ap)])
    tabla.append(["posición del centro (x,y)", cX])
    tabla.append(["xMínima", x])
    tabla.append(["y Máxima", y+w])
    tabla.append(["y Mínima", y])
    tabla.append(["Tamaño en pixeles", h*w])

    print(tabla)

    tabla = [[]]
    cv2.drawContours(img, [ap],0 ,[0,255,0],2)
    cv2.imshow("imagen",img)
    cv2.waitKey(0)


cv2.imshow("imagen", img)
cv2.waitKey(0)
