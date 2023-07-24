# 实数矩阵运算


ROUND = 8


def matrix_random(x, y, min_v, max_v):
    # 随机生成矩阵(整数) x为行,y为列
    from random import randint
    return [[randint(min_v, max_v) for _i in range(y)] for _j in range(x)]


def matrix_minor(a, x, y):
    # 余子行列式
    result = []
    tmp = -1
    for i in range(len(a)):
        if i == x:
            continue
        result.append([])
        tmp += 1
        for j in range(len(a[0])):
            if j == y:
                continue
            result[tmp].append(a[i][j])

    return result


def matrix_det(a):
    # 矩阵行列式求值
    result = 0
    if len(a) == 1:
        result = a[0][0]
    elif len(a) == 2:
        result = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    else:
        # for i in range(len(a[0])):
        #     result += (-1) ** (0 + i) * a[0][i] * matrix_det(matrix_minor(a, 0, i))

        cal_list = []
        for i in range(len(a[0])):
            cal_list.append([a[0][i] * (-1) ** (0 + i), matrix_minor(a, 0, i)])
        while len(cal_list[0][1]) != 2:
            new_cal_list = []
            for i in range(len(cal_list)):
                sub_cal_list = cal_list[i]
                for j in range(len(sub_cal_list[1])):
                    new_cal_list.append([sub_cal_list[1][0][j] * (-1) ** (0 + j) * sub_cal_list[0],
                                         matrix_minor(sub_cal_list[1], 0, j)])
            cal_list = new_cal_list

        for i in range(len(cal_list)):
            result += cal_list[i][0] * (
                    cal_list[i][1][0][0] * cal_list[i][1][1][1] - cal_list[i][1][1][0] * cal_list[i][1][0][1]
            )

    return result


def matrix_t(a):
    # 转置
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def matrix_diag(_l):
    # 对角矩阵
    result = []
    for i in range(len(_l)):
        result.append([])
        for j in range(len(_l)):
            if j == i:
                result[i].append(_l[i])
            else:
                result[i].append(0)

    return result


def matrix_adj(a):
    # 伴随矩阵
    result = [[] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[j].append(round((-1) ** (i + j) * matrix_det(matrix_minor(a, i, j)), ROUND))

    return result


def matrix_inv(a):
    # 逆矩阵
    det_a = matrix_det(a)
    if det_a == 0:
        return

    return matrix_multi_number(matrix_adj(a), 1 / det_a)


def matrix_add(a, b):
    # 加法
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(round(a[i][j] + b[i][j], ROUND))

    return result


def matrix_sub(a, b):
    # 减法
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(round(a[i][j] - b[i][j], ROUND))

    return result


def matrix_multi(a, b):
    # 乘法
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(b[0])):
            tmp = 0
            for k in range(len(a[0])):
                tmp += a[i][k] * b[k][j]
            result[i].append(round(tmp, ROUND))

    return result


def matrix_multi_number(a, n):
    # 数乘
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(round(a[i][j] * n, ROUND))

    return result


def matrix_div(a, b):
    # 除法 a/b
    return matrix_multi(a, matrix_inv(b))


if __name__ == "__main__":
    import time
    import numpy as np

    a_arr = matrix_random(6, 6, 0, 9)
    # a_arr = [[1, 2, 3], [1, 0, -1], [0, 1, 1]]
    b_arr = matrix_random(6, 6, 0, 9)
    print("a_arr: \n", a_arr)
    print("b_arr: \n", b_arr)
    print("ret: ")
    t1 = time.time()
    print(" ", matrix_div(a_arr, b_arr))
    t2 = time.time()
    print("time1: ", t2 - t1)
    t1 = time.time()
    print(np.dot(np.mat(a_arr), np.mat(b_arr).I))
    # print(np.mat(a_arr).I)
    t2 = time.time()
    print("time2: ", t2 - t1)
