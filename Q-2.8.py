def len_string(s,i=0):
    if i == len(s)-1:
        return 1
    return 1 + len_string(s,i+1)

s = "Hello world"
print("length of the string is :")
print(len_string(s,i=0))

#OUTPUT:
# length of the string is :
# 11
