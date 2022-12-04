int factorialinterative(int N){
    int output = 1;

    for(int i = 1; i <= N; i++){
        output = output * i;
    }
    return output;
}

int factorialrecursive(int N){
    if (N == 1){
        return 1;
    } else {
        return N*factorialrecursive(N-1);
    }
}
