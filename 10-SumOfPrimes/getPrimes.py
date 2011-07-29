import math

# Our initial seed of prime numbers up to 99
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def findPrimeUpTo(n):
    i = 99
    while i <= n:
        i += 2 #only need to check odds
        if checkIfPrime(i):
            prime.append(i)
    return prime

def checkIfPrime(n):
    sqrt = math.floor(math.sqrt(n))
    for p in prime:
        if p > sqrt: #Max prime factor would be the sqrt
            break
        if (n % p) == 0:
            return False
    return True


findPrimeUpTo(2000000)
print sum(prime)
