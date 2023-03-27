#!/usr/bin/python3
<<<<<<< HEAD

=======
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
import sys


def safe_print_integer_err(value):
<<<<<<< HEAD
    """Prints an integer with "{:d}".format().
    If a ValueError message is caught, a corresponding
    message is printed to standard error.
    Args:
        value (int): The integer to print.
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
=======
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        sys.stderr.write("Exception: ")
        sys.stderr.write(ex.args[0])
        sys.stderr.write("\n")
        return False
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
