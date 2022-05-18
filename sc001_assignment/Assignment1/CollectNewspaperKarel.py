from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    TODO:
    """
    go_and_pick_beeper()


def go_and_pick_beeper():
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    while not on_beeper():
        move()
    pick_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    pick_beeper()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
