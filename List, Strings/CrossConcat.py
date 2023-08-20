list1 = [1,2,3,4,5]
list2 = ["a","b","c","d"]
def crossConcat(list1,list2):
    list = []
    if len(list1) >= len(list2):
        for i in range(0,len(list1)):
            list.append(list1[i])
            if i < len(list2):
                list.append(list2[i])
    elif len(list2) > len(list1):
        for i in range(0,len(list2)):
            if i < len(list1):
                list.append(list1[i])
            list.append(list2[i])
    return list

print(crossConcat(list1,list2))