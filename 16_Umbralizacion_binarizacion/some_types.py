import cv2
import numpy as np

# Cargar la imagen como escala de grises
image = cv2.imread("../src/img/16/astronauta.png", 0)
cv2.imshow("Original", image)

# Valores menores a 127 serán 0, arriba serán 255
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("1) Threshold binary", thresh1)

# Valores menores a 127 serán 255, arriba serán 0
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("2) Threshold binary inverse", thresh2)

# Valores arriba de 127 son truncados (el arg 255 es ignorado)
ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("3) Threshold trunc", thresh3)

# Valores menores a 127 serán 0, arriba serán sin cambio
ret, thresh4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("4) Threshold to zero", thresh4)

# Valores menores a 127 serán sin cambio, arriba serán 0
ret, thresh5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("5) Threshold to zero inv", thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()
