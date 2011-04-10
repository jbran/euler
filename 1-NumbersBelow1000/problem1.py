

def go(n):
    target = n
    return sumDiv(3,target) + sumDiv(5,target) - sumDiv(15,target)

def sumDiv(n, target):
#The max value to sum to
    max_value = target // n
#Where the summation of 1...N = n(n+1)  / 2
    return n*(max_value*(max_value+1)) // 2

def sumOf3and5(n):
    sum = 0;
    for x in xrange(1,n):
       if x % 3 == 0 or x % 5 == 0:
            sum += x 
    return sum



#print sumOf3and5(10)
#print sumOf3and5(1000)
#print sumOf3and5(1000000000)
print go(1000000000)
