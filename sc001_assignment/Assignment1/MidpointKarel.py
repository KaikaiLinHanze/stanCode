from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    TODO:
    """
    if not front_is_clear():
        put_beeper()
    else:
        fill_one_line()
        turn_around()
        erase()
def fill_one_line():
    while front_is_clear():
        move()
        put_beeper()
def erase():
    while on_beeper():
        pick_beeper()
        move()
        while on_beeper():
            move()
        turn_around()
        move()
    put_beeper()
def turn_around():
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
