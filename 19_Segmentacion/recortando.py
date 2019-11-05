import cv2
import numpy as np

image = cv2.imread("../src/img/19/figuras.jpeg")
cv2.imshow("Original", image)
cv2.waitKey(0)

original_image = image

# Escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Encontrar bordes con Canny
edged = cv2.Canny(gray, 45, 180)

contours, hierachy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow("Canny Edges After Contouring", edged)
cv2.waitKey(0)

i = 0
for c in contours:
    if(cv2.contourArea(c) < 0.5):
        continue
    (x, y, w, h) = cv2.boundingRect(c)
    # Recortamos el controno y mostramos el resultado
    cropped_contour = original_image[y:y+h, x:x+w]
    name = "recorte_" + str(i+1)
    cv2.imshow(name, cropped_contour)
    cv2.waitKey(0)
    i += 1


cv2.drawContours(image, contours, -1, (0, 255, 0), 1)
cv2.imshow('Contornos', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
