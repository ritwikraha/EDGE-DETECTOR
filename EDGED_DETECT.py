import cv2
import numpy as np

img = cv2.imread('SAT.jpg',0)
kernel = np.ones((10,10),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img2=closing
cv2.imwrite('SAT_closing.jpg',img2)
dilation = cv2.dilate(img2,kernel,iterations = 1)
img3=dilation
cv2.imwrite('SAT_closing_dilation.jpg',img3)
gradient = cv2.morphologyEx(img3, cv2.MORPH_GRADIENT, kernel)
imgf=gradient
cv2.imwrite('SAT_last_not_least.jpg',imgf)
edges = cv2.Canny(imgf,100,200)
cv2.imwrite('SAT_FINAL.jpg',edges)
edges_inv = cv2.bitwise_not(edges)
cv2.imwrite('SAT_FINAL_LAST.jpg',edges_inv)

