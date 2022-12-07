#!/usr/bin/pytho3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new.append([x * x for x in row])
    return new
