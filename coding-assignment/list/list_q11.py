#11. Get Even Numbers from a List
#Get all even numbers from the list [1, 2, 3, 4, 5, 6].

lst = [1, 2, 3, 4, 5, 6]
even_lst = [x for x in lst if x % 2 == 0]
print(even_lst)
