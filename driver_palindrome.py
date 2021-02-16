from palindrome import isPalindrome

try:
    inputS = input("Enter the string\n")
    if isPalindrome(inputS):
        print(inputS, "is a Palindrome String")
    else:
        print(inputS, "is NOT A Palindrome String")

except ValueError as e:
    print(e)
