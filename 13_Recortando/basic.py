import cv2
import numpy as np

image = cv2.imread('../src/img/9/girasol.jpg')

height, width = image.shape[:2]

# Coordenadas del píxel inicial (esquina superior izquierda del área a recortar)
start_row, start_col = int(height * 0.25), int(width * 0.25)

# Coordenadas del píxel final (esquina inferior derecha)
end_row, end_col = int(height * 0.75), int(width * 0.75)

# Recortar
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.imshow("Recortada", cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()
