clc;
clear;
close all;

I = rgb2gray(imread('test3.jpg'));
subplot(131);
imshow(I);
title("image de base en gris");

I = imcomplement(I);
subplot(132);
imshow(I);
title("image inversée");

SE = strel('rect', [1 2]);
I = imerode(I, SE);
subplot(133);
imshow(I);
title("image érodée");

imwrite(I, "testErosion.png");