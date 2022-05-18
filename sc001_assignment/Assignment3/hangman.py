"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


# def main():
#     """
#     TODO:
#     """
#     ans = random_word()
#     show = len(ans)*"-"
#     print("the answer is "+str(show))
#     hang_man(ans)
# def hang_man(ans):
#     life = N_TURNS
#     show = len(ans) * "-"
#     while True:
#         guess = input("your guess word is").upper()
#         output = ""
#         if guess in ans:
#             for i in range(len(ans)):
#                 if guess == ans[i]:
#                     output += ans[i]
#                 else:
#                     output += show[i]
#             print("you are correct")
#         show = output
#         if show == ans:
#             print("you won the answer is" + str(ans))
#             break
#         elif life == 0:
#             print("you are totally hang. the word was" + str(ans))
#             break
#         else:
#             life -= 1
#             print("there is no "+ str(guess) + "'s in the word \n you have"+ str(life))
#         print(show)

def main():
    ans = random_word()
    show = len(ans) * "-"
    print(show)
    hang_man (ans, show)
def hang_man(ans, show):
    life = N_TURNS
    while True:
        guess = input("your guess word:").upper()
        if guess.isalpha() is False:
            print("Illegal input")
        else:
            correct = ""
            if guess in ans:
                for i in range(len(ans)):
                    if guess == ans[i]:
                        correct += guess
                    else:
                        correct += show[i]
                show = correct
                print("YOU ARE CORRECT \n remain word is" + str(show))
            else:
                life -= 1
                print("THERE WAS NO " +str(guess) + " in the word \n please guess again"+ str(show) + "YOU HAVE "+str(life))
            if correct == ans:
                print("YOU WIN! THE CORRECT ANSWER WAS " + ans)
                break
            if life == 0:
                print("YOU ARE HANGED! THE CORRECT ANSWER WAS " + ans)
                break



def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
