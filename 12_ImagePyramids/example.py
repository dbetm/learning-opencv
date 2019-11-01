import cv2

image = cv2.imread("../src/img/8/cieloEstrellado.jpg")

for i in range(6):
    cv2.imshow("Recursividad " + str(i), image)
    image = cv2.pyrDown(image)

cv2.waitKey(0)
cv2.destroyAllWindows()
