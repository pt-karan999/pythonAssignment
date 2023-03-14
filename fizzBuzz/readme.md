Test cases:
•	10
Output:-
FizzBuzz
1       
2       
Fizz    
4       
Buzz    
Fizz    
7       
8       
Fizz    
Buzz

•	15
Output:-
FizzBuzz
1       
2       
Fizz    
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
 
Approach
Iterate loop from 1 to n
For i in range(1,n+1):
•	if(i%3==0 and i%5==0):
•	            print("FizzBuzz")
•	        elif(i%3==0):
•	            print("Fizz")
•	        elif(i%5==0):
•	            print("Buzz")
•	        else:
•	            print(i)
