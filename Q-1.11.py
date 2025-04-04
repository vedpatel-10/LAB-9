def create_list(lst1,lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    set3 = set1 & set2

    return set3

lst1 = [23,534,5,545574,94657,56,42,6,0,42,2555,863,35]
lst2 = [23,35,234,4534,545,"fggf",545574]
print(create_list(lst1,lst2))   