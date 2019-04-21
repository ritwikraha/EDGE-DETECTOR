# EDGE-DETECTOR #
- - - -

## Abstract ##
- - - -
This paper presents an innovative algorithm to efficiently detect edges from an image using Morphological operator and Adaptive Gaussian Thresholding.Proposes an alternative to existing algorithm by use of weighted combination of thresholded images.Edge Detection has been carried out by three methods consecutively. The first is the method of Morphological Gradient to detect outlines from an image by analysis of spatial structures.The next is adaptive gaussian thresholding performed on the inverted outlined image.The third and the final step is the weighted addition of the thresholded and inverted image based on dissimilarity recognised by a Peak-Signal-to-Noise-Ratio function.
- - - -

### Introduction ###

Edge detection is being used in a number of industries for image segmentation and data extraction in areas such as image processing, computer vision and machine vision.The image enhancement and edge detection problem can be approached from various methodologies among which one is Mathematical Morphology.It is the method for analysis of spatial structures which aims at analysis of the shape and form of the object. Most image enhancement algorithms depend on histogram equalization or gradient mapping.The noise filtering of the image has been achieved using erosion and dilation techniques from the OpenCV module while the rest of the functions such as PSNR have been achieved using numpy module. The algorithm has been developed using Python 3.7.1 and OpenCV 3.4.1

---
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/164c2a085a9f47da9c83f064186e81de)](https://www.codacy.com/app/rtzdzn/EDGE-DETECTOR?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ritwikraha/EDGE-DETECTOR&amp;utm_campaign=Badge_Grade)
