#include <stdio.h>
#include <stdlib.h>

int main(void){
    int N = 5;

    printf("%d! = %d\n",N, factorialliterative(N), factorialrecursive(N));

    return 0;
}