import cv2
import numpy as np

# Cargar la imagen como escala de grises
image = cv2.imread("../src/img/16/sinergia.png", 0)
cv2.imshow("Original", image)
cv2.waitKey(0)

# Valores menores a 127 serán 0, arriba serán 255
ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold binary", thresh1)
cv2.waitKey(0)

# Es buena práctica hacer desenfoque así para remover el ruido
image = cv2.GaussianBlur(image, (3,3), 0)

# Usar umbralización adaptativa
# cv2.adaptiveThreshold(img, max value, adaptive type, threshold type,
#    block_size, constant that's substracted from mean)
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 3, 5)
cv2.imshow("Adaptive Mean Thresholding", thresh)
cv2.waitKey(0)

_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding", th2)
cv2.waitKey(0)

# Umbralización con Otsu usando filtrado Gaussiano
blur = cv2.GaussianBlur(image, (5,5), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Gaussian Otsu's Thresholding", thresh)
cv2.waitKey(0)
