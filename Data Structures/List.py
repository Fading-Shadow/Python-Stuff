class List:
    def __init__(self,size):
        self.size = size
        self.array = []

    def push(self,value):
        if len(self.array) < self.size:
            self.array.append(value)
        else:
            print("The list is full!")
            return
        
    def pop(self):
        if len(self.array) > 0:
            return self.array.pop()
        else:
            print("The list is empty!")
            return
        
    def peek(self):
        return self.array[len(self.array)]

    def clear(self):
        self.array.clear()

    def display(self):
        for i in range(0,len(self.array)):
            print(self.array[i],end = " ")
        print("")

# a = List(3)
# a.push(5)
# a.push(4)
# a.push(3)
# a.push(5)
# a.display()
# a.pop()
# a.display()
# a.pop()
# a.pop()
# a.pop()
