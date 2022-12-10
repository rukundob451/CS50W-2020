def compute_sum(n):
    return sum([i / (i + 1) for i in range(1, n + 1)])


n = int(input(("n: ")))  # input returns a string...must convert to int
# compute_sum returns float...need to convert to int to get answer
print(compute_sum(n))  # format to 3 decimal places
# some other examples
print(compute_sum(55))
print(compute_sum(533))
