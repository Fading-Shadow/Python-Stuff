print("Give a number: ",end="")
nr = int(input())
list = []
while nr:
    list.insert(0,nr%10)
    nr = int(nr/10)

print(list)