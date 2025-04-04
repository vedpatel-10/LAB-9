def calculate_average(lst,i =0):
    if i == len(lst)-1:
        return lst[i]/len(lst)
    
    return lst[i]/len(lst) + calculate_average(lst, i+1)

import random

lst = [random.randint(1,11) for i in range(10)]
print(lst)
print("Average is :")
print(calculate_average(lst,i=0))

