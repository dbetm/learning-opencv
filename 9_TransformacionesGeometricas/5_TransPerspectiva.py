"""
Para realizar una transformación de perspectiva es necesario especificar una
matriz de 3×3. Luego de aplicar este tipo de transformación, las líneas
rectas permanecerán rectas.

Para generar la matriz de 3×3 es necesario  indicar cuatro puntos sobre la
imagen de inicial y los correspondientes  puntos sobre la imagen resultante.

Tres de los cuatro puntos, tienen que ser no-colineales (no se unen con una recta).
De esta manera la matriz de transformación puede ser generada utilizando la función
cv2.getPerspectiveTransform. Luego, para aplicar la transformación, se utiliza
cv2.warpPerspective teniendo en cuenta la matriz de 3×3 generada con la
función anterior.
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("../src/img/9/girasol.jpg")
rows, cols, ch = img.shape

pts1 = np.float32([[56, 56], [780, 56], [56, 550], [780, 550]])
pts2 = np.float32([[90, 178], [320, 190], [5, 590], [750, 580]])

M = cv2.getPerspectiveTransform(pts1, pts2)
res = cv2.warpPerspective(img, M, (rows, cols))

# Mostramos las fotos
plt.subplot(121), plt.imshow(img), plt.title("Entrada")
plt.subplot(122), plt.imshow(res), plt.title("Salida")
plt.show()
