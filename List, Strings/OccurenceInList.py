list = [1,2,3,4]

def occurs(elem,list):
    for i in range(0,len(list)):
        if elem == int(list[i]):
            print("The element occurs in the list")
            return
    print("The element does not occur in the list")

print("Give a number to check in the list")
number = int(input())
occurs(number,list)