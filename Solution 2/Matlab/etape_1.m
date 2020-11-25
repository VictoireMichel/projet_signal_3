clc;
clear;
close all;

A = imread("linkyTest.jpg");
B = A(208:346,131:534,:);
imwrite(B, "linky.png");