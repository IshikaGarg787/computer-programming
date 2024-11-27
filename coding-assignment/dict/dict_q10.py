#12. Remove Duplicates in a List of Dictionaries
#Problem: Remove duplicate values in a list of dictionaries based on a key.

dictionaries = [{'a': 1, 'b': 2}, {'a': 1, 'b': 3}, {'a': 2, 'b': 2}]
seen = set()
result = []
for d in dictionaries:
    key = tuple(d.items())  
    if key not in seen:
        seen.add(key)
        result.append(d)
print(result)
