set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}


umumiy = sum(set1.intersection(set2))

only_set1 = sum(set1.difference(set2))

result = umumiy - only_set1
print(result)