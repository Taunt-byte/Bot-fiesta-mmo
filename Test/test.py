import cv2
import numpy as np

img = cv2.imread("imagem.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray, 100, 200)


cv2.imshow("Imagem com bordas", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
