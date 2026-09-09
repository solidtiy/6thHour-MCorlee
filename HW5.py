#Name:Misa
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!

print("Hello World")

#1. Create a list with 5 strings containing 5 different names in it.

misas_alters = ["Alichine" , "Trixis" , "Jordan" , "Tara" , "Elliot"]

print(misas_alters)

#2. Append a new name onto the Name List.

misas_alters.append("Lula")

print(misas_alters)

#3. Print out the 4th name on the list.

print(misas_alters[4])

#4. Create a list with 4 different integers in it.

misas_alters_ages = [16 , 15, 17, 23]
print(misas_alters_ages)

#5. Insert a new integer into the 2nd spot and print the new list.

misas_alters_ages.insert(2 , 2000000)
print(misas_alters_ages)

#6. Sort the list from lowest to highest and print the sorted list.

misas_alters_ages.sort()
print(misas_alters_ages)

#7. Add the 1st three numbers on the sorted list together and print the sum.

added_ages = misas_alters_ages [1] + misas_alters_ages [2] + misas_alters_ages [3]
print(added_ages)

#8. Create a list with two strings, two variables, and two boolean values.

random_list = ["help" , "Dying" , 2 , 1 , True , False]

print(random_list)
#9. Create a print statement that asks the user to input their own index value for the list on #8.

random_list.append(input("Add a number"))

print(random_list)