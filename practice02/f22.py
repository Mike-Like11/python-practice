def f22(x):
    a = x & 255
    b = x & 256
    c = x & 2096640
    d = x & 534773760
    e = x & 1610612736
    f = x & 2147483648
    a = a << 22
    b = b << 13
    c = c >>9
    d = d >> 9
    e = e << 1
    f = f >> 11
    x = a | b | c | d | e | f
    return x
