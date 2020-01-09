rgb = imread('SAT.jpg');
I = rgb2gray(rgb);

se = strel(ones(2,2));

im_dilate = imdilate(I,se);

im_closing = imerode(im_dilate,se);

im_dilate2 = imdilate(im_closing,se);

basic_gradient = imdilate(im_dilate2, se) - imerode(im_dilate2, se);

basic_gradient = imcomplement(basic_gradient);

T = adaptthresh(basic_gradient,0.1,'ForegroundPolarity','dark','Statistic','gaussian');

figure
imshow(I)
figure
imshow(T, [])
% I2=py.edged.morphoedgedetect(I)
% figure(1) 
% subplot(1,2,1), imshow(I,[]);title('Original Image');
% subplot(1,2,2), imshow(I2,[]);title('Edge Detected');

