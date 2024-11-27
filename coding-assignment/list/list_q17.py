#17. Find the Largest Number in Each Sublist
#Find the largest number in each sublist of [[1, 2, 3], [4, 5], [6, 7, 8]].

lst = [[1, 2, 3], [4, 5], [6, 7, 8]]
largest_elements = [max(sublist) for sublist in lst]
print(largest_elements)
