import random

arr = eval(input("计算次数:"))
points_number = eval(input("点数目:"))
in_range_points = 0
pi_arr = 0
for j in range(arr):
    for i in range(points_number):
        x = random.random()
        y = random.random()
        if (abs(x - 0.5) ** 2 + abs(y - 0.5) ** 2) <= (0.5 ** 2):
            in_range_points += 1
    pi_arr += (in_range_points / points_number) * 4
    in_range_points = 0
pi = pi_arr / arr
print('pi ≈ %f' % pi)
