class Matrix:
    def __init__(self,rows,cols): # Construct the matrix
        self.rows = rows+1
        self.cols = cols+1
        self.m = []
        for i in range(0,self.rows):
            aux = []
            for j in range (0,self.cols):
                aux.append(0)
            self.m.append(aux)

    def value(self,value,row,col):
        self.m[row][col] = value

    def display(self):
        for i in range(0,self.rows):
            for j in range (0,self.cols):
                print(self.m[i][j],end=" ")
            print("")

# a = Matrix(4,4) # initializing the matrix object
# a.value(5,0,2) # giving self.m[0][2] the value 5
# print(a.m[0][2])