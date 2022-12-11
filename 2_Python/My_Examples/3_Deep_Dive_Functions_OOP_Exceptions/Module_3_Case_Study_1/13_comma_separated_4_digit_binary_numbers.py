# Get the input string
input_str = input("binary string: ")

# Split the input string into a list of binary numbers
binary_nums = input_str.split(',')

# Create a list to store the decimal numbers that are divisible by 5
divisible_nums = []

# Iterate over the list of binary numbers
for binary_num in binary_nums:
    # Convert the binary number to a decimal integer
    decimal_num = int(binary_num, base=2)

    # Check if the decimal integer is divisible by 5
    if decimal_num % 5 == 0:
        # Add the decimal integer to the list of divisible numbers
        divisible_nums.append(decimal_num)

# Print the list of divisible numbers as a comma-separated sequence
print(",".join(str(num) for num in divisible_nums))
