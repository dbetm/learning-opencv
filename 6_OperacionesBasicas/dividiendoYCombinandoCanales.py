import numpy as np
import cv2

img = cv2.imread("../src/img/6/nocheEstrellada.jpg")

# Se dividen los canales de una imagen en sus planos individuales
b, g, r = cv2.split(img)
# Luego, es posible fusionar para volver a tener la imagen
img = cv2.merge((b,g,r))

# Otra forma de obtener el canal azul
b = img[:, :, 0]
print(b[:])

# Ahora seleccionaremos el canal rojo y le ponemos el valor 0
# Indexación de Numpy es mejor que usar split (en cuanto eficiencia)
img[:, :, 2] = 0

# Mostramos la imagen
cv2.namedWindow("Imagen", cv2.WINDOW_NORMAL)
cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
