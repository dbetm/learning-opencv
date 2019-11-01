import cv2
import numpy as np

image = cv2.imread("../src/img/9/girasol.jpg")

# El kernel necesita ser de tamaño impar y positivo
blur = cv2.blur(image, (3,3))
cv2.imshow('Promedio', blur)
cv2.waitKey(0)

# En lugar de un filtro cuadrado, usa un filtro Gaussiano
gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow("Desenfoque Gaussiano", gaussian)
cv2.waitKey(0)

# Toma la mediana de todos los elementos del píxel bajo el área
# del kernel y el elemento central lo remplaza por la mediana
median = cv2.medianBlur(image, 5)
cv2.imshow("Desenfoque por mediana", median)
cv2.waitKey(0)

# Bilateral es muy efectivo para remover el ruido sin afectar bordes
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Desenfoque bilateral', bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()
