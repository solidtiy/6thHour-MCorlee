#Name:Misa
#Class: 6th Hour
#Assignment: HW11
import random
from typing import Any

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100


list = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

#3. Print the list.

print(list)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.

if list[0] >= list[1] and list[0] >= list[2]:
    print(f"{list[0]} is the biggest number.")
    largest = list[0]
elif list[1] >= list[0] and list[1] >= list[2]:
    print(f"{list[1]} is the biggest number.")
    largest = list[1]
elif list[2] >= list[0] and list[2] >= list[1]:
    print(f"{list[2]} is the biggest number.")
    largest = list[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".


#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if largest % 2 == 0:
    if largest % 3 == 0:
        print(f"{largest} is divisible by both 2 and 3")
    else:
        print(f"{largest} is divisible by 2 but not 3")
else:
    if largest % 3 == 0:
        print(f"{largest} is divisible by 3 but not 2")
    else:
        print(f"{largest} is divisible by neither")