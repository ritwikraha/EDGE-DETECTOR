# EDGE-DETECTOR #
- - - -

## Abstract ##
- - - -
This paper presents an innovative algorithm to efficiently detect edges from an image using Morphological operator and Adaptive Gaussian Thresholding.Proposes an alternative to existing algorithm by use of weighted combination of thresholded images.Edge Detection has been carried out by three methods consecutively. The first is the method of Morphological Gradient to detect outlines from an image by analysis of spatial structures.The next is adaptive gaussian thresholding performed on the inverted outlined image.The third and the final step is the weighted addition of the thresholded and inverted image based on dissimilarity recognised by a Peak-Signal-to-Noise-Ratio function.
- - - -

### Introduction ###

Edge detection is being used in a number of industries for image segmentation and data extraction in areas such as image processing, computer vision and machine vision.The image enhancement and edge detection problem can be approached from various methodologies among which one is Mathematical Morphology.It is the method for analysis of spatial structures which aims at analysis of the shape and form of the object. Most image enhancement algorithms depend on histogram equalization or gradient mapping.The noise filtering of the image has been achieved using erosion and dilation techniques from the OpenCV module while the rest of the functions such as PSNR have been achieved using numpy module. The algorithm has been developed using Python 3.7.1 and OpenCV 3.4.1


- - - -
##  ALGORITHM ##
- - - -
```
Step 1: Start
Step 2: Input ‘Image’
Step 3: Define Kernel...............................(01)
Step 4: clo=Closing(‘Image’,kernel).................(02)
Step 5: dil=Dilation(clo,kernel)....................(03)
Step 6: grad=Gradient(dil,kernel)...................(04)
Step 7: edge_inv=~grad
Step 8: Procedure psnr(imgO,imgF)
	8.1: mse=mean()
	8.2: IF mse==0
	8.3:	return 100
	8.4: ELSE
	8.5:	pix_max=255.0
	8.6:	return 20*log(pix_max/sqrt(mse))
Step 9: Procedure thres(imgk)......................(05)
	9.1: imgb=Adaptivethreshold(imgk)
	9.2: return imgb
Step 10: imgbinary=thres(edges_inv)
Step 11: d=psnr(edges_inv,imgbinary)
Step 12: c=psnr(image,grad)
Step 13: IF d<c
	13.1: imgF=AddWeighted(imgbinary(0.3),edges_inv(0.7))...........(06)
Step 14: ELSE
	14.1: imgF=AddWeighted(imgbinary(0.5),edges_inv(0.5))...........(07)
Step 15: Display imgF
Step 16: End

1. defining a structuring element of size 2X2
2. refer to 
3. refer to
4. refer to
5. refer to 
6. weighted addition in 0.3 and 0.7 proportions
7. weighted addition in equal proportions

```
- - - - 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/164c2a085a9f47da9c83f064186e81de)](https://www.codacy.com/app/rtzdzn/EDGE-DETECTOR?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ritwikraha/EDGE-DETECTOR&amp;utm_campaign=Badge_Grade)
