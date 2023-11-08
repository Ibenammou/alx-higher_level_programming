#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        mat = []
        for line in matrix:
            i = []
            for n in line:
                i.append(n**2)
            mat.append(i)
        return(mat)
