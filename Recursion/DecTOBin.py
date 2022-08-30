def DecToBin(n):
    assert int(n) == n, "The parameter must be an integer only!"

    if int(n/2) == 0:
        return n%2
    return str(DecToBin(int(n/2))) + str(n % 2)

print(DecToBin(10))