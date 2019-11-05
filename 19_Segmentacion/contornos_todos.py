import cv2
import numpy as np

image = cv2.imread("../src/img/8/donut.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

# Escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Encontrar bordes con Canny
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

# Encontrando los contornos
# La siguiente función altera la imagen que se pasa por parámetro
contours, hierachy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.imshow("Canny Edges After Contouring", edged)
cv2.waitKey(0)

print("El número de contornos es: " + str(len(contours)))

# Dibujar todos los contornos
# Usar -1 en el tercer parámetro para dibujarlos todos
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

cv2.imshow('Contornos', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
