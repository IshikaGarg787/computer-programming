#5. Sort a Tuple of Tuples
#Problem: Sort the tuple ((2, 3), (1, 2), (3, 1)) based on the second element of each nested tuple.

t = ((2, 3), (1, 2), (3, 1))
sorted_t = sorted(t, key=lambda x: x[1])
print(sorted_t)
