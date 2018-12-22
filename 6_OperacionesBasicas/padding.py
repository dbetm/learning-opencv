""" HACIENDO BORDES PARA LA IMAGEN
cv2.copyMakeBorder toma los siguientes argumentos:
    + src - introducir la imagen
    + top, bottom, left, right – ancho de borde en número de píxeles en
correspondencia con las direcciones.
    + borderType:
        - BORDER_CONSTANT
        - BORDER_REFLECT
        - BORDER_REFLECT_101 o cv2.BORDER_DEFAULT
        - BORDER_REPLICATE
        - BORDER_WRAP
    + valor (si el tipo es cv2.BORDER_CONSTANT)
"""
import numpy as np
import cv2
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]
img = cv2.imread("../src/img/6/opencv_logo.png")
replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
plt.subplot(231), plt.imshow(img, 'gray'), plt.title('Original')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('Replicate')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('Reflect')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('Reflect101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('Wrap')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('Constant')
plt.show()
