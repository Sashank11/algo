def dec_bin(n):
    assert int(n) == n, 'The number must be integer only!'
    if n == 0:
        return 0
    else:
        return n%2 + 10* dec_bin(int(n/2))

print(dec_bin(7))