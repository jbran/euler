import math

primes = range(1,21)

##Brute force approach takes 3m 12s
def findMax():
    i = 2520
    while True:
        #print i
        if checkNum(i):
            print i
            break
        i += 1

def checkNum(n):
    for i in primes:
        if n % i != 0:
            return False
    return True

# Learned approach takes .103s
def findPrimesUpTo(n):
    prime = [2,3,5,7]
    i = 11
    while i < n:
        if checkIfPrime(i,prime):
            prime.append(i)
        i += 2
    return prime

def checkIfPrime(n, prime):
    sqrt = math.floor(math.sqrt(n))
    for p in prime:
        if p > sqrt:
            break;
        if (n % p) == 0:
            return False
    return True

def findSmallestDivisible(primes, n):
    total = 1
    sqrt = math.floor(math.sqrt(n))
    for i in primes:
        if i <= sqrt: 
            val = math.floor(math.log(n) / math.log(i))
            total = total * (i ** val)
        else:
            total = total * i

    return total

def findMaxFast(n):
    primes = findPrimesUpTo(n) 
    return findSmallestDivisible(primes, n)



print findMaxFast(20)
