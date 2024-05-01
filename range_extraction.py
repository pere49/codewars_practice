ls = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
final = []
temp = []

for index in range(0, len(ls)):
    if index != len(ls)-1 and ls[index+1] - ls[index] == 1:
        temp.extend([ls[index], ls[index+1]])
        continue

    final.append(f"{temp[0]}-{temp[-1]}") if len(set(temp)) > 2 else final.extend(temp) if len(set(temp)) == 2  else final.append(ls[index])
    temp.clear()

print(",".join(str(v) for v in final))