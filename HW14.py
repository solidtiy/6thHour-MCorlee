#Name: Misa
#Class: 6th Hour
#Assignment: HW14
import random
import time

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.

i = 5
while i <= 5:
    print(i)
    i -=1
    if i<0:
        print("Hello World")
        break

#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).

t = 1
while t <= 30:
    t +=1
    if t % 2 == 0:
        print(t)

#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.

r = 1
while r <= 30:
    r +=1
    if r % 3 == 0:
        print(r)

#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.


m=random.randint(1,6)
print(m)
while m!=1:
    m = random.randint(1, 6)
    print(m)

#5. Create a while loop that asks for a number input until the user inputs the number 0.

print("Give a Number")
while int(input())>0:
    int(input())
    if int(input())!=0:
        print("Give a Number")
    if int(input())==0:
        break
