import cv2
import numpy as np

image = cv2.imread("../src/img/9/medusa.jpg")
cv2.imshow("Original", image)
cv2.waitKey(0)

# Creamos un kernel de 5x5
kernel_5x5 = np.ones((3,3), np.float32) / 9 # sobre 9 para normalizar

# Hacemos la convolución
blurred = cv2.filter2D(image, -1, kernel_5x5)
cv2.imshow("5x5 Kernel blurring", blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()
