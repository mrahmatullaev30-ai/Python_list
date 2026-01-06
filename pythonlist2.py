set1 = {'olma', 'anor', 'youtube', 'instagram', 'gilos'}
set2 = {'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
set3 = {'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

umumiy = set1.intersection(set2)

result = umumiy.difference(set3)

print(result)