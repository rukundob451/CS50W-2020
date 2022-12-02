sentence = input("Sentence: ")

# count characters
print(f"There are {len(sentence)} characters in \"{sentence}\"")

# count digits
digit_count = 0
for ch in sentence:
    if ch.isdigit():
        digit_count += 1
print(f"There are {digit_count} digits in \"{sentence}\"")

# count non-digits
non_digit_count = 0
for ch in sentence:
    if not ch.isdigit():
        non_digit_count += 1
print(f"There are {non_digit_count} non-digits in \"{sentence}\"")

# count alpha characters
alpha_count = 0
for ch in sentence:
    if ch.isalpha():
        alpha_count += 1
print(f"There are {alpha_count} alpha characters in \"{sentence}\"")
