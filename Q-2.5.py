def calculate(a , b):
    if b ==1:
        return a
    return a * calculate(a,b-1)

a = int(input("Enter the base number: "))
b = int(input("Enter the power number: "))
c = calculate(a,b)
print(c)

#OUTPUT:
# Enter the base number: 3
# Enter the power number: 6
# 729   
