def isPalindrome(s):
    if len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])

print(isPalindrome('awesome'))
print(isPalindrome('tacocat'))