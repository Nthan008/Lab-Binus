#include <stdio.h>


int multiMat(int mat1[N][N], int mat2[N][N], int matResult[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            int sum = 0;
            for (int k = 0; k < N; k++)
            {
                sum = sum + (mat1[i][k] * mat2[k][j]);
            }
            matResult[i][j] = sum;
        }
    }
    return matResult;
}

static void printMat(const char *tag, int mat[N][N])
{
    printf("%s (%dx%d):\n", tag, N, N);
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf(" %3d", mat[i][j]);
        }
        printf("\n");
    }
}