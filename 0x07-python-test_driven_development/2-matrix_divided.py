#!/usr/bin/python3
"""
my matrix class
"""


def matrix_divided(matrix, div):
        """
        Description:
            Divides all elements of a matrix by "div"
            must be a list of lists of integers or floats
        Args:
            matrix (list): the lists.
            div (int or float): a numbr.
        Returns:
            list: new matrix.
        Raises:
            TypeError: not lists of int/floats or div is not number
            ZeroDivisionError: If div is equal to 0.
        """

        if type(matrix) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        size = None
        for ele in matrix:
            if type(ele) is not list:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            if size is None:
                size = len(ele)
            elif size != len(ele):
                raise TypeError("Each row of the matrix must have the same size")
            for i in ele:
                if type(i) is not int and type(i) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")

        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        newMtrix = []
        for ele in matrix:
            nexElem = [round(i / div, 2) for i in ele]
            newMtrix.append(nexElem)

        return newMtrix
