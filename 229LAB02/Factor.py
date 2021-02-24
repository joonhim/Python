import math
def primeFactors(a):

    while a % 2 == 0:
        print(2)
        a = a / 2

    for i in range(3, int(math.sqrt(a)) + 1, 2):
        while a % i == 0:
            print(i)
            a = a /i
    if a > 2:
        print(a)


a = 342
primeFactors(a)