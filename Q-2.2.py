def binary_num(num,i=2):
    if num == 0:
        return ""
    return str(num % i) + binary_num(num//2,i=2)
    

num = int(input("Enter a number: "))
fun_ans = binary_num(num,i=2)

rev_ans = fun_ans[::-1]
print(rev_ans)    

#OUTPUT:
# Enter a number: 23
# 10111
