# Given 2 strings, write a program that efficiently finds the longest common subsequence.

str1 = "Ana has apples"
str2 = "Ana goes to someone that has apples"

# result should be "has apples" and not "Ana"

seq=""
substring = ""

for i in range(0,len(str1)):
    init = i
    for j in range(0,len(str2)):
        if str1[i] == str2[j]:
            substring += str(str1[i])
            if i < len(str1)-1:
                i += 1
            if j < len(str2)-1:
                j += 1
        elif str1[i] != str2[j]:
            if len(substring) > len(seq):
                seq = str(substring)
                substring = ""
            else:
                substring = ""
                if init < len(str1)-1:
                    i = init+1
                j = 0

print("The longest common subsequence is: "+seq)