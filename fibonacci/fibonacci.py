def fib(n):
    a=0
    b=1
    if n<=0:
        print("Incorrect")
    elif(n==1):
        return a
    elif(n==2):
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
n=int(input("Enter the no."))
print(fib(n))