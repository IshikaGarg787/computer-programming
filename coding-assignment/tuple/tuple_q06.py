#6. Zip Two Lists into a Tuple
#Problem: Zip the lists [1, 2, 3] and ['a', 'b', 'c'] into a tuple of pairs.

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
zipped = tuple(zip(lst1, lst2))
print(zipped)
