list = [1,5,3,2,6,9,4]

def bubblesort(list):
    sorted = False
    while sorted != True:
        sorted = True
        for i in range(0,len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                i -= 1
                sorted = False

print(list)
bubblesort(list)
print("Sorted: ",end=" ")
print(list)