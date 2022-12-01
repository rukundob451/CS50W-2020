# Function to sort the words in alphabetical order
def sort_sentence(s):
    # split sentence into words using space delimiter
    word = s.split(" ")
    for i in range(len(word)):
        # convert all the words into lowercase
        word[i] = word[i].lower()
    s = sorted(word)
    print(' '.join(s))


# sentence to sort
sentence = input("Enter a sentence for sorting words:\n")

# function call
sort_sentence(sentence)
