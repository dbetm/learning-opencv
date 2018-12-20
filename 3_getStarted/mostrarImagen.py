import numpy as np
import cv2

# cv2.IMREAD_COLOR: carga una imagen de color. Cualquier transparencia de la imagen será ignorada. Es el indicador (o bandera) predeterminado. -> 1
# cv2.IMREAD_GRAYSCALE: carga la imagen en modo de escala de grises -> 0
# cv2.IMREAD_UNCHANGED: carga la imagen como sin alteraciones incluyendo el canal alfa -> -1

# Load an color image in grayscale
img = cv2.imread("../src/img/3/ninja.png", 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

# Función con enlace al teclado
cv2.waitKey(0)
# Para cerrar las ventans
# cv2.destroyAllWindows()

"""
Hay un caso especial en que puedes crear una ventana y cargar la imagen posteriormente. En ese caso, puedes especificar si la ventana es redimensionable o no. Esto se realiza con la función cv2.namedWindow(). Por defecto, el indicador (o bandera) es cv2.WINDOW_AUTOSIZE. Pero si se especifica la que el indicador sea  cv2.WINDOW_NORMAL, puedes cambiar el tamaño de la ventana. Esto será útil cuando las dimensiones de la imagen sean muy grandes y se añada una barra de seguimiento (o un scroll).
"""

# Guardando la imagen
cv2.imwrite('../src/img/3/ninja-gray.png', img)
