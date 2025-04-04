def ispangram(s):
    set1= set(s)
    for i in range(97,123):
        if not(chr(i) in set1):
            return "not a pangram"                 
    return "yes, it is a pangram "    
    
s = input("Enter a string in small alphabets: ")    
ans = ispangram(s)
print(ans)
