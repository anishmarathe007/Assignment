def reverseString(s):
    str = ''
    for i in s:
        str = i + str
    return str

def isPalindrome(inputS):
    if reverseString(inputS) == inputS :
        return 1
    else:
        return 0
