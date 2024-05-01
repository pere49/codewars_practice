"""
Function that returns true/false if argument:
    1. Has same nesting structure as first array
    2. Has corresponding length of nested arrays as first array

input -> output
ARRAY -> BOOL

Algorithm break down
1. Check the nesting structure of the first array -> check type(recursion)
2. Check structure of second element and compare
"""

def same_structure_as(arr1, arr2):
    if isinstance(arr1, list) and isinstance(arr2, list):
        if len(arr1) != len(arr2):
            return False
        for subarr1, subarr2 in zip(arr1, arr2):
            if not same_structure_as(subarr1, subarr2):
                return False
        return True
    else:
        return not isinstance(arr1, list) and not isinstance(arr2, list)
    
print(same_structure_as([1, 1, 1], [2, 2, 2]))  # True
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))  # True
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))  # False
print(same_structure_as([1, [1, 1]], [2, [2]]))  # False 
