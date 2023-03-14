class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def search(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def SizeTree(self):
        l=self.inorder([])
        return len(l)



bst = BSTNode()
choice=1
while(choice):
    n=int(input("Enter 1 for insert,2 for delete,3 for search, 4 for check the size of Tree,5 for inorder traversal, 6 for exit\n"))
    if(n==1):
        x=1
        while(x):
            num=int(input("Enter the no"))
            bst.insert(num)
            x=int(input("1 for insert more , 0 for exit\n"))
    elif(n==2):
        x=int(input("enter node to delete"))
        bst.delete(x)
    elif(n==3):
        x=int(input("enter node to search"))
        t=bst.search(x)
        if(t):
            print("Item is present in Tree")
        else:
            print("Item is not present in the Tree")
    elif(n==4):
        print("The Size of tree is ",bst.SizeTree())
    elif(n==5):
        print(bst.inorder([]))
    elif(n==6):
        choice=0
    else:
        print("You entered a wrong key,please enter correct option\n")
