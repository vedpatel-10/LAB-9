def count_lower_upper(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count = upper_count+1
        elif i.islower():
            lower_count = lower_count + 1  
    s ={"upper case": upper_count , "lower case": lower_count}
    return s      

s = input("Enter a string: ")
print(count_lower_upper(s))   
