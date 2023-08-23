class Graph:
    def __init__(self,rows,cols): # Construct the matrix
        self.rows = rows+1
        self.cols = cols+1
        self.m = []
        for i in range(0,self.rows):
            aux = []
            for j in range (0,self.cols):
                aux.append(0)
            self.m.append(aux)

    def addEdge(self,row,col):
        self.m[row][col] = 1

    def removeEdge(self,row,col):
        self.m[row][col] = 0

    def display(self):
        for i in range(0,self.rows):
            for j in range (0,self.cols):
                print(self.m[i][j],end=" ")
            print("")

# a = Graph(3,3)
# a.display()
# a.addEdge(0,2)
# print()
# a.display()