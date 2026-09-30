#Name:Misa
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!

print("Hello World")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.

alters_and_ages = {
    "Alter_one" : "Venue",
    "Alter_two" : "Alichine",
    "Ages" : [14,16,15]
}


#3. Print the keys of the dictionary from #2.

print(alters_and_ages.keys())

#4. Print the values of the dictionary from #2

print(alters_and_ages.values())

#5. Print one of the three numbers from the list by itself
print(alters_and_ages["Ages"][2])

#6. Using the update function, add a fourth key to the dictionary and give it a value.

alters_and_ages.update({"Alter_three" : "Trixis"})

#7. Print the entire dictionary from #2 with the updated key and value.

print(alters_and_ages)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.

my_classmates = {
    "classmateone" : {
        "Name" : "Braylee",
        "Grade" : 12,
        "Female" : True,
    },
    "classmatetwo" : {
        "Name" : "Owyn",
        "Grade" : 9,
        "Female" : False,
    },
    "classmatethree" : {
        "Name" : "Cody",
        "Grade" : 9,
        "Female" : True,
    },
}

print(my_classmates)

#9. Print the names of all three classmates on the same line.

print(my_classmates["classmateone"]["Name"] , my_classmates["classmatetwo"]["Name"] , my_classmates["classmatethree"]["Name"])

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.

my_classmates.pop("classmatetwo")
print(my_classmates)