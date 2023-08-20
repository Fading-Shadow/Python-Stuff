list1=[1,3,5]
list2=[2,4,6,8]

def sortMerge(list1,list2):
    list = list1+list2
    return sorted(list)

print(sortMerge(list1,list2))