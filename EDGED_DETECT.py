import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

img = cv2.imread('img/testna_slika1b.bmp',0)
kernel = np.ones((2,2),np.uint8)#using a kernel to reconstruct the image as per convenience

"""CLOSING OPERATION- is simply the opposite of opening operation in morphological operator
an OPENING OPERATION- is erosion followed by dilation,it is useful in removal of noises
EROSION- is the process of eroding away the boundary of the image , (a pixel in the original image is 
considered 1 if all the pixels under the kernel is 1)
DILATION-just the opposite of erosion, used to thicken an image
hence CLOSING= DILATION then EROSION
OPENING=EROSION then DILATION, CLOSING is helpful in smoothening out the object)"""

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
dilation = cv2.dilate(closing,kernel,iterations = 1)#dilating the closed image

"""It is the difference between dilation and erosion of an image.
The result will look like the outline of the object."""

gradient = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)


edges_inv = cv2.bitwise_not(gradient)#inverting the gradient image so that the edges are better detected


"""the function psnr will calculate the peak-signal-noise-ratio of two given images
Peak Signal to Noise Ratio ( PSNR) and Mean Square Error (MSE)
are used to comparing the squared error between the original image and the reconstructed image.
There is an inverse relationship between PSNR  and MSE.
When you try to compute the MSE between two identical images,
the value will be zero and hence the PSNR will be undefined (division by zero).
here it is seen the value may come around 0.033 which allows us to approximate
that the images are 30% similar)"""

def psnr(imgORI, imgFIN):
    mse = np.mean( (imgORI - imgFIN) ** 2 )
    if mse == 0:
      return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

"""the thres function is defined in such a way that an adaptive threshold of the input image is taken
the algorithm gets different thresholds for different areas of the image
threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
notice 11 is the size of the pixel around which thresholding is performed and C is an arbitrary constant subtracted 
from the Gaussian function"""
def thres(imgk):
    imgbinar = cv2.adaptiveThreshold(imgk,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,4)
    
    return imgbinar

imgbinary= thres(edges_inv)#passing the inverted image through the thres filter
d=psnr(edges_inv,imgbinary)# calculating the psnr of the inverted and the filtered image 
print ('PSNFR OF FILTERED IMAGES:',d)
print ('PSNFR OF ORIGINAL IMAGES:',psnr(img,gradient))#calculating the psnr of the original and gardient image
"""since higher the PSNR of two set of images the better the degraded image has been reconstructed
or in other words the better the more the set of images are similar
hence if a set of image has higher PSNR than the other set that set is more similar than the other set
which means if the filtered images (d) have a higher PSNR than the original ones
then the original ones have been dissimilar before the  thresholding operation 
hence the inverted gradient and thresholded image
is merged 0.5 and 0.5 (equal proportions) weighted addition
If however the PSNR of the filtered images is lower than the original images
then the dissimilarity of the filtered images is higher than that of the original ones 
which means the adaptive threshold operation has rendered them too dissimilar
hence they are merged in 0.3(of the thresholded image) and 0.7(of the inverted gradient) weighted addition"""
if d<=psnr(img,gradient):
	imgF = cv2.addWeighted(imgbinary, 0.3, edges_inv, 0.7, 0)
	

imgF = cv2.addWeighted(imgbinary, 0.5, edges_inv, 0.5, 0)





titles = ['Original Image','EDGE-INV','RAW EDGE','FINAL']
images = [img, edges_inv, imgbinary, imgF]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()