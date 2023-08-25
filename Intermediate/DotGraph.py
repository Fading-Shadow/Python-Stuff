class DotGraph:
    def __init__(self,rows,cols): # Construct the matrix
        self.rows = rows+1
        self.cols = cols+1
        self.m = []
        for i in range(0,self.rows):
            aux = []
            for j in range (0,self.cols):
                aux.append(".")
            self.m.append(aux)

    def addEdge(self,row,col):
        self.m[row][col] = "x"

    def removeEdge(self,row,col):
        self.m[row][col] = "."

    def display(self):
        for i in range(0,self.rows):
            for j in range (0,self.cols):
                if j == 0:
                    if i == 0:
                        print("o",end=" ")
                    else:
                        print("|",end=" ")
                elif i == 0:
                    print("-",end=" ")
                else:
                    print(self.m[i][j],end=" ")
            print("")


a = DotGraph(4,4)
a.addEdge(0,1)
a.addEdge(1,2)
a.addEdge(2,3)
a.addEdge(3,3)
a.display()
