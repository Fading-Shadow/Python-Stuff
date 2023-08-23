class Queue:
    def __init__(self,size):
        self.size = size
        self.array = []

    def enqueue(self,value):
        if len(self.array) < self.size:
            self.array.insert(0,value)
        else:
            print("The queue is full!")
            return
        
    def dequeue(self):
        if len(self.array) > 0:
            return self.array.pop()
        else:
            print("The queue is empty!")
            return
        
    def peek(self):
        return self.array[len(self.array)]

    def clear(self):
        self.array.clear()

    def display(self):
        for i in range(0,len(self.array)):
            print(self.array[i],end = " ")
        print("")

# a = Queue(3)
# a.enqueue(5)
# a.enqueue(4)
# a.enqueue(3)
# a.enqueue(5)
# a.display()
# a.dequeue()
# a.display()
# a.dequeue()
# a.dequeue()
# a.dequeue()
