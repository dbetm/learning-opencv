import cv2
import numpy as np

image = cv2.imread("../src/img/9/girasol.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

# Crear el kernel para agudizar, no se normaliza dado que la suma
# de los valores del kernel ya suman 1
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])
# Aplicando la diferencia de núcleos en la imagen de entrada
sharpened = cv2.filter2D(image, -1, kernel_sharpening)

cv2.imshow("Agudizada", sharpened)
cv2.waitKey(0)


cv2.destroyAllWindows()
