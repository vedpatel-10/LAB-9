def sum_avg(sub1,sub2,sub3,sub4,sub5):
    total_value = sub1 + sub2 +sub3 + sub4 + sub5
    average_value = total_value/5

    return total_value,average_value    


sub1 =int(input("subject 1: "))
sub2 = int(input("subject 2: "))
sub3 = int(input("subject 3: "))
sub4 = int(input("subject 4: "))
sub5 = int(input("subject 5: "))
print("Total and Average values are",sum_avg(sub1,sub2,sub3,sub4,sub5),"respectively")

#OUTPUT:
# subject 1: 77
# subject 2: 81
# subject 3: 90
# subject 4: 88
# subject 5: 59
# Total and Average values are (395, 79.0) respectively
