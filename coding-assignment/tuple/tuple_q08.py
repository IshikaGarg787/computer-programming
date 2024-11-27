#8. Find the Sum of Even Indexed Elements in a Tuple
#Problem: Given the tuple (1, 2, 3, 4, 5, 6), find the sum of elements at even indexes.

t = (1, 2, 3, 4, 5, 6)
sum_even_indexes = sum(t[i] for i in range(len(t)) if i % 2 == 0)
print(sum_even_indexes)
