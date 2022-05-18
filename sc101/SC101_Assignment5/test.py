
def main():
    number_list = [1, 1, 2, 5, 10]
    print(can_make_sum(number_list, 9))


def can_make_sum(lst, target):
    return helper(lst, target, 0, 0)


def helper(lst, target, current, index):
    if index == len(lst):
        return current == target
    else:
        return helper(lst, target, current, index+1) or helper(lst, target, current+lst[index], index+1)


if __name__ == "__main__":
    main()