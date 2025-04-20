def convert(s):
    lst1 = s.split(" ")
    set1 = set(lst1)
    lst2 = list(set1)
    lst2.sort()

    return " ".join(lst2)

s = input("Enter a string :")
print(convert(s)) 

#OUTPUT:
# Enter a string :lion is the king of jungle
# is jungle king lion of the
