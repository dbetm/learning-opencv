import numpy as np
import cv2
# img: La imagen donde se desea dibujar la forma geométrica
# thickness: Grosor de la línea, círculo, etc.
# color: Colores BGR, ejemplo, azul (255, 0, 0). Para grises solo un escalar

# Crear una imagen en negro
# imagen de 512 x 512
img = np.zeros((512, 512, 3), np.uint8)

# Dibuja una línea horizontal verde con un grosor de 4px
img = cv2.line(img, (0, 255), (511, 255), (0, 255, 0), 4)

# Dibujando un rectángulo
# Coordenadas de la esquina superior izquierda y esquina inferior derecha
img = cv2.rectangle(img, (210, 360), (300, 500), (255, 0, 0), 3)

# Dibujando un círculo
# Coordenada del centro, radio, color y thickness (-1 rellena la figura)
img = cv2.circle(img, (256, 256), 100, (0, 0, 255), -1)

# Dibujando una elipse
# coordenadas del centro, longitud del eje mayor y menor, + ángulo de rotación (antihorario)
# startAngle y endAngle indican el arco inicial y final, medidos en dir horaria
# respecto al eje mayor
img = cv2.ellipse(img, (255, 105), (100, 50), 0, 0, 180, (255, 0, 0), -1)

# Dibujando un polígono (triángulo amarillo)
""" Para dibujar un polígono es necesario especificar las coordenadas de los
vértices. Construye las coordenadas en un arreglo de dimensiones ROWSx1x2,
donde ROWS es el número de vértices y debe ser de tipo int32.
"""
pts = np.array([[180, 120], [330, 120], [255, 140]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

""" Si el tercer argumento en cv2.polylines es False, entonces se obtendrá
una línea poligonal abierta.
"""
# cv2.polylines se puede utilizar para dibujar varias líneas.

# Aregando texto a las imágenes
# Coordenada: Esquina inferior izquierda
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'David', (40, 90), font, 3, (255, 255, 255), 2, cv2.LINE_AA)

# Mostrar la imagen
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
