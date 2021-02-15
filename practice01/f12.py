import math
def f12(x):
    if x<-23:
        return 49*x**7-x**5
    elif -23<=x<32:
        return math.exp(x**5)+71*x**8
    else:
        return abs(math.cos(x)+x**3)-33*x**3-74