def rotate(k,list):
    list1 = []
    for i in range(0,len(list)):
        list1.append(list[(i+k)%len(list)])
    return list1

list = [1,2,3,4,5,6]
print("Initial list: "+str(list))
print("By how many elements do you want to rotate the list? k = ",end="")
k = int(input())

list = rotate(k,list)
print("The list rotated by "+str(k)+" is: "+str(list))