keypad = [["1","2","3"],
        ["4","5","6"],
        ["7","8","9"],
        ['#',"0",'#']]

"""
1. Check the horizontal adjacent values
2. Check the vertical values
3. loop through string
4. replace every value with adjacent values
5. Perform permutation on list
"""
pin = "336"
combinations = []
for i, num in enumerate(pin):
    row_index = int(int(num)//3.5) if num !='0' else 3
    row = keypad[row_index]
    index = row.index(num)
    horizontal = [row[index+1]] if index==0 else [row[0], row[-1]] if index==1 else [row[index-1]]
    vertical = [keypad[row_index+1][index]] if row_index==0 else [keypad[row_index+1][index], keypad[row_index-1][index]] if row_index==1 or row_index==2 else [keypad[row_index-1][index]]
    adjacent = vertical+horizontal
    adjacent.append(num)
    combinations.append([adj for adj in adjacent if adj!= "#"])

# Permutation
while len(combinations) > 1:
    x_com = combinations[0]
    y_com = combinations[1]
    res = []
    for x in x_com:
        for y in y_com:
            res.append(x + y)
    combinations[0] = res
    combinations.pop(1)
print(combinations[0])
# print(keypad[:][:2])