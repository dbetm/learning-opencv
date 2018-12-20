""" el programa carga una imagen en escala de grises, la muestra, guarda la imagen si presionas ‘s’ y termina su ejecución, o simplemente termina sin guardar si presionas la tecla ESC. """

import numpy as np
import cv2

img = cv2.imread("../src/img/3/ninja.png", 0)
cv2.imshow("image", img)

k = cv2.waitKey(0)
if(k == 27): # Wait for ESC key to exit
    cv2.destroyAllWindows()
elif(k == ord('s')): # Wait for 's' key to save and exit
    cv2.imwrite("../src/img/3/ninja2-gray.png", img)
    cv2.destroyAllWindows()
