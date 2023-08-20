def forSum(list):
    sum = 0
    for i in range(0,len(list)):
        sum += list[i]
    print("For-sum: "+str(sum))

def whileSum(list):
    sum = 0
    i = 0
    while i < len(list):
        sum += list[i]
        i += 1
    print("While-sum: "+str(sum))

def recursiveSum(list,i):
    if i < len(list):
        return int(list[i]) + recursiveSum(list,i+1)
    else:
        return 0
    
list = [1,2,3,4,5]

forSum(list)
whileSum(list)
rec = recursiveSum(list,0)
print("Recursive-Sum: "+str(rec))