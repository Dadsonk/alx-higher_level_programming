#!/usr/bin/python3
<<<<<<< HEAD

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
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
=======
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        item = my_list[i]
        try:
            print("{:d}".format(item), end="")
            n += 1
        except Exception:
            continue
    print("")
    return n
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
