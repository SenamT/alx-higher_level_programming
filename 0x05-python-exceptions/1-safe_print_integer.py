#!/usr/bin/python3


def safe_print_integer(value):
    """prints an integer with "{:d}".format().

    Args:
        value (int): this is the number which needs to be printed.

    Returns:
        Returns True if value has been correctly printed.
        Otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
