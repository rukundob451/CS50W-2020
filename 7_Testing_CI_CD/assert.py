def square(x):
    return x * x


print(square(10) == 100)  # True
print(square(10) == 101)  # False

# assertions
assert(square(10) == 100)  # no output
assert(square(10) == 101)  # AssertionError thrown
