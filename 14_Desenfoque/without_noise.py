import cv2
import numpy as np

image = cv2.imread("../src/img/9/girasol.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

"""
Parámetros, después de None son - la fuerza del filtro 'h' (5-10 buen rango)
Siguiente es, hForColorComponent, fija los mismo que el valor h de nuevo
"""

dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)
cv2.imshow("Fast Means Denoising", dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
