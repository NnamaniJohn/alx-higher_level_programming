#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    t_wgh = 0
    for s, w in my_list:
        total += (s * w)
        t_wgh += w
    avg = total / t_wgh
    return avg
