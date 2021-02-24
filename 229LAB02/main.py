def SieveOfEratosthenes(k):

    prime = [True for i in range(k + 1)]
    a = 2
    while (a * a <= k):


        if (prime[a] == True):

            for i in range(a * a, k + 1, a):
                prime[i] = False
        a += 1


    for a in range(2, k + 1):
        if prime[a]:
            print(a,)

if __name__ == '__main__':
    k = 10000
    print("Following are the prime numbers smaller",)
    print("than or equal to", k)
    SieveOfEratosthenes(k)