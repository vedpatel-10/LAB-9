def list_sanitizer(lst,i=0):
    if i == len(lst)-1:
        if lst[i]> 0:
            return [lst[i]]
        elif lst[i]<=0:
            return [0] 

    if lst[i]> 0:
        return [lst[i]] + list_sanitizer(lst,i+1)
    elif lst[i]<=0:
        return [0] + list_sanitizer(lst,i+1)
    
lst = [234,-324,4324,-23,-23,-373,24,-32,234,-53,0]  
print("Sanitizing the list: ")
print(list_sanitizer(lst,i=0)) 

