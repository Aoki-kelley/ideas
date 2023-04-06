WIDTH = 64  # 初始版图边长,int: WIDTH >= 4

RATE = 1  # 繁殖意向比,int or float: 0<=RATE<=1

CELL_NUM = 3  # 初始细胞数,int: CELL_NUM<=WIDTH**2-2WIDTH

POSITIONS = [(1, 1), (2, 2), (1, 2)]  # 点列表,若CELL_NUM设置则可忽略

Stable_Limit = 5  # 群体稳定后的迭代次数

MINECRAFT_MODE = False  # 在minecraft地图中绘制

TURTLE_MODE = False  # 在turtle画布中绘制

DEBUG_MODE = False  # debug模式

# (1)当前细胞为死亡状态时，当周围有3个存活细胞时，则迭代后该细胞变成存活状态(模拟繁殖)；若原先为生，则保持不变。
# (2)当前细胞为存活状态时，当周围的邻居细胞低于两个(不包含两个)存活时，该细胞变成死亡状态(模拟生命数量稀少)。
# (3)当前细胞为存活状态时，当周围有两个或3个存活细胞时，该细胞保持原样。
# (4)当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态(模拟生命数量过多)。
# ————百度百科
