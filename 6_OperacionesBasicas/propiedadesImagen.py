import numpy as np
import cv2

# Primero se carga la imagen
img = cv2.imread("../src/img/6/nocheEstrellada.jpg")
# La imagen cargada es de 2000 x 1333 px

# Las propiedades de imagen incluyen número de filas, columnas y canales,
# tipo de data de imagen, número de píxeles, etc.

print(img.shape) # tupla -> (# filas, # columnas, # de canales)

print("Total de pixeles: " + str(img.size))
print("El tipo de datos es: " + str(img.dtype))
