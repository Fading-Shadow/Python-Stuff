import random
number = random.randint(1, 10) # returns an int between 1 to 10
answer = 11
tries = [0,0,0,0,0,0,0,0,0,0]
while int(answer) != int(number):
    print ("Guess the number from 1 to 10")
    answer = int(input())
    tries[answer+1] = 1
    if answer > number:
        print("Too high")
    elif answer < number:
        print("Too low")
    else:
        sum=0
        for i in range(0,10):
            sum += int(tries[i])
        print("Correct the number was: "+str(answer) + "\nIt only took "+str(sum)+" tries!")
