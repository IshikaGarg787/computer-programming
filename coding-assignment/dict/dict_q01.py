#Merge Dictionaries with Different Keys
#Problem: Write a function that merges two dictionaries with potentially different keys. If the keys are different, the function should preserve both dictionaries and their key-value pairs.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merge_dicts(dict1, dict2)  # Returns: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
