list= []
for i in range(1,21): # creating the list of the first 20 numbers
    list.append(i)
print("The list is: "+str(list))

def on_all(list):
    for i in range(0,len(list)):
        print(list[i]*list[i],end=" ")

on_all(list)