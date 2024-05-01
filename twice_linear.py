def dbl_linear(n):
    y = lambda x: [2 * x + 1, 3 * x + 1]
    u = [1]
    count = 0
    # n = 50
    while count < n:
        u = sorted(u)
        u.extend(y(u[count]))
        count+=1

    # u = list(set(u))
    print(u)

dbl_linear(30)
