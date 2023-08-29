#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elememts of a list.

    Args:
        my_list (list): this is the list which prints components from.
        x (int): this is the amount of components of my_list to print.

    Returns:
        The amount of components printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
