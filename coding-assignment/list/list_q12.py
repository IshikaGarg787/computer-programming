#12. Flatten a Nested List
#Flatten the nested list [1, [2, 3], [4, [5, 6]]].

lst = [1, [2, 3], [4, [5, 6]]]
flat_lst = []
for item in lst:
    if isinstance(item, list):
        for sub_item in item:
            if isinstance(sub_item, list):
                flat_lst.extend(sub_item)
            else:
                flat_lst.append(sub_item)
    else:
        flat_lst.append(item)
print(flat_lst)
