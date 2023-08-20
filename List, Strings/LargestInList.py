list = [2,5,1,3,7,0]
def LargestInList(list):
    max = int(list[0])
    for i in range(0,len(list)):
        if int(list[i]) > max:
            max = list[i]
    print("The largest in the list is: "+str(max))

LargestInList(list)