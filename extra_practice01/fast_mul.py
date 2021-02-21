def fast_mul(x, y):
    if y==0 or x==0:
        return 0
    r = 0
    while y > 0:
        if y%2==1:
            r += x
        x *= 2
        y = y // 2
    return r
def test_fast_mul():
    for x in range(101):
        for y in range(101):
            assert x * y == fast_mul(x, y)