for n in range(2000, 3201):
    if n % 7 == 0 and not n % 5 == 0:
        print(n, end=",")