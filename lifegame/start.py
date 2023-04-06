from lifegame import *
from copy import deepcopy
from setting import *
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
from draw import *
import turtle

# original_cell_dict = map_found(CELL_NUM, WIDTH, RATE, POSITIONS)  # 给定点生成
original_cell_dict = map_found(0, WIDTH, RATE)  # 随机生成
temp_cell_dict = deepcopy(original_cell_dict)
stable_limit = Stable_Limit  # 群体稳定后的迭代次数
count_list = []

while True:
    if DEBUG_MODE:
        judge = debugger(original_cell_dict, WIDTH)
        if not judge:
            break

    for pos, cell in original_cell_dict.items():
        new_cell = temp_cell_dict[pos]
        if cell.status == 0:
            if near_count(cell, original_cell_dict, WIDTH, 's+') >= 2 and near_count(cell, original_cell_dict,
                                                                                     WIDTH, 's') == 3:
                # 死细胞周围有繁殖意向的活细胞为2且周围有3个活细胞,该细胞诞生
                new_cell.status = 1
                if chance(RATE):
                    new_cell.breed_intention = 1
                else:
                    new_cell.breed_intention = 0
                near_list = near_list_found(pos, WIDTH)
                for near_pos in near_list:  # 以该细胞为中心创建死细胞
                    if near_pos not in temp_cell_dict:
                        temp_cell_dict[near_pos] = Cell(pos=near_pos, status=0)
        else:
            near_survivor_count = near_count(cell, original_cell_dict, WIDTH, 's')
            if near_survivor_count < 2 or near_survivor_count > 3:  # 活细胞周围活细胞数小于2或大于3,该细胞死亡
                new_cell.status = 0
                new_cell.breed_intention = -1
            else:
                if chance(RATE):
                    new_cell.breed_intention = 1
                else:
                    new_cell.breed_intention = 0
    count = 0
    for pos_n in list(temp_cell_dict.keys()):  # 删去多余的死细胞并统计活细胞数
        cell_n = temp_cell_dict[pos_n]
        if cell_n.status == 0:
            near_survivor_count = near_count(cell_n, temp_cell_dict, WIDTH, 's')
            if near_survivor_count == 0:
                del temp_cell_dict[pos_n]
        else:
            count += 1

    if len(count_list) <= stable_limit:
        count_list.append(count)
    if len(count_list) == stable_limit + 1:
        for value in count_list:
            if count_list.count(value) == stable_limit:
                stable_limit = 0
                break
        else:
            del count_list[0]

    original_cell_dict = deepcopy(temp_cell_dict)
    del temp_cell_dict
    temp_cell_dict = deepcopy(original_cell_dict)
    print('----------{0}个存活---------'.format(count))
    if count == 0:
        print('All cells died.')
        break
    '''else:
        for p, cell in original_cell_dict.items():
            print(p, cell, near_count(cell, original_cell_dict, 's+'))'''

    if TURTLE_MODE:
        pen = turtle.Pen()
        turtle.screensize(100, 100)
        pen.hideturtle()
        pen.up()
        draw_map_turtle(WIDTH, turtle.Pen())
        for pos_n, cell in original_cell_dict.items():
            if cell.status == 1:
                # draw_dot_turtle(pos_n[0], pos_n[1], pen)
                draw_pot_turtle(pos_n[0], pos_n[1], pen)
        pen.clear()

    if MINECRAFT_MODE:
        temp_pos = []
        try:
            mc = minecraft.Minecraft.create()
            draw_map_mc(WIDTH, mc)
            for pos, cell in original_cell_dict.items():
                if cell.status == 1:
                    mc.setBlock(pos[0], -3, pos[1], block.STAINED_GLASS.id, 3)  # 淡蓝色玻璃
                    temp_pos.append(pos)
            # mc.postToChat('-{0}个存活-'.format(count))
            time.sleep(0.6)
            if stable_limit != 0:
                for pos in temp_pos:
                    mc.setBlock(pos[0], -3, pos[1], block.GLASS.id)  # 版图内恢复为玻璃
                temp_pos.clear()
            else:
                mc.setBlocks(0 - 2, -3, 0 - 2, WIDTH + 2, -3, WIDTH + 2, block.GLASS.id)
                print("Minecraft's map cleaned.")
                mc.postToChat('Map cleaned.')
            del mc
        except ConnectionRefusedError:
            print('Connect Error')
            # /fill -240 1 -143 -176 1 -79 glass 0 minecraft:stained_glass 3 清图指令
    time.sleep(0.1)
    if stable_limit == 0:
        print('Stop.')
        break
