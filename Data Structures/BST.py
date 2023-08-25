class BST:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def insert(self,value):
        if self.value == None:
            self.value = value
        elif value < self.value:
            if self.left == None:
                self.left = BST()
            self.left.insert(value)
        else:
            if self.right == None:
                self.right = BST()
            self.right.insert(value)

    def preorder(self):
        if self.value:
            print(self.value,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        if self.value:
            print(self.value,end=" ")
    
    def inorder(self):
        if self.left:
            self.left.preorder()
        if self.value:
            print(self.value,end=" ")
        if self.right:
            self.right.preorder()


tree = BST()

tree.insert(5)
tree.insert(1)
tree.insert(7)
tree.insert(3)
tree.insert(8)

print("Preorder: ")
tree.preorder()

print("\nPostorder: ")
tree.postorder()

print("\nInorder: ")
tree.inorder()
print()