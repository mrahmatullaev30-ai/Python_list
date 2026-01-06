ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}

city = ali.intersection(vali)
print("Ikkala do'st ham borgan shaharlar:", city)


only_ali = ali.difference(vali)
print("Faqat Ali borgan shaharlar:", only_ali)
