print("How many days are in a year on the planet?")
days = float(input())
print("The amount of years it takes to generate a leap year on this planet is: ",end="")
print (round((1/(days-int(days))),3))