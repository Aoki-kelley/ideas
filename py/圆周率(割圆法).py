def pi():
    i = 0
    p = 0
    length = 2 ** 0.5
    n = 1
    while i < 15:
        length = (2 - (4 - length ** 2) ** 0.5) ** 0.5
        p = length * 2 ** (n + 1)
        n += 1
        i += 1
    return p


arr = eval(input('计算次数:'))
pi_arr = 0
for j in range(arr):
    pi_arr += pi()
print(pi_arr / arr)
