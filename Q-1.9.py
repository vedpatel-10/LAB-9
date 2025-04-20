def count_alpha_digits(s):
    alpha_count = 0
    digit_count = 0
    for i in s:
        if i.isalpha():
            alpha_count = alpha_count + 1
        elif i.isdigit():
            digit_count = digit_count + 1    

    d1 = {"Alphabets":alpha_count , "Digits":digit_count}
    return d1

s = input("Enter a string : ")
print(count_alpha_digits(s))

#OUTPUT:
# Enter a string : I have 5 pencils and 2 erasers
# {'Alphabets': 22, 'Digits': 2} 
