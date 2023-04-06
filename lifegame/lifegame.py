import random


class Cell:
    breed_intention = -1  # 初始为-1,值可为-1,0,1;分别表示不可繁殖,无繁殖意向,有繁殖意向

    def __init__(self, pos: tuple, status: int):
        self.pos = pos  # (x,y)
        self.status = status  # 0&1,活&死

    def __str__(self):
        return "position<{pos}>,status<{status}>,intention<{intention}>".format(pos=self.pos,
                                                                                status=self.status,
                                                                                intention=self.breed_intention)


def near_list_found(pos: tuple, width: int) -> list:
    """
    :param width: 版图边界
    :param pos: 中心点
    :return: 返回中心点周围八个点的列表
    """
    x = pos[0]
    y = pos[1]
    l_1 = [-1, 0, 1]
    l_n = []
    for a in l_1:
        for b in l_1:
            x_n = x + a
            y_n = y - b
            if x_n in range(0, width + 1) and y_n in range(0, width + 1):
                l_n.append((x_n, y_n))
    l_n.remove(pos)
    return l_n


def map_found(cell_num: int, width: int, rate: int, positions=None) -> dict:
    """
    :param cell_num:起始个数，为0则随机
    :param width:版图宽度,4<width
    :param rate:繁殖意向比
    :param positions:为None则按cell_num进行,否则按positions提供的点坐标进行
    :return 返回细胞字典 dict:[(x1,y1):cell1,(x2,y2):cell2,...]
    """
    cell_dict = {}
    if not positions:
        if cell_num == 0:
            amount = random.randint(width, width ** 2 - width * 2)
        else:
            amount = abs(cell_num)
        print('*******初始{0}个存活*******'.format(amount))
        for i in range(amount):  # 版图中创建活细胞
            x = random.randint(1, width - 1)
            y = random.randint(1, width - 1)
            if (x, y) not in cell_dict.keys():
                _cell = Cell(pos=(x, y), status=1)
                if chance(rate):
                    _cell.breed_intention = 1
                else:
                    _cell.breed_intention = 0
                cell_dict[(x, y)] = _cell
    else:
        for pos in positions:
            if pos not in cell_dict.keys():
                _cell = Cell(pos=pos, status=1)
                if chance(rate):
                    _cell.breed_intention = 1
                else:
                    _cell.breed_intention = 0
                cell_dict[pos] = _cell
    pos_list = list(cell_dict.keys())
    for pos in pos_list:  # 以活细胞为中心创建死细胞
        near_list = near_list_found(pos, width=width)
        for near_pos in near_list:
            if near_pos not in cell_dict:
                cell_dict[near_pos] = Cell(pos=near_pos, status=0)
    return cell_dict


def chance(rate: int or float) -> bool:
    """
    :param rate: 0<=rate<1
    """
    x = random.random()
    if x < rate:
        return True
    else:
        return False


def near_count(__cell: Cell, cell_dict: dict, width: int, mode: str) -> int:
    """
    :param __cell: 中心细胞
    :param cell_dict: 全体细胞字典
    :param width: 版图边界
    :param mode: 计数模式,'s' or 's+' or 'd'
    :return: 中心细胞周围存活的细胞数
    """

    class ModeError(Exception):
        def __init__(self, wrong_mode):
            self.wrong_mode = wrong_mode

        def __str__(self):
            return "参数mode应为s,s+或d"

    count = 0
    pos = __cell.pos
    near_list = near_list_found(pos, width)
    for near_pos in near_list:
        if near_pos in cell_dict:
            if mode == 's+':
                if cell_dict[near_pos].status == 1 and cell_dict[near_pos].breed_intention == 1:
                    count += 1
            elif mode == 's':
                if cell_dict[near_pos].status == 1:
                    count += 1
            elif mode == 'd':
                if cell_dict[near_pos].status == 0:
                    count += 1
            else:
                raise ModeError(mode)
    return count


def debugger(cell_dict: dict, width: int) -> bool:
    """
    :param cell_dict: 全体细胞字典
    :param width: 版图边长
    :return: 无问题则True,反之则False
    """
    for pos, _cell in cell_dict.items():
        if pos != _cell.pos:
            print('{pos}处细胞位置参数不一致'.format(pos=pos))
            return False
        else:
            if near_count(_cell, cell_dict, width, 'd') == 0:
                print('{pos}处细胞周围缺失死细胞'.format(pos=pos))
                return False
        return True


if __name__ == '__main__':
    WIDTH = 20  # 初始版图边长,int: WIDTH >= 4
    RATE = 0.5  # 繁殖意向比,int or float: 0<=RATE<1
    CELL_NUM = 1  # 初始细胞数,int: CELL_NUM<=(WIDTH-1)**2
    POSITIONS = [(1, 1), (2, 2), (1, 2)]
    cell_d = map_found(CELL_NUM, WIDTH, RATE, POSITIONS)
    print(len(cell_d))
    for p, cell in cell_d.items():
        print(p, cell, near_count(cell, cell_d, WIDTH, 's+'))
