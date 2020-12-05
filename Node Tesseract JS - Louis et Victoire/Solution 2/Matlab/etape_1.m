clc;
clear;
close all;

A = imread("linkyTest.jpg");
subplot(211);
imshow(A);
title("A : image de base");

B = A(208:346,131:534,:);
subplot(212);
imshow(B);
title("B : découpe du cadran");

imwrite(B, "linky.png");