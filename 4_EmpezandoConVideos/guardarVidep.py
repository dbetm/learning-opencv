import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define el codec y crea el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter("../src/videos/4/output.avi", fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == True):
        frame = cv2.flip(frame, 0) # Invierte el cuadro

        # escribe el cuadro invertido
        out.write(frame)
        # Lo mostramos
        cv2.imshow("Cuadro", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break

# Libera si la tarea ha terminado
cap.release()
out.release()
cv2.destroyAllWindows()
