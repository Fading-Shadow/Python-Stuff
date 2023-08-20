list = [1,2,3,4,5,6,7,8,9,0]

def ReverseInPlace(list):
    for i in range(0,int(len(list)/2)):
        aux = int(list[i])
        list[i] = list[len(list)-i-1]
        list[len(list)-i-1] = aux

def display(list):
    for i in range(0,len(list)):
        print(list[i],end=" ")
    print()

display(list)
ReverseInPlace(list)
display(list)