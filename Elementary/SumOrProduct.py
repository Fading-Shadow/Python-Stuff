print("Give a number: ")
number = input()
number = int(number)
print("+ or * ?")
op = str(input())
if op == '+':
    sum = 0
    for i in range(number+1):
        sum += i
    print("The sum of all numbers from 1 to "+str(number)+" is "+str(sum))

elif op == '*':
    product = 1
    for i in range(1,number+1): # to compute from 1 to number instead of from 0 to number in which case it would return 0
        product *= i
    print("The product of all numbers from 1 to "+str(number)+" is "+str(product))

else:
    print("Can't compute")