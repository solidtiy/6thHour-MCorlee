#Name:Misa
#Class: 6th Hour
#Assignment: HW8
import random

#1. Import the "random" library

#2. print "Hello World!"

print("Hello World")

#3. Create three different variables that each randomly generate an integer between 1 and 10

rando_1 = random.randint(1, 10)
rando_2 = random.randint(1, 10)
rando_3 = random.randint(1, 10)
#4. Print the three variables from #3 on the same line.
print(rando_1, rando_2, rando_3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
rando_math = rando_1 + 2
rando_math2 = rando_2 - 4
rando_math3 = rando_3 * 1.5
#6. Print each result from #5 on the same line.

print(rando_math, rando_math2, rando_math3)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6

list = [ random.randint(1,6) , random.randint(1,6) , random.randint(1,6) , random.randint(1,6) ]
#8. Sort the list in #7 and print it.

list.sort()
print(list)
#9. Add together the highest three numbers in the list from #7 and print the result.

# I dont know how to do this but im sickan dont have the energy sorry:(

#10. Create a list with 5 names of other students in this class and print the list.
names = [ "Misa" , "Owyn" , "Braylee" , "Matthew"]

print(names)
#11. Shuffle the list in #10 and print the list again.

random.shuffle(names)

#12. Print a random choice from the list of names from #10.

names2 = random.choice(names)

print(names2)