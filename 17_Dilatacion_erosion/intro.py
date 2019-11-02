import numpy as np
import cv2

image = cv2.imread("../src/img/17/quote.jpg", 0)
cv2.imshow("Original", image)
cv2.waitKey(0)

# Se define el tamaño del kernel
kernel = np.ones((7,7), np.uint8)

# Erosión
erosion = cv2.erode(image, kernel, iterations = 1)
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)

# Dilatación
dilatacion = cv2.dilate(image, kernel, iterations = 1)
cv2.imshow("Dilatacion", dilatacion)
cv2.waitKey(0)

# Opening (erosión -> dilatación)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.waitKey(0)

# Closing (dilatación -> erosión)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
