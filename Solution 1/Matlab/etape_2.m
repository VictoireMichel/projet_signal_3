cadranTest = imread("cadran.png");
subplot(211);
imshow(cadranTest);
title("cadran de base");

limit = 128;
sizeCadran = size(cadranTest);
for i = 1:sizeCadran(1)
    for j = 1:sizeCadran(2)
        if limit < cadranTest(i,j)
            cadranTest(i, j) = 255;
        else
            cadranTest(i,j) = 0;
        end
    end
end

subplot(212);
imshow(cadranTest);
title("résultat");

imwrite(cadranTest, "newCadran.png");