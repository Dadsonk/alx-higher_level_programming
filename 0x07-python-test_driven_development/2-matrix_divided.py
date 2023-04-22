#!/usr/bin/python3
"""Defines a matrix division function."""




def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div, rounded to 2 decimal places.

    Args:
    - matrix (list[list]): A list of lists of integers or floats.
    - div (int/float): The divisor.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers/floats.
    - TypeError: If any row of the matrix has a different size than the others.
    - TypeError: If div is not a number (int or float).
    - ZeroDivisionError: If div is 0.

    Returns:
    - A new matrix representing the result of the division.
    """
    if not isinstance(matrix, list) 
    or not all(isinstance(row, list) for row in matrix):
   raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(num/div, 2) for num in row] for row in matrix]

