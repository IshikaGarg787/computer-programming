#5. Find Common Keys Between Two Dictionaries
$Problem: Find the common keys between two dictionaries.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
common_keys = set(dict1) & set(dict2)
print(common_keys)
