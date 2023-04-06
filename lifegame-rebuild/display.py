# python 3.9.7
# auther: K
# date: 4/6, 2023

import numpy
import tkinter
from time import sleep
from PIL import Image, ImageTk
from lifegame import LifeGameMap


def enlarge2image(data, n):
    """将二维列表 data 放大 n 倍"""
    size = (len(data), len(data[0]))
    ret = [[-1] * size[1] * n for _ in range(size[0] * n)]

    for i in range(0, size[0] * n, n):
        for j in range(0, size[1] * n, n):
            v = data[i // n][j // n]
            for k in range(n):
                for m in range(n):
                    if v == 1:
                        ret[i + k][j + m] = 255
                    else:
                        ret[i + k][j + m] = 0
    return ret


class DisplayTk:
    flag_step = 0
    flag_mult = 0

    cell_num = 0  # 初始细胞数
    enlarge_num = 6  # 放大倍数
    lifegame_map = None
    windows = None
    canvas = None
    tk_image = None

    windows_size = []  # 窗口大小
    canvas_size = []  # 画布大小
    img_pos = []  # 图片位置

    def map2tk_image(self):
        """将版图转换为可显示的图片"""
        result = enlarge2image(self.lifegame_map.get_map(), self.enlarge_num)
        result = numpy.asarray(result, dtype=numpy.uint8)
        img = Image.fromarray(result)
        ret = ImageTk.PhotoImage(image=img)
        return ret

    def do_step(self):
        """单步迭代"""
        self.flag_mult = 0
        self.flag_step = not self.flag_step
        if self.flag_step:
            self.lifegame_map.generate()

            self.tk_image = self.map2tk_image()
            self.canvas.create_image(self.img_pos[0], self.img_pos[1], image=self.tk_image)
            self.canvas.update()

            self.flag_step = not self.flag_step

    def do_mult(self):
        """连续迭代"""
        self.flag_step = 0
        self.flag_mult = not self.flag_mult
        while self.flag_mult:
            self.lifegame_map.generate()

            self.tk_image = self.map2tk_image()
            self.canvas.create_image(self.img_pos[0], self.img_pos[1], image=self.tk_image)
            self.canvas.update()
            sleep(0.05)

    def map_remark(self):
        """地图重置"""
        self.flag_step = 0
        self.flag_mult = 0
        self.lifegame_map.clear_map()
        self.lifegame_map.random_map(self.cell_num)

        self.tk_image = self.map2tk_image()
        self.canvas.create_image(self.img_pos[0], self.img_pos[1], image=self.tk_image)
        self.canvas.update()

    def windows_kill(self):
        """关闭窗口"""
        self.flag_step = 0
        self.flag_mult = 0
        sleep(0.05)
        self.windows.destroy()

    def __init__(self, windows_size, canvas_size, img_pos):
        self.windows_size = windows_size
        self.canvas_size = canvas_size
        self.img_pos = img_pos

        self.windows = tkinter.Tk(className="lifegame")
        self.windows.geometry("{0}x{1}".format(windows_size[0], windows_size[1]))
        self.canvas = tkinter.Canvas(self.windows, width=canvas_size[0], height=canvas_size[1], bg='lightgray')
        self.canvas.pack()

        tkinter.Button(self.windows, command=self.do_step, text="单步迭代").place(x=windows_size[1] / 2 - 120,
                                                                              y=windows_size[1] - 40)
        tkinter.Button(self.windows, command=self.do_mult, text="持续迭代").place(x=windows_size[1] / 2 - 40,
                                                                              y=windows_size[1] - 40)
        tkinter.Button(self.windows, command=self.map_remark, text="重新生成").place(x=windows_size[1] / 2 + 40,
                                                                                 y=windows_size[1] - 40)
        tkinter.Button(self.windows, command=self.windows_kill, text="关闭窗口").place(x=windows_size[1] / 2 + 120,
                                                                                   y=windows_size[1] - 40)

    def map_init(self, height, length, boundary, n):
        self.cell_num = n
        self.lifegame_map = LifeGameMap(height, length, boundary)
        self.lifegame_map.random_map(n)

        self.tk_image = self.map2tk_image()
        self.canvas.create_image(self.img_pos[0], self.img_pos[1], image=self.tk_image)

    def display(self):
        self.windows.mainloop()


def start():
    display_tk = DisplayTk(windows_size=[700, 700], canvas_size=[650, 650], img_pos=[325, 325])
    display_tk.map_init(100, 100, True, 2000)

    display_tk.display()


if __name__ == "__main__":
    start()
