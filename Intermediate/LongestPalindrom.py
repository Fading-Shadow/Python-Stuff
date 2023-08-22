def isPalindrome(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

print("Give a string: ")
string = str(input())

aux = ""
result = ""
for i in string.split(" "):
    aux += i
    if isPalindrome(aux) == True:
        if len(result) < len(aux):
            result = aux
        aux = ""

print(result)