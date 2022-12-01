# print numbers between 1000 and 3000 only if all digits are even
even_digit_list = []  # start with empty list

# start with 2000 because 1 is odd so ignore all numbers from 1000 to 1999
# for nums in range(2000, 3101):
# check that each digit is not even
# also, the end of the range needs to be 1 more than the end of the range to make sure end of range is tested

for i in range(2000, 3101):
    s = str(i)
    if all(int(c) % 2 == 0 for c in s):
        even_digit_list.append(s)

# join the resulting list elements, separating elements by commas
print(', '.join(map(str, even_digit_list)))
