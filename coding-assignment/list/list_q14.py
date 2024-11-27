#14. Rotate a List by N Positions
#Rotate the list [1, 2, 3, 4, 5] by 2 positions.

lst = [1, 2, 3, 4, 5]
n = 2
rotated_lst = lst[-n:] + lst[:-n]
print(rotated_lst)
