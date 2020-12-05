clc;
clear;
close all;

A = imread("test6.jpg");
subplot(221);
imshow(A);
title('Image de départ');

B = A(1005:1137,1102:1779,:);
subplot(222);
imshow(B);
title('B : découpe cadran');

C = imcomplement(B);
subplot(223);
imshow(C);
title('C : Image inversée');

cadran = C(:,:,2);
subplot(224);
imshow(cadran);
title('cadran : Résultat en enlevant le vert');

imwrite(cadran, "cadran.png");