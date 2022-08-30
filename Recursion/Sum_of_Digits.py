def Sum(n):
    assert int(n) == n and n >=0, "The number has to be a positive integer only"
    if n==0:
        return 0
    return n%10+Sum(int(n/10))

print(Sum(5))