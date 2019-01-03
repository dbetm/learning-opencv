# and, or, negación y XOR

# rectangular region of interest (ROI)
import cv2

# Cargamos las 2 imágenes
img1 = cv2.imread("../src/img/7/girasoles.jpg")
img2 = cv2.imread("../src/img/7/github.jpg")

# Se quiere poner el logo en la esquina izquierda y por eso se crea un ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# Ahora se crea una máscara del logo y se hace una máscara inversa también
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# Límite / Umbral
ret, mask = cv2.threshold(img2gray, 250, 255, cv2.THRESH_BINARY)
# inversa
mask_inv = cv2.bitwise_not(mask)
# Ahora se pone oscura el área del logotipo en ROI
img1_bg = cv2.bitwise_and(roi, roi, mask = mask)
# Tomar solamente la región del logotipo de la imagen del logo
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
# Poner el logo en ROI y modificar la imagen principal
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv2.imshow("res", img1)
# Para guardarla
cv2.imwrite("../src/img/7/agregandoUnaImagen.png", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
