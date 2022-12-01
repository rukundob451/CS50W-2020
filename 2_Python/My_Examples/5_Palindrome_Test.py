def palindrome_test(sentence):
    return sentence[::-1] == sentence


sent = input("Sentence: ")
if palindrome_test(sent.lower()):
    print(f"{sent} is a palindrome!")
else:
    print(f"{sent} is not a palindrome!")
