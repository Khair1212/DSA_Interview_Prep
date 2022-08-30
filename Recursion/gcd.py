# gcd (8,2) = 2
#
# gcd (48,18)
# step 1: 48/18 = 2 reemainder 12
# step 2: 18/12 = 1 remainder 6
# step 3: 12/6 = 2 remainder 0
#
# gcd(a,0) = a
# gcd(a, b) = gcd(b, a mod b)
# unintentional case
# - positive integer
# - Covert negative numerbs to positive

def gcd(a, b):
    assert int(a) ==a and int(b) == b, 'the numbers must be integer'
    if a < 0:
        a = -1*a
    if b < 0:
        b = -1 * b

    if b == 0:
        return a
    return gcd (b, a%b)

print(gcd(48, 18))