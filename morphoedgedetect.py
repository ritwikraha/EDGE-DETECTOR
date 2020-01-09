import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def morphoedgedetect(imgj):
	kernel = np.ones((2,2),np.uint8)

	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	dilation = cv2.dilate(closing,kernel,iterations = 1)

	gradient = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)


	edges_inv = cv2.bitwise_not(gradient)

	def psnr(imgORI, imgFIN):
	    mse = np.mean( (imgORI - imgFIN) ** 2 )
	    if mse == 0:
	      return 100
	    PIXEL_MAX = 255.0
	    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


	def thres(imgk):
	    imgbinar = cv2.adaptiveThreshold(imgk,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	            cv2.THRESH_BINARY,11,4)
	    
	    return imgbinar

	imgbinary= thres(edges_inv)
	d=psnr(edges_inv,imgbinary)
	if d<=psnr(img,gradient):
		imgF = cv2.addWeighted(imgbinary, 0.3, edges_inv, 0.7, 0)
		

	imgF = cv2.addWeighted(imgbinary, 0.5, edges_inv, 0.5, 0)

	return imgF
