div = [2,3,5,7,9]

def isprime(num):
    prime = True
    i = 0
    while i<=4:
        if num % div[i] == 0:
            prime = False
            break
        else:
            i += 1
    return (prime)

num = int(input('Enter a number: '))
print(isprime(num))
