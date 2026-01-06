set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

teskari = (set1.difference(set2)).union(set2.difference(set1))

for i in sorted(teskari, reverse=True):
    print(i, end=" ")