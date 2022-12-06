#include <stdio.h>

#include "mylib/mylib.h"

int main(void)
{
    int N = 2;

    int mat1[N][N] = {{1, 2}, {3, 4}};
    int mat2[N][N] = {{9, 8}, {7, 6}};
    int mat3[N][N];

    multiMat(mat1, mat2, mat3);

    printMat("Mat1", mat1);
    printMat("Mat2", mat2);
    printMat("Mat3", mat3);

    return 0;
}