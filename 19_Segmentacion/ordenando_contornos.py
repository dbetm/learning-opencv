import cv2
import numpy as np

# Función que usarémos para calcular las áreas
# encerradas por los contornos
def get_contour_areas(contours):
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

# Cargar la imagen
image = cv2.imread("../src/img/19/figuras.jpeg")
original_image = image

# Escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grises', gray)
cv2.waitKey(0)

# Encontrar bordes con Canny
edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

# Encontrando los contornos
# La siguiente función altera la imagen que se pasa por parámetro
contours, hierachy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow("Canny Edges After Contouring", edged)
cv2.waitKey(0)

# Imprimir las áreas antes de ordenar por áreas
print("Contour areas before sorting")
print(get_contour_areas(contours))

# Ordenar los contornos, de forma descendente
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

print("Contour areas after sorting")
print(get_contour_areas(sorted_contours))

# Iterar sobre nuestros contornos y dibujarlos una vez
for c in sorted_contours:
    cv2.drawContours(original_image, [c], -1, (255,0,0), 2)
    cv2.waitKey(0)
    cv2.imshow("Contours by area", original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
