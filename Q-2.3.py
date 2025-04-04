def vowel_count(s,i=0):
    if i+1 == len(s):
        if s[i]== "a" or s[i]=="e" or s[i]=="i" or s[i] == "o" or s[i] =="u":
            return 1 
        else:
            return 0
    if s[i]== "a" or s[i]=="e" or s[i]=="i" or s[i] == "o" or s[i] =="u":
        return (1 + vowel_count(s,i+1))
    else:
        return (0 + vowel_count(s,i+1))

s = input("Enter a string in small alphabets: ")
print(vowel_count(s,i=0))