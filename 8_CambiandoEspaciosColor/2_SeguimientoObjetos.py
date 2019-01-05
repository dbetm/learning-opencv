# Se va a extraer un objeto de color

# En HSV es más fácil representar un color que en RGB

# El método es el siguiente (extraer objeto color azul):
"""
+ Tomar cada fotograma del video
+ Conviértelo de RGB a HSV
+ Limitamos la imagen en HSV a un rango azul
+ Ahora se extra el objeto azul únicamente.
"""
import cv2
import numpy as np

image = cv2.imread("../src/img/8/nadal.jpg")

# Convertir BGR a HSV_BGR2HSV)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define el rango de colores
lower_verde = np.array([25, 50, 50])
upper_verde = np.array([67, 255, 255])
lower_rosa1 = np.array([125, 50, 50])
upper_rosa1 = np.array([167, 255, 255])

# Umbral de la imagen HSV para obtener solo los colores deseados
mask = cv2.inRange(hsv, lower_verde, upper_verde)
mask1 = cv2.inRange(hsv, lower_rosa1, upper_rosa1)

# Bitwise-AND mask and origin image
bola = cv2.bitwise_and(image, image, mask= mask)
camiseta = cv2.bitwise_and(image, image, mask= mask1)

cv2.imshow('frame', image)
# cv2.imshow('mask', mask)
cv2.imshow('Bola', bola)
cv2.imshow('Camiseta', camiseta)

cv2.waitKey(0)

cv2.destroyAllWindows()
