# Tranformación afín

"""
En una transformación afín todas las líneas paralelas en la imagen original
seguirán siendo paralelas en la imagen de salida. Para encontrar la matriz
de transformación, necesitamos tres puntos de la imagen de entrada y sus
ubicaciones correspondientes en la imagen de salida.
Luego cv2.getAffineTransform creará una matriz 2×3 que se pasará a cv2.warpAffine.
"""

import numpy as np
import matplotlib.pyplot as plt # carga la librería para graficar
import cv2

img = cv2.imread("../src/img/9/girasol.jpg", -1)
rows, cols, channels = img.shape

# definimos los puntos de entrada
pts1 = np.float32([[100, 400], [400, 100], [100, 100]])
# ahora los de salida
pts2 = np.float32([[50, 300], [400, 200], [80, 150]])

M = cv2.getAffineTransform(pts1, pts2)
res = cv2.warpAffine(img, M, (cols, rows))
# Mostramos las fotos
plt.subplot(121), plt.imshow(img), plt.title("Entrada")
plt.subplot(122), plt.imshow(res), plt.title("Salida")
plt.show()

cv2.imshow("Res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
