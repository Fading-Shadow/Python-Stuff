str = "The quick brown fox" # result: “Hetay uickqay rownbay oxfay”.
def toPigLatin(str):
    aux = str.split(" ")
    result = ""
    for i in range(0,len(aux)):
        j = aux[i]
        if j[0] == j[0].upper():
            if i < len(aux)-1:
                result += j[1].upper()+j[2:len(j)]+j[0].lower()+"ay "
            else:
                result += j[1].upper()+j[2:len(j)]+j[0].lower()+"ay"
        else:
            if i < len(aux)-1:
                result += j[1:len(j)]+j[0]+"ay "
            else:
                result += j[1:len(j)]+j[0]+"ay"
    return result

def toEnglish(str):
    aux = str.split(" ")
    result = ""
    for i in range(0,len(aux)):
        j = aux[i]
        if j[0] == j[0].upper():
            if i < len(aux)-1:
                result += j[len(j)-3].upper()+j[0:len(j)-3].lower()+" "
            else:
                result += j[len(j)-3].upper()+j[0:len(j)-3]
        else:
            if i < len(aux)-1:
                result += j[len(j)-3]+j[0:len(j)-3]+" "
            else:
                result += j[len(j)-3]+j[0:len(j)-3]
    return result
print("String:\n"+str+"\n")
print("\nTo PigLatin: ")
str = toPigLatin(str)
print(str)
print("\nBack To English: ")
str = toEnglish(str)
print(str)
