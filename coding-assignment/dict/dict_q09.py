#10. Remove Keys from Dictionary
#Problem: Remove keys from a dictionary based on a condition (e.g., key length is greater than 1).

d = {'a': 1, 'abc': 2, 'def': 3, 'x': 4}
d = {k: v for k, v in d.items() if len(k) <= 2}
print(d)
