"""
La rotación de una imagen, en un cierto ángulo θ, se logra  aplicando
la siguiente matriz de transformación:
    | cos(0)|-sin(0)|
M = |-------|-------|
    | sin(0)| cos(0)|
Sin embargo, OpenCV permite además personalizar más la rotación multiplacando
por un factor de escala.
Por otra parte, también permite cambiar el centro de rotación.
Considerar estas 2 últimas opciones modifica la matrix de traslación.
"""

# Ejemplo donde se rota una imagen con respeco al centro sin aplicar
# ningún factor de escala

import numpy as np
import cv2

img = cv2.imread("../src/img/9/medusa.jpg", 0)
# se obtienen las dimensiones
rows, cols = img.shape
# con (cols/2, rows/2) se obtiene el centro, luego el ángulo, y me
# imagino que el factor de escala
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
res = cv2.warpAffine(img, M, dsize=(cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Resultado", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
