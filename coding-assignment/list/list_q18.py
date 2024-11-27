#18. Remove All Falsey Values from a List
#Remove all falsey values (None, 0, "", etc.) from the list [1, 0, None, 2, "", 3, False].

lst = [1, 0, None, 2, "", 3, False]
filtered_lst = [item for item in lst if item]
print(filtered_lst)
