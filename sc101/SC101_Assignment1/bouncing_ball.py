"""
File: bouncing ball
Name:Kai
-------------------------
TODO:This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
# CONSTANT
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global variable
time = 0


ball = GOval(SIZE, SIZE)
ball.filled = True
window = GWindow(800, 500, title='bouncing_ball.py')
window.add(ball, START_X + 1 / 2 * SIZE, START_Y + 1 / 2 * SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(ball_bounce)


def ball_bounce(click):
    """
    :param click: use to start the beginning of the event
    :return: using the global ball to fix the object into the unique one, and return the bouncing ball.
    """
    global time
    # time is used to record click times
    if time <= 2 and ball.y == START_Y + 1 / 2 * SIZE:
        # if the ball is not at the right way, the event of the mouse will be ignored
        bounce = 0
        time += 1
        while True:
            bounce += GRAVITY
            ball.move(VX, bounce)
            if ball.y >= window.height - SIZE and bounce > 0 :
                bounce *= -REDUCE
            if ball.x + SIZE >= window.width:
                break
            pause(DELAY)
        window.add(ball, START_X + 1 / 2 * SIZE, START_Y + 1 / 2 * SIZE)


if __name__ == "__main__":
    main()
