def create_array(x, y, z, value):
    array = [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]
    return array

array_3d = create_array(3, 4, 5, 7)

for i in range(len(array_3d)):
    for j in range(len(array_3d[i])):
        print(array_3d[i][j])
    print()  

#OUTPUT:
# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]     

# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]

# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]
# [7, 7, 7, 7, 7]
