"""
File: class_reviews.py
Name: Kai
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1
def main():
    """
    The user is asked to input the class name (either SC001 or SC101).
    If the user input -1 for class name, program would output the maximum, minimum, and average among all the inputs.
    """
    max01 = 0 #max number for sc001
    min01 = 0 #min number for sc001
    sum01 = 0 #sum for sc001
    max11 = 0 #max number for sc101
    min11 = 0 #min number for sc101
    sum11 = 0 #sum for sc101
    n01 = 0 #number for sc001
    n11 = 0 #number for sc101
    classtype = input("which class? or " + str(EXIT) + " to quit.").upper()
    if classtype == str(EXIT):
        print("No class scores were entered.")
    else:
        score = int(input("score:"))
        while True:
            if classtype == "SC001":
                if score > max01:
                    max01 = score
                if score < min01:
                    min01 = score
                n01 += 1
                sum01 += score
            if classtype == "SC101":
                if score > max11:
                    max11 = score
                if score < min11:
                    min11 = score
                n11 += 1
                sum11 += score
            classtype = input("which class? or " + str(EXIT) + " to quit.").upper()
            if classtype == str(EXIT):
                break
            else:
                score = int(input("score:"))
        print("==================SC001==================")
        if sum01 != 0:
            print("Max(001):"+str(max01)+"\nMin(001):"+str(max01)+"\nAvg(001):"+str(sum01/n01))
        else:
            print("No score for SC001")
        print("==================SC101==================")
        if sum11 != 0:
            print("Max(101):" + str(max11) + "\nMin(101):" + str(max11) + "\nAvg(101):" + str(sum11 / n11))
        else:
            print("No score for SC101")


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
