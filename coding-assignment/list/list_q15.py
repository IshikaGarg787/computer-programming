#15. Find the Difference Between Two Lists
#Find the elements in the first list but not in the second list.

lst1 = [1, 2, 3]
lst2 = [2, 3, 4]
print(list(set(lst1) - set(lst2)))
