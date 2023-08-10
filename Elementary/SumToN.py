print("Give a number: ")
number = input()
number = int(number)
sum = 0
for i in range(number+1):
    sum += i
print("The sum of all numbers from 1 to "+str(number)+" is "+str(sum))