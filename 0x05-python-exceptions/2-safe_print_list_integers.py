#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    Args:
        my_list (list): this is the list where numbers must be printed from.
        x (int): The amount ofcomponents of my_list to print.

    Returns:
        Returns the real number of integers printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
