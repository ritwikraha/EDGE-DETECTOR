import cv2
import numpy as np
import math
import edged
from matplotlib import pyplot as plt

img = cv2.imread('img/testna_slika1b.bmp',0)
imgEdge= edged.morphoedgedetect(img)


cv2.imwrite('new_edge.jpg',imgEdge)