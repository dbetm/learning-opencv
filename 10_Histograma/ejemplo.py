import cv2
import numpy as np

# Necesitamos importar matplotlib para crear
# nuestros histogramas gráficos
from matplotlib import pyplot as plt

image = cv2.imread('../src/img/9/girasol.jpg')
cv2.imshow("Entrada", image)

histogram = cv2.calcHist([image], [0], None, [256], [0,256])
"""
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
"""

# Graficamos el histograma , ravel() flatens our image array
plt.hist(image.ravel(), 256, [0,256])
plt.show()

# Enumeración que nos sirva para ver los canales de colores separados
color = ('b', 'g', 'r')

# Separamos los colores y graficamos cada uno en el histograma
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(histogram2, color=col)
    plt.xlim([0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
