def fast_pow(x, y):
    r = 1
    while y > 0:
        if y%2==1:
            r *= x
        x *=x
        y = y // 2
    return r
def test_fast_pow():
    for x in range(101):
        for y in range(101):
            assert x * y == fast_pow(x, y)