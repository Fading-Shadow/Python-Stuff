list = [1,2,3,4,5]

def runningSum(list):
    sum = 0
    for i in range(0,len(list)):
        sum += list[i]
    return sum

print(runningSum(list))