def move_zeros(lst):
    zeros = [0] * lst.count(0)
    while 0 in lst:
        lst.remove(0)
    return lst + zeros

def move_zeros(lst):
    zeros = [lst.pop(index) for index, value in enumerate(lst) if value == 0]
    return lst + zeros

print(move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))