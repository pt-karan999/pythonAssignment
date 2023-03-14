class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    def isEmpty(self):
        return self.front == None
    def EnQueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):
        if self.isEmpty():
            return
        t=self.front.data
        temp = self.front
        self.front = temp.next
        return t
        if(self.front == None):
            self.rear = None

    def peek(self):
        return self.front.data
if __name__ == "__main__":
    queue = Queue()
    choice=1
    while(choice):
        n=int(input("Enter 1 for enqueue,2 for dequeue,3 for peek, 4 for check if queue is empty or not and 5 for exit\n"))
        if(n==1):
            x=1
            while(x):
                num=int(input("Enter the no"))
                queue.EnQueue(num)
                x=int(input("1 for insert more , 0 for exit\n"))
        elif(n==2):
            print("dequeue: item=",queue.DeQueue())
        elif(n==3):
            print("value on front is ",queue.peek())
        elif(n==4):
            if(queue.isEmpty()):
                print("yes, the queue is empty\n")
            else:
                print("No,the queue is not empty\n")
        elif(n==5):
            choice=0
        else:
            print("You entered a wrong key,please enter correct option\n")