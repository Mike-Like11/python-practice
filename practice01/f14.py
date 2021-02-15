import math
def f14(n):
    if n==0:
        return 9
    elif n==1:
        return 2
    else:
        return f14(n - 2) / 5 - math.cos(f14(n - 2))