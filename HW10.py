#Name:Misa
#Class: 6th Hour
#Assignment: HW10

import random

#1. Print "Hello World!"

print("Hello World")

#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.

A= random.randint(1,10)
B= random.randint(1,10)
C= random.randint(1,10)

#3. Print A, B, and C on the same line.

print(A,B,C)

#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.

if A>5:
    print("A is greater than five")
elif A<5:
    print("A is less than five")
else:
    print("A is equal to five")

#5. Make an if statement that prints if variable B is between 3 and 7, or not.

if B>3 and B<7:
    print("B is between 3 and 7")

#6. Make an if statement that prints if variable C is even or odd.

if C % 2 == 0:
    print("C is even")
else:
    print("C is odd")


#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20

new_random= random.randint(1,20)

addidion= 3 + new_random
print(addidion)

#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.

if addidion>A+B+C:
    print("addidion is greater than A+B+C all together")
elif addidion<A+B+C:
    print("addidion is less than A+B+C all together")
else:
    print("addidion is equal to A+B+C")