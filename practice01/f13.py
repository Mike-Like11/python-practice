import math
def f13(n, m):
    sum_1=0
    for i in range(1, n+1):
            sum_1 += 49 * i ** 7 - 14 * i ** 5
    sum_2=0
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum_2 += math.cos(j) - 10 * i ** 6
    return sum_1-sum_2