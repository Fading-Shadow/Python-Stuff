print("Give a number: ")
number = input()
number = int(number)
sum = 0
for i in range(number+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print("The sum of all numbers from 1 to "+str(number)+" that are multiples of 3 or 5 is "+str(sum))