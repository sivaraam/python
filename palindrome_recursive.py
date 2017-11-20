def toChars(s):
    import string
    s = string.lower(s)
    ans = ''
    for c in s:
        if c in string.lowercase:
            ans = ans + c
    return ans

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

baseIndent = '    '
def isPalPrint(s, indent):
    print indent + 'isPalPrint called with ' + s
    if len(s) <= 1:
        print indent + 'About to return True from "Base case"'
        return True
    else:
        ans = s[0] == s[-1] and isPalPrint(s[1:-1], indent + baseIndent)
        print indent + 'About to return ', ans, 'from "Recursive case"'
        return ans

def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    return isPalPrint(toChars(s),  '    ')


print isPalindrome('Guttag')


print isPalindrome('Guttug')

print isPalindrome('Able was I ere I saw Elba')
