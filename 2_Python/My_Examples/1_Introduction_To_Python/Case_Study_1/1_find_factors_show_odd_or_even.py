def find_factors(x):
    print("The factors of ", x, " are:")
    for i in range(1, x + 1):
        if x % i == 0:
            if i % 2 == 0:
                print(f"{i}:  Even Number")
            else:
                print(f"{i}:  Odd Number")


num = int(input("Find factors for what number? "))
find_factors(num)
