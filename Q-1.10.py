def frequency(s):
    lst = s.split()
    freq_dict = {}
    for i in lst:
        count = s.count(i)
        d1 = { i : count}
        freq_dict = {**freq_dict, **d1}
    
    return sorted(freq_dict.items())

s = input("Enter a string of words in small alphabets : ")
print(frequency(s))

#OUTPUT:
# Enter a string of words in small alphabets : apple a day, keeps the doctor away
# [('a', 5), ('apple', 1), ('away', 1), ('day,', 1), ('doctor', 1), ('keeps', 1), ('the', 1)] 
