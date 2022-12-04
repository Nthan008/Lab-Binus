int fibonacciiterative(int N){
    int tmp0 = 0;
    int tmp1 = 1;
    int output;
    if (N==0){
        return tmp0;
    } else if (N == 1){
        return 1;
    } else {
        int tmp0 = 0;
        int tmp1 = 1;
        int output;
        for (int i = 2; i<= N; i++){
            output = tmp0 + tmp1;
            tmp0 = tmp1;
            tmp1 = output;
        }
    }
    return output;
}

int fibonaccirecursive(int N){

    if (N ==  0){
        return 0;
    } else if (N == 1){
        return 1;
    } else {
        return fibonaccirecursive(N-1)+fibonaccirecursive(N-2);
    }
}