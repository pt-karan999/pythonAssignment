class node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Stack:
    def __init__(self):
        self.head = node("head")
        self.len=0

    def isEmpty(self):
        return self.len == 0
    
    def getSize(self):
        return self.len
    

    
    def peek(self):
        if self.isEmpty():
            raise Exception("Trying Peeking from an empty stack")
        return self.head.next.val

    def push(self, val):
        Node = node(val)
        Node.next = self.head.next
        self.head.next = Node
        self.len += 1
  
    def pop(self):
        if self.isEmpty():
            raise Exception("Trying to pop from an empty stack")
        rem = self.head.next
        self.head.next = self.head.next.next
        self.len -= 1
        return rem.val

if __name__ == "__main__":
    stack = Stack()
    choice=1
    while(choice):
        n=int(input("Enter 1 for push,2 for pop,3 for peek, 4 for check the size of stack, 5 for check if stack is empty or not and 6 for exit\n"))
        if(n==1):
            x=1
            while(x):
                num=int(input("Enter the no"))
                stack.push(num)
                x=int(input("1 for push more , 0 for exit\n"))
        elif(n==2):
            print("popped item=",stack.pop())
        elif(n==3):
            print("value on top is ",stack.peek())
        elif(n==4):
            print("the length of stack is ",stack.getSize())
        elif(n==5):
            if(stack.isEmpty()):
                print("yes, the stack is empty\n")
            else:
                print("No,the stack is not empty\n")
        elif(n==6):
            choice=0
        else:
            print("You entered a wrong key,please enter correct option\n")
