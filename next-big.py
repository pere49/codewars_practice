def next_bigger(n):
    n_split = [int(num) for num in str(n)]
    print(n_split[-2:])

val = 12
result = next_bigger(val)
print(result)