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
