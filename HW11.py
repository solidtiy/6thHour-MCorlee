#Name:Misa
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100

A= random.randint(1,10)
B= random.randint(1,10)
C= random.randint(1,10)
list= [A, B, C]

#3. Print the list.

print(list)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.

if A>B and A>C:
    print("A is the highest of the three numbers")
elif B>A and B>C:
    print("B is the highest of the three numbers")
else:
    print("C is the highest of the three numbers")

#5. Tie the result (the largest number) from #4 to a variable called "num".

if A>B and A>C:
    print(A)
elif B>A and B>C:
    print(B)
else:
    print(C)

num=C

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num%2==0:
    if num%2==0:
        print("num is divisible by 2")
    else:
        print("num is not divisible by 2")
elif num%3==0:
    if num%3==0:
        print("num is divisible by 3")
    else:
        print("num is not divisible by 3")