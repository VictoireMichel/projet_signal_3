cadranTest = imread("cadran.png");
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

imwrite(cadranTest, "newCadran.png");