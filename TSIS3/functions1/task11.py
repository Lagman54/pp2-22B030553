def isPalindrome(s):
    return s == s[::-1]


print(isPalindrome("abc"))
print(isPalindrome("abacaba"))
