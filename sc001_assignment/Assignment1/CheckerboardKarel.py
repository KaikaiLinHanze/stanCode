from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    TODO:
    """
    if front_is_clear():
        fill_one_line()
        while left_is_clear():
            cross()
            to_the_end()
            detect_front_line()
            if on_beeper():
                save_move()
                save_move()
                fill_one_line()
            else:
                save_move()
                fill_one_line()
    else:
        if left_is_clear():
            turn_left()
            fill_one_line()
        else:
            put_beeper()
def detect_front_line():
    turn_left()
    save_move()
    if on_beeper():
        turn_around()
        save_move()
    else:
        turn_around()
        save_move()
        put_beeper()
    turn_right()
def turn_right():
    for i in range(3):
        turn_left()
def to_the_end():
    while front_is_clear():
        save_move()
def cross():
    if left_is_clear():
        turn_left()
        save_move()
        turn_left()
def fill_one_line():
    while front_is_clear():
        put_beeper()
        save_move()
        save_move()
    detect()
def save_move():
    if front_is_clear():
        move()
def detect():
    turn_around()
    save_move()
    if on_beeper():
        turn_around()
        save_move()
    else:
        turn_around()
        save_move()
        put_beeper()
def turn_around():
    for i in range(2):
        turn_left()
# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)