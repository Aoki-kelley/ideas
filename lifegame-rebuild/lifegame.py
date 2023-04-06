# python 3.9.7
# auther: K
# date: 4/6, 2023

import time
from random import sample
from copy import deepcopy


def timer(func):
    """计时装饰器"""

    def inner():
        t1 = time.time()
        func()
        t2 = time.time()
        print("Timer:", t2 - t1)

    return inner


class LifeGameMap:
    height = 0
    length = 0
    boundary = False  # 是否无视边界
    cell_map = list()
    count = [0, 0]  # 前为生,后为死

    def __init__(self, height, length, boundary=False):
        self.height = height
        self.length = length
        self.boundary = boundary

        for i in range(height):
            tmp_list = [0 for _ in range(length)]
            self.cell_map.append(tmp_list)

    def random_map(self, n):
        """在版图内随机产生 n 个活细胞"""
        n = min(n, self.height * self.length)
        self.count[0] = n
        self.count[1] = self.height * self.length - self.count[0]

        pos_list = sample([(i, j) for i in range(self.height) for j in range(self.length)], n)
        for p in pos_list:
            self.cell_map[p[0]][p[1]] = 1

    def clear_map(self):
        """版图清空"""
        self.cell_map = list()
        for i in range(self.height):
            tmp_list = [0 for _ in range(self.length)]
            self.cell_map.append(tmp_list)

    def get_str(self, alive='1', dead='0'):
        s = ""
        for i in range(self.height):
            tmp_s = ""
            for j in range(self.length):
                if self.cell_map[i][j] == 1:
                    tmp_s += alive
                else:
                    tmp_s += dead
            s += (tmp_s + '\n')
        return s

    def get_map(self):
        return self.cell_map

    def get_up(self, x, y):
        """竖为x,横为y"""
        if x - 1 < 0:
            if self.boundary:
                x = self.height
            else:
                return 0
        return self.cell_map[x - 1][y]

    def get_down(self, x, y):
        """竖为x,横为y"""
        if x + 1 > self.height - 1:
            if self.boundary:
                x = 0 - 1
            else:
                return 0
        return self.cell_map[x + 1][y]

    def get_left(self, x, y):
        """竖为x,横为y"""
        if y - 1 < 0:
            if self.boundary:
                y = self.length
            else:
                return 0
        return self.cell_map[x][y - 1]

    def get_right(self, x, y):
        """竖为x,横为y"""
        if y + 1 > self.length - 1:
            if self.boundary:
                y = 0 - 1
            else:
                return 0
        return self.cell_map[x][y + 1]

    def get_up_right(self, x, y):
        """竖为x,横为y"""
        if x - 1 < 0:
            if self.boundary:
                x = self.height
            else:
                return 0
        if y + 1 > self.length - 1:
            if self.boundary:
                y = 0 - 1
            else:
                return 0
        return self.cell_map[x - 1][y + 1]

    def get_down_right(self, x, y):
        """竖为x,横为y"""
        if x + 1 > self.height - 1:
            if self.boundary:
                x = 0 - 1
            else:
                return 0
        if y + 1 > self.length - 1:
            if self.boundary:
                y = 0 - 1
            else:
                return 0
        return self.cell_map[x + 1][y + 1]

    def get_up_left(self, x, y):
        """竖为x,横为y"""
        if x - 1 < 0:
            if self.boundary:
                x = self.height
            else:
                return 0
        if y - 1 < 0:
            if self.boundary:
                y = self.length
            else:
                return 0
        return self.cell_map[x - 1][y - 1]

    def get_down_left(self, x, y):
        """竖为x,横为y"""
        if x + 1 > self.height - 1:
            if self.boundary:
                x = 0 - 1
            else:
                return 0
        if y - 1 < 0:
            if self.boundary:
                y = self.length
            else:
                return 0
        return self.cell_map[x + 1][y - 1]

    def get_count(self):
        return self.count

    def generate(self):
        """迭代"""
        cell_map_copy = deepcopy(self.cell_map)
        count = [self.count[0], self.count[1]]

        for x in range(self.height):
            for y in range(self.length):
                alive_count = self.get_up(x, y)
                alive_count += self.get_down(x, y)
                alive_count += self.get_left(x, y)
                alive_count += self.get_right(x, y)
                alive_count += self.get_up_right(x, y)
                alive_count += self.get_down_right(x, y)
                alive_count += self.get_up_left(x, y)
                alive_count += self.get_down_left(x, y)

                if alive_count == 3:
                    if cell_map_copy[x][y] == 0:
                        count[0] += 1
                        count[1] -= 1
                    cell_map_copy[x][y] = 1
                elif alive_count == 2:
                    continue
                else:
                    if cell_map_copy[x][y] == 1:
                        count[0] -= 1
                        count[1] += 1
                    cell_map_copy[x][y] = 0

        self.cell_map = deepcopy(cell_map_copy)
        self.count = [count[0], count[1]]

    def mult_generate(self, n):
        """多步迭代"""
        while n > 0:
            self.generate()
            n -= 1


@timer
def start():
    lifegame_map = LifeGameMap(100, 100, False)
    lifegame_map.random_map(2000)

    lifegame_map.mult_generate(1)
    print(lifegame_map.get_count())


if __name__ == "__main__":
    start()
