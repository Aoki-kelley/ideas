import turtle
import mcpi.block as block

__all__ = ['draw_map_turtle', 'draw_dot_turtle', 'draw_pot_turtle', 'draw_map_mc']


def draw_map_turtle(width: int, pen: turtle.Pen):
    """
    绘制边长为width的方形
    """
    pen.up()
    pen.goto(-1, -1)
    pen.down()
    pen.hideturtle()
    pen.speed(10)
    pen.goto(0 - 1, width + 1)
    pen.goto(width + 1, width + 1)
    pen.goto(width + 1, 0 - 1)
    pen.goto(0 - 1, 0 - 1)
    pen.up()


def draw_dot_turtle(x, y, pen: turtle.Pen):
    """
    在(x,y)处打圆点
    """
    pen.hideturtle()
    pen.speed(10)
    pen.goto(x, y)
    pen.dot(3)


def draw_pot_turtle(x, y, pen: turtle.Pen, width=1):
    """
    以(x,y)为左下角点绘制边长为width的黑色实心方形
    """
    pen.hideturtle()
    pen.speed(10)
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.fillcolor('black')
    pen.begin_fill()
    pen.goto(x + width, y)
    pen.goto(x + width, y + width)
    pen.goto(x, y + width)
    pen.goto(x, y)
    pen.end_fill()


def draw_map_mc(width: int, mc):
    """
    在minecraft地图中绘制版图,边界为粉色玻璃
    """
    mc.setBlocks(0 - 1, -3, 0 - 1, width + 1, -3, 0 - 1, block.STAINED_GLASS.id, 6)
    mc.setBlocks(width + 1, -3, 0 - 1, width + 1, -3, width + 1, block.STAINED_GLASS.id, 6)
    mc.setBlocks(width + 1, -3, width + 1, 0 - 1, -3, width + 1, block.STAINED_GLASS.id, 6)
    mc.setBlocks(0 - 1, -3, width + 1, 0 - 1, -3, 0 - 1, block.STAINED_GLASS.id, 6)
