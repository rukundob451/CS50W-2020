def compute_sum(n):
    return sum([i / (i + 1) for i in range(1, n + 1)])


print(compute_sum(4))
print(compute_sum(55))
print(compute_sum(5))
