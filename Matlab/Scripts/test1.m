clc;
clear;
close all;

A = imread("test6.jpg");

B = A(1005:1137,1102:1779,:);

C = imcomplement(B);

cadran = C(:,:,2);

imwrite(cadran, "cadran.png");