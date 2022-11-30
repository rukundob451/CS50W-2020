# Create an empty set
s = set()

# Add elements to the set
# sets cannot be accessed by an index
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)  # {1, 2, 3, 4}
# s cannot be subscripted.  The statement below produces a TypeError
# print(s[1])

s.add(3)  # is 3 in the set twice???
print(s)  # NO!!!  Only unique values are added.  {1, 2, 3, 4}

s.remove(2)
print(s)  # {1, 3, 4}
print(len(s))  # 3 elements in the set now.  The len() function works on all sequences
print(f"The set has {len(s)} elements.")  # 3 elements
