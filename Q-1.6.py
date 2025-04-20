def lst_num(begin,end):
    lst = []
    for i in range(begin,end+1):
        tpl =(i , i**2, i**3)
        lst.append(tpl)

    return lst 

end = int(input("Enter a number till max : "))
begin =1
print(lst_num(begin,end))       

#OUTPUT:
# Enter a number till max : 7
# [(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125), (6, 36, 216), (7, 49, 343)] 
