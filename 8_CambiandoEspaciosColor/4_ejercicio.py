import cv2
import numpy as np

imagen = cv2.imread("../src/img/8/cieloEstrellado.jpg")

"""
For HSV, Hue range is [0,179], Saturation range is [0,255] and Value
range is [0,255]. Different software use different scales. So if you are
comparing OpenCV values with them, you need to normalize these ranges.
"""

# Convertir BGR a HSV_BGR2HSV)
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# RGB stands for Red Green Blue.
# BGR is the same, except the order of areas is reversed.

# Definir el rango del blanco in HSV
lower_white = np.array([0, 0, 220])
upper_white = np.array([255, 35, 255])

# Obtener solo los colores blancos
mask = cv2.inRange(hsv, lower_white, upper_white)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(imagen, imagen, mask= mask)
cv2.imshow("Original", imagen)
cv2.imshow("Máscara", mask)
cv2.imshow("Solo estrellas", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
