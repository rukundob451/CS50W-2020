# Define a list of names
names = ["Harry", "Ron", "Hermione", "Ginny"]

print(names)
print(names[0])  # Harry
print(names[1])  # Ron
print(names[2])  # Hermione
print(names[3])  # Ginny

names.append("Draco")
print(names)
print(names[0])  # Harry
print(names[1])  # Ron
print(names[2])  # Hermione
print(names[3])  # Ginny
print(names[4])  # Draco

# sort the list of names
names.sort()
print(names)
print(names[0])  # Draco
print(names[1])  # Ginny
print(names[2])  # Harry
print(names[3])  # Hermione
print(names[4])  # Ron

