"""
a determinant is a scalar value which is a function of the entries of a square matrix
    det A = |A| = |a b| = ad -bc
                  |c d|
    
1. get the first value index from matrix
2. trim the column on which the value is found in the n+1 row
3., multiply the value with the remainder in the row

"""

matrix= [[4, 6], [3,8]]
cross_mult = []

# for index, value in enumerate(matrix[0]):
#     temp_matrix = matrix[1].pop(index)
#     cross_mult.append(value*temp_matrix)

# result = cross_mult[0] - cross_mult[1]
print(matrix[1])