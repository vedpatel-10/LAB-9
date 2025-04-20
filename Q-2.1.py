def prime_factor(num, i=2):
    if num == 1 :
        return []
    elif num % i == 0:
        return [i] + prime_factor(num//i , i)
    return prime_factor(num, i+1)

num = int(input("Enter a number : "))
if num <=0:
    print("Enter positive number")
elif num == 1:
    print("1 is not prime")
else:
    print(prime_factor(num))

#OUTPUT:
# Enter a number : 17
# [17]  
