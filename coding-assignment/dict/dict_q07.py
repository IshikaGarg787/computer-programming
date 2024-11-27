#8. Find the Key with the Second Highest Value
#Problem: Find the key with the second-highest value in a dictionary.

d = {'a': 10, 'b': 20, 'c': 30, 'd': 25}
sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
second_highest_key = sorted_items[1][0]
print(second_highest_key)
