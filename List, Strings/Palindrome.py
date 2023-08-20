def isPalindrome(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print("Give a string: ",end="")
str = str(input())
if isPalindrome(str):
    print("The given string is a palindrome")
else:
    print("The given string is NOT a palindrome")