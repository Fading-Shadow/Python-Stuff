def convert(base,list): # converts to base 10
    result = []
    for i in range(0,len(list)):
        aux = str(list[i])
        sum = 0
        for j in range(0,len(aux)):
            sum += int(aux[j])*(base**(len(aux)-j-1))
        result.append(sum)
    return result

list = [1,101,111] # base 2
list = convert(2,list)
print(list)