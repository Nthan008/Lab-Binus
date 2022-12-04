#include <stdio.h>
#include "mylib.h"

int main(void){
    int n;

    for(int i = 1; i <= n; i++){
        printf("F(%d)= %d", i, fibonaccirecursion(i));
    }
    return 0;
}