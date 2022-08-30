def power(x, m):
    assert m>=0 and int(m)==m , "x, m should be positive"
    if m == 0:
        return 1
    elif m == 1:
        return x
    else:
        return x * power(x, m-1)

print(power(2,4))