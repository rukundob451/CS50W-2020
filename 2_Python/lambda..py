people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# sort the list by name


def f(person):
    return person["name"]


# sort the dictionary by the person's name
# call the f function
print('Sorting using key = f, with the f function returning the dictionary sorted by keys')
print(people.sort(key=f))
print()
print("Sorting calling a lambda function to also sort by the name key")
# use lambda function
print("sort list of dictionaries by name")
people.sort(key=lambda person: person["name"])
print(people)
print()
print("sort list of dictionaries dict by house")
people.sort(key=lambda person: person["house"])
print(people)
