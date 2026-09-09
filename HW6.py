#Name:Misa
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(number_list)

#2. Sort the list from highest to lowest.

number_list.sort()
print(number_list)

#3. Create an empty list.

empty_list = []
print(empty_list)

#4. Remove the median number from the first list and add it to the second list.

number_list.pop(4)
print(number_list)
empty_list.append(5)
print(empty_list)


#5. Remove the first number from the first list and add it to the second list.

number_list.pop(0)
print(number_list)
empty_list.append(0)
print(empty_list)

#6. Print both lists.

print(number_list)
print(empty_list)

#7. Add the two numbers in the second list together and print the result.

empty_list_sum = empty_list[0] + empty_list[1]
print(empty_list_sum)

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

empty_list.remove(0)
empty_list.remove(5)

number_list.append(0)
number_list.append(5)

print(number_list)
print(empty_list)
#9. Sort the first list from lowest to highest and print it.

number_list.sort()
print(number_list)