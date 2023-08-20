class Graph:
 # redo its not a TREE its a Graph/ Matrix
 def __init__(self): # Constructor
    self.left = None
    self.right = None
    self.value = None

 def insert(self,value):
    if self.value == None:
      self.value = value
    elif self.left == None:
        self.left = Graph()
        self.left.insert(value)
    elif self.right == None:
       self.right = Graph()
       self.right.insert(value)

 def display(self):
    if self.value != None:
       print(self.value,end=" ")
    else:
        if self.left != None and self.left.value != None:
            self.left.display()
        if self.right != None and self.right.value != None:
            self.right.display()

a = Graph()
a.insert(10)
a.insert(20)
a.insert(30)
a.insert(40)

a.display()
