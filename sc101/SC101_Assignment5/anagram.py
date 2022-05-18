"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dic = {}


def main():
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        read_dictionary()
        data = input(f'Find anagrams for :')
        if data == EXIT:
            break
        else:
            find_anagrams(data)


def read_dictionary():
    global dic
    with open(FILE, mode="r") as f:
        for line in f:
            dic[line.strip()] = 0


def find_anagrams(s):
    """
    :param s: Input word
    :return: print anagrams
    """
    a = helper(s, "", len(s), [], [])
    print(f'{len(a)} anagrams: {a}')


def helper(lst, anagram, answer_len, index, ans):
    if len(anagram) == answer_len and anagram in dic:
        if anagram not in ans:
            print(f'Searching...')
            print(f'Found: {anagram}')
            ans.append(anagram)
    else:
        for i in range(len(lst)):
            # Choose
            if i not in index:
                anagram += lst[i]
                index.append(i)
                # Explore
                helper(lst, anagram, answer_len, index, ans)
                # Un-choose
                anagram = anagram[:-1]
                index.pop()
    return ans


# def has_prefix(sub_s):
#     """
#     :param sub_s:
#     :return:
#     """
#     for ch in dic:
#         if ch.startswith(sub_s):
#             return True
#     return False


if __name__ == '__main__':
    main()
