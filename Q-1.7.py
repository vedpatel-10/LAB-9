def ispalindrome(s):
    s1 = s.lower()
    count = 0
    for i in range(0,len(s1)//2):
        if s1[i]== " ":
            continue
        if s1[i] == s1[-1*(i+1)]:
            count = count +1 

    if count == len(s1)//2:
        return "Yes, it is a palindrome"
    else:
        return "No, it is not a palindrome"        

s  = input("Enter a string: ")
print(ispalindrome(s))

#OUTPUT:
# Enter a string: malayalam
# Yes, it is a palindrome
