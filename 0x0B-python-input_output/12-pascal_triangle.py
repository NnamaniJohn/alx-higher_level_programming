#!/usr/bin/python

"""pascal triangle"""


def pascal_triangle(n):
    """
    pascal triangle
    """
    if n <= 0:
        return []
    tri = []
    for i in range(1, n + 1):
        li = []
        for j in range(1, i + 1):
            if j == 1:
                val = 1
            elif j == i:
                val = 1
            else:
                val = tri[i-1-1][j-1-1] + tri[i-1-1][j-1]
            li.append(val)
        tri.append(li)
    return tri
