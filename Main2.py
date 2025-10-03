# # TODO: Create a list of your favorite fruits

# favourite_fruits = ["Mango", "Strawberry", "Watermelon","Pineapple"]
# print(favourite_fruits)

# # TODO: Add a new fruit to the end of the list

# favourite_fruits.append("Ginger")
# print(favourite_fruits)

# # TODO: Remove the second fruit from the list

# del favourite_fruits[2] ou favourite_fruits.pop[2]
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



# # EXERCICE 3

# # TODO: Create a dictionary representing a person (name, age, city)

# person = {
#     "Name": "Jude",
#     "age":22,
#     "city": "Paris"
# }
# print(person)

# # TODO: Add a new key-value pair for the person's occupation
# person['occupation'] = "Acteur"
# print(person)

# # TODO: Update the person's age

# person["age"] = 23
# print(f'Son age est: {person["age"]}')

# # TODO: Remove the 'city' key-value pair

# del person["city"]
# print(person)


# # TODO: Print all keys, then all values
# print("Les clés :", person.keys())
# print("Les valeurs :", person.values())

# # TODO: Check if a specific key exists in the dictionary
# if "occupation" in person:
#     print("La clé 'occupation' existe bien dans le dictionnaire.")
# else:
#     print("La clé 'occupation' n'existe pas.")




# # Exercice 4

# # TODO: Create two sets of numbers

# numero= {12,14,23,25}
# chiffre = {1,2,3,4,}

# print(f'Les numéros sont : {numero},Les chiffres sont {chiffre}')

# # TODO: Find the union of the two sets

# union_set = numero.union(chiffre)
# print(f'Les numéro et chiffres sont {union_set}')


# # TODO: Find the difference between the first and second set

# intersection_set = numero.intersection(chiffre)
# print(intersection_set)
# difference_set = numero.difference(chiffre)
# print(difference_set)

# # TODO: Add a new element to one of the sets

# intersection_set.add(32)
# print(intersection_set)


# # TODO: Remove an element from one of the sets
# intersection_set.remove(32) 
# print(f'Intersection après suppression : {intersection_set}')

# # Print the results of each operation
# print(f'Union : {union_set}')
# print(f'Intersection : {intersection_set}')
# print(f'Différence : {difference_set}') 

#Exercice 5

# TODO: Create a list of dictionaries representing books (title, author, year)

book = [{
    "title" : "Moi",
    "author": "Jude",
    "Year": 2025
}]

print(book)

# TODO: Add a new book to the list

new_book = [{
    "title" : "Tu casses la tête",
    "author": "La flemme",
    "year": 2026
}]

book.append(new_book)
print(f'Les nouvelles listes sont : {book}')

# TODO: Sort the list of books by year

book.sort()

# TODO: Create a dictionary where keys are authors and values are lists of their books

# TODO: Print all books by a specific author

# Print the final nested data structure

