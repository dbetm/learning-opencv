import cv2
import numpy as np

image = cv2.imread("../src/img/18/catrina.jpg", 0)
cv2.imshow("Original", image)
cv2.waitKey(0)

height, width = image.shape

# Extraer bordes con Sobel
sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=9)
cv2.imshow("Sobel x", sobel_x)
cv2.waitKey(0)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=9)
cv2.imshow("Sobel Y", sobel_y)
cv2.waitKey(0)

# Hacemos or de ambos sobel
sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow("Sobel OR", sobel_OR)
cv2.waitKey(0)

# Laplaciano
laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow("Laplacian", laplacian)
cv2.waitKey(0)

# La detección de bordes con el algorito de Canny usa valores de gradiente
# como umbrales

""" Necesitamos darle dos valores de umbrales, th1 y th2. Cualquier gradiente
con un valor más grande que th2 es considerado un borde, abajo de th1 no es
gradiente, los valores intermedios dependen si sus intensidades están
conectadas.
"""

canny = cv2.Canny(image, 100, 255)
cv2.imshow("Canny", canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
