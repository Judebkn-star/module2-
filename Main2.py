# # TODO: Create a list of your favorite fruits

# favourite_fruits = ["Mango", "Strawberry", "Watermelon","Pineapple"]
# print(favourite_fruits)

# # TODO: Add a new fruit to the end of the list

# favourite_fruits.append("Ginger")
# print(favourite_fruits)

# # TODO: Remove the second fruit from the list

# del favourite_fruits[2]
# print(favourite_fruits)

# # TODO: Sort the list alphabetically
# favourite_fruits.sort()
# print(favourite_fruits)

# # TODO: Create a new list with the first three fruits

# three_fruits = favourite_fruits[:3]
# print(three_fruits)


# EXERCICE 2

# # # # Print the original list and the new list

# # TODO: Create a tuple with your favorite colors
# colors = ("blue", "green", "red","black","blue")
# print(colors)

# # TODO: Try to modify one of the colors (this should raise an error)
# # colors[1] = "yellow"
# # print(colors)

# # TODO: Count how many times a specific color appears in the tuple

# blue_count = colors.count("blue")
# print(blue_count)

# # TODO: Find the index of a specific color

# Index_colors = colors.index("green")
# print("L'index de green est :", Index_colors)

# # TODO: Create a new tuple by concatenating two existing tuples


# New_tuple = ("La" , "Mangue")

# # Concaténer les deux tuples
# Concatenate_tuple = New_tuple + colors
# print(Concatenate_tuple)


# Print the results of each operation



# EXERCICE 3

# TODO: Create a dictionary representing a person (name, age, city)

person = {
    "Name": "Jude",
    "age":22,
    "city": "Paris"
}
print(person)

# TODO: Add a new key-value pair for the person's occupation
person['occupation'] = "Acteur"
print(person)

# TODO: Update the person's age

person["age"] = 23
print(f'Son age est: {person["age"]}')

# TODO: Remove the 'city' key-value pair

del person["city"]
print(person)
# TODO: Print all keys, then all values



# TODO: Check if a specific key exists in the dictionary

# Print the final dictionary
