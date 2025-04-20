def rev_lst(lst ,i=-1):
    if -1*len(lst) == i :
        return [lst[i]]
    
    return [lst[i]] + rev_lst(lst, i-1)

lst = [2,6,45,8,421] 
reverse = rev_lst(lst,i=-1)
print(reverse)   

#OUTPUT:
# [421, 8, 45, 6, 2]  
