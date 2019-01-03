"""
Esto también es suma, pero con diferentes pesos da la sensación
de mezcla o transparencia.
Se suman mediante esta ecuación:
g(x) = (1-alpha) * f_0(x) + alpha * f_1(x)
Variando  alfa de 0 a infinito, puedes efectuar una transición suave entre
una imagen y la otra.
"""

import cv2

img1 = cv2.imread("../src/img/7/girasol.jpg")
img2 = cv2.imread("../src/img/7/astronauta.jpg")

print("Total de pixeles: " + str(img1.size))
print("Total de pixeles: " + str(img2.size))

# a la primera se le da un peso de 0.7 y a la otra de 0.3
# con gamma igual a 0 (último parámetro)
dst = cv2.addWeighted(img2, 0.6, img1, 0.4, 0)

cv2.imshow("Fusión", dst)
# Para guardarla
cv2.imwrite("../src/img/7/fusión.png", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
