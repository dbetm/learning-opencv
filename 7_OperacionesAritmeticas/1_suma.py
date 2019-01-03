"""
Puedes sumar 2 imágenes usando cv2.add() - OpenCV o res = img1 + img2 - Numpy
Ambas imágenes deben tener la misma profundidad y tipo, o la segunda puede
ser un valor escalar.
"""

import numpy as np
import cv2

# suma con OpenCV, operación saturada
# suma con Numpy, operación modular
# EJEMPLO

x = np.uint([250])
y = np.uint([10])

print(cv2.add(x,y)) # 250 + 10 = 260 => 255
print(x+y) # 250 + 10 = 260 % 256 = 4
print("\n")
# NOTA: Al correrlo ambos dan 260

# Con imágenes
img1 = cv2.imread('../src/img/7/sol.jpeg')
img2 = cv2.imread('../src/img/7/sol.jpeg')
img3 = cv2.add(img1, img2)
img4 = img1 + img2

cv2.imshow('OpenCV', img3)
cv2.imshow("Numpy", img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
