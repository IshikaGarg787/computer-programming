#19. Merge Two Lists Alternately
#Problem: Merge two lists [1, 2, 3] and [a, b, c] alternately to form [1, 'a', 2, 'b', 3, 'c'].

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
result = [None]*(len(lst1) + len(lst2))
result[::2] = lst1
result[1::2] = lst2
print(result)
