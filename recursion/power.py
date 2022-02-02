def power(base, exp):
    assert exp>=0 and int(exp) == exp, 'The exponent should be postive interger.'
    if base == 0:
        return 0
    if base == 1:
        return 1
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

print(power(2, 10))
