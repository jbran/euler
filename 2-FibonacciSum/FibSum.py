


def fibEvenSum(limit):
    minus2 = 0
    minus1 = 1
    sum = 0
    while True:
        f = minus1 + minus2
        if f > limit:
            break
        minus2 = minus1
        minus1 = f

        if f % 2 is 0:
            sum += f

    return sum
            



print fibEvenSum(4000000)
