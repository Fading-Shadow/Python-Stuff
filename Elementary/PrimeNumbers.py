print("give a maximum number ")
n = int(input())
def isPrime(number):
    for i in range(2,int(number/2+1)):
        if number % i == 0:
            return False
    return True

for i in range(2,n+1):
    if isPrime(i) == True:
        print(str(i), end=', ')