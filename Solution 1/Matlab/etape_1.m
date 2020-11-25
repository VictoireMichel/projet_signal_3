clc;
clear;
close all;

A = imread("test6.jpg");
imshow(A);

B = A(1005:1137,1102:1779,:);
figure;
imshow(B);

C = imcomplement(B);
figure;
imshow(C);

cadran = C(:,:,2);
figure;
imshow(cadran);

imwrite(cadran, "cadran.png");