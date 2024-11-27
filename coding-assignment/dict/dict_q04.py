#4. Invert a Dictionary
#Problem: Create a new dictionary that inverts the keys and values of the given dictionary.

d = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in d.items()}
print(inverted)
