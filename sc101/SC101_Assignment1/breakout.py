"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 50 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    if lives > 0:
        while True:     # Add animation loop here!
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            brick_count = graphics.get_brick_count()
            pause(FRAME_RATE)
            graphics.ball.move(dx, dy)
            graphics.hit_wall()
            graphics.probe_check()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                if lives == 0:
                    break
                else:
                    graphics.set_ball()
            if brick_count == 0:    # Close the game
                break
        graphics.set_ball()


if __name__ == '__main__':
    main()
