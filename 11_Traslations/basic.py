import cv2
import numpy as np

image = cv2.imread('../src/img/9/girasol.jpg')
# Guardar la altura y ancho de la imagen
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

#    | 1 0 Tx |
# T= | 0 1 Ty |

# T es nuestra matriz de traslación
T =  np.float32([[1,0,quarter_width], [0, 1, quarter_height]])

# Usamos warpAffine para transformar la imagen usando la matriz T
img_traslation = cv2.warpAffine(image, T, (width, height))
cv2.imshow('Translation', img_traslation)
cv2.waitKey()
cv2.destroyAllWindows()
