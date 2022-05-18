"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    """
    data = input("Please give me a dna string and I will find the complement :").upper()
    complement(data)
def complement(data):
    if not data.isdigit:
        print("illegal inputting")
    else:
        ans = ""
        for i in range(len(data)):
            ch = data[i]
            if ch == "A":
                ans += "T"
            elif ch == "T":
                ans += "A"
            elif ch == "C":
                ans +="G"
            elif ch =="G":
                ans +="C"
        print("the complement of "+str(data)+" is: "+str(ans))



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
