list = [1,2,3,4,5,6,7,8,9,0]

def odds(list): # prints the odd indexes so only the even values in this case
    for i in range(0,len(list)):
        if i % 2 == 1:
            print(list[i],end=" ")

odds(list)