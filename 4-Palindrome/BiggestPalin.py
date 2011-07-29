

palin = []

def biggest():
    for i in reversed(range(100,1000)):
        for j in reversed(range(100,1000)):
            val = i * j
            if isNumPalindrome(val):
                palin.append(val)
            j -= 1
    i -= 1
   

def isNumPalindrome(num):
    n = num
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n / 10
    return rev == num

biggest()
print sorted(palin)[-1]
