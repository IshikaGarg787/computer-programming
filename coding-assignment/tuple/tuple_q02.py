#2. Remove Duplicate Elements from a Tuple
#Problem: Remove duplicates from the tuple (1, 2, 2, 3, 4, 4).

t = (1, 2, 2, 3, 4, 4)
t_unique = tuple(set(t))
print(t_unique)
