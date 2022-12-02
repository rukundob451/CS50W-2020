def listToString(s):
    str1 = ""
    return (str1.join(s))


aString = input("Enter a string: ")

my_list = []

for x in range(len(aString)):
    # modulus 2 function test
    if x % 2 == 0:
        my_list.append(aString[x])
print(listToString(my_list))
