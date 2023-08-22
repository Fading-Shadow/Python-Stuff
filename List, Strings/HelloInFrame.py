list = ["Hello", "world", "in", "a", "frame"]

def get_max(list):
    max = 0
    for i in list:
        if len(i) > max:
            max = len(i)
    return max

def fill(width): # fills the line with * as appropriate
    for i in range(0,width+4):
        print("*",end="")
    print()

width = get_max(list)

fill(width) # first row

for i in list:
    if len(i) == width:
        print("* "+str(i)+" *")
    else:
        print("* "+str(i),end="")
        for i in range(0,width-len(i)):
            print(" ",end="")
        print(" *")


fill(width)