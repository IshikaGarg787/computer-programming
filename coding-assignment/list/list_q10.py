#10. Find the Second Largest Element in a List
#Find the second largest element in the list [4, 1, 3, 2, 5].

lst = [4, 1, 3, 2, 5]
unique_lst = list(set(lst))
unique_lst.sort()
print(unique_lst[-2])
