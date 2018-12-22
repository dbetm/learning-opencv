import numpy as np
import cv2

# Primero se carga la imagen
img = cv2.imread("../src/img/6/nocheEstrellada.jpg")
# La imagen cargada es de 2000 x 1333 px

# Se puede acceder al valor de un pixel con la coordenada
# Imágenes RGB regresan una gama de colores, en grises solo la intensidad
px = img[100, 100]
print(px)

# Obtener el valor del azul
bluePx = img[100, 100, 0]
print(bluePx)

# Ahora modificamos un pixel
img[101, 101] = [255, 255, 255] # blanco
print(img[101, 101])

# Un mejor método para acceder al pixel y editarlo
# Accesing RED value
redPx = img.item(10, 10, 2) # el dos porque queremos el rojo
print(redPx)

# Modifying RED value
img.itemset((10, 10, 2), 100)
redPx = img.item(10, 10, 2)
print(redPx)

cv2.namedWindow("Imagen cargada", cv2.WINDOW_NORMAL)
cv2.imshow("Imagen cargada", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
