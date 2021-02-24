def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)
a=200
b=10

print("gcd(", a , "," , b, ") = ", gcd(a, b))

