list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

onlyList1 = [i for i in list1 if i not in list2]
onlyList2 = [i for i in list2 if i not in list1]
union = onlyList1 + list2
# union = onlyList2 + list1 (hiçbir fark yok)

print(onlyList1)
print(onlyList2)
print(union)