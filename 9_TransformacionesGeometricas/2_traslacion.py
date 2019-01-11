"""
Una traslación es el desplazamiento de la posición de un objeto. Si se conoce
la magnitud del desplazamiento (t_x,t_y) en las direcciones x e y,
respectivamente,  se puede escribir la matriz de transformación M como:
    | 1| 0|tx|
M = |--|--|--|
    |0 | 1|ty|
"""

import numpy as np
import cv2

img = cv2.imread("../src/img/9/medusa.jpg", 0)
# se obtienen las dimensiones
rows, cols = img.shape
# la trasladamos 30 en x & 60 en y
M = np.float32([[1, 0, 30], [0, 1, 60]])

res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Resultado", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
