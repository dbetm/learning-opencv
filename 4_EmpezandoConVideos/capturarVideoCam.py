import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Comprobar si cap inició la captura
print(cap.isOpened())
""" También puede acceder a algunas de las características de este
vídeo usando el método cap.get(PropID), donde PropID es un número del 0 al 18.
"""
while(True):
    # Captura de video cuadro a cuadro
    ret, frame = cap.read()
    # Operaciones sobre los cuadros
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Mostrar el cuadro resultante, en este caso muestra en escala de gris
    cv2.imshow('Marco', gray)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

# Se libera la captura
cap.release()
cv2.destroyAllWindows()
