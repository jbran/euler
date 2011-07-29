# Our initial seed of prime numbers up to 99
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def findNthPrime(n):
    i = 100
    while len(prime) < n:
        i += 1
        if checkIfPrime(i):
            prime.append(i)
    return prime

"""Return if Prime

Go through our list of primes and see if an input, n, is divisible by that prime number.

"""
def checkIfPrime(n):
    for p in prime:
        if (n % p) == 0:
            return False
    return True


print findNthPrime(10001)# 104743
