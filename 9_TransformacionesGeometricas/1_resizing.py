import numpy as np
import cv2
# métodos disponibles con cv2.resize():
"""
La función usa diferentes métodos de interpolación, siendo los más usados:
cv2.INTER_AREA, para contraer la imagen y cv2.INTER_CUBIC (suave) &
cv2.INTER_LINEAR, para acercar la imagen. El método de interpolación
utilizado por defecto es cv2.INTER_LINEAR.
"""

img = cv2.imread("../src/img/9/medusa.jpg")

# Indicando el factor de escala
res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

# Indicando manualmente el tamaño
height, width = img.shape[:2]
res2 = cv2.resize(img, (int(0.5*width), 120), interpolation = cv2.INTER_CUBIC)
# Mostramos la original y la manipulada
cv2.imshow("Original", img)
cv2.imshow("Redimensionada", res)
cv2.imshow("Redimensionada 2", res2)

cv2.waitKey(0)
cv2.destroyAllWindows()
