"""
2 de los métodos, más usados, de conversión de espacios de color son:
+ RGB <-> Gris
+ RGB <-> HSV
"""

# Se usa:
#   cv2.cvtColor(input_image, flag) donde flag determina el tipo de conversión.

"""
Para la conversión de RGB -> Gris usamos los indicadores cv2.COLOR_BGR2GRAY.
De forma similar para RGB -> HSV. Usamos el indicador cv2.COLOR_BGR2HSV.
Para obtener otros indicadores, sólo ejecuta los siguientes comandos
en tu terminal Python:
"""

import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

"""
Para HSV, el rango de tonos es [0,179], el rango de saturación es [0,255]
y el rango de valor es [0,255]
"""
