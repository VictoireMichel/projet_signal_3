clc;
clear;
close all;

A = imread("linkyTest.jpg");
imshow(A);

B = A(208:346,131:534,:);
figure;
imshow(B);

imwrite(B, "linky.png");