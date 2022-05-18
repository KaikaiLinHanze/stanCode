"""
File: draw a line
Name:Kai
-------------------------
TODO:This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
# CONSTANT
SIZE = 20

# global variable
window = GWindow(title='draw_line.py')
time = 0
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(point):
    """
    :param point: is a variable to memory the mouse
    :return: the movement of mouse click after two click.
    For the first click, there is a circle to memory the site.
    For the second click, there is a line.
    """
    global time
    # time is used to record how many time is clicked.
    if time % 2 == 0:
        window.add(circle, x=point.x - SIZE / 2, y=point.y - SIZE / 2)
    else:
        line = GLine(circle.x+SIZE / 2, circle.y+SIZE / 2, point.x, point.y)
        window.add(line)
        window.remove(circle)
    time += 1


if __name__ == "__main__":
    main()
