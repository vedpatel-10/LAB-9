def lst_num(begin,end):
    lst = []
    for i in range(begin,end+1):
        tpl =(i , i**2, i**3)
        lst.append(tpl)

    return lst 

end = int(input("Enter a number till max : "))
begin =1
print(lst_num(begin,end))       