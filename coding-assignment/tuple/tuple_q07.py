#7. Create a Tuple of Tuples from a Range
#Problem: Create a tuple of tuples from a range of numbers. For example, for the range 0-4, create ((0, 1), (2, 3), (4, 5)).

t = tuple((i, i + 1) for i in range(0, 5, 2))
print(t)
