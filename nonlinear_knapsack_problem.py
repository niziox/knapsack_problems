#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import math

def non_kp_decisions(g, a, b):
    decisions = np.zeros((b + 1, 2 * len(a)))

    for iter, col in zip(range(len(a)-1, -1, -1), range(0, 2 * len(a) + 1, 2)):
        for y in range(b + 1):
            if iter == 0 and y != b:
                continue
            x_tab = [i for i in range(math.floor(y / a[iter])+1)]
            min_x_f = (np.inf, np.inf)

            if iter == len(a) - 1:
                for x in x_tab:
                    if g[x][iter] < min_x_f[1]:
                        min_x_f = (x, g[x][iter])
                decisions[y, col], decisions[y, col+1] = min_x_f
            else:
                for x in x_tab:
                    try:
                        if g[x][iter] + decisions[y - a[iter]*x, col-1] < min_x_f[1]:
                            min_x_f = (x, g[x][iter] + decisions[y - a[iter]*x, col-1])
                    except IndexError:
                        pass

                decisions[y, col], decisions[y, col+1] = min_x_f

    return decisions

def non_kp(g, a, b):
    decisions = non_kp_decisions(g, a, b)
    objective_function = {}

    def _non_kp(row, col, objective_function, decisions, object):
        if object == len(a):
            return
        else:
            row = int(row)
            col = int(col)
            objective_function[object+1] = int(decisions[row, col])
            row = row - a[object] * decisions[row, col]

            _non_kp(row, col-2, objective_function, decisions, object+1)

    _non_kp(b, 2 * len(a) - 2, objective_function, decisions, 0)

    return objective_function


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = 15
    g = np.array([[20, 9, 6, 4],
                  [18, 6, 2, 0],
                  [14, 3, 0, 0],
                  [11, 0, 0, 0],
                  [7, 0, 0, 0],
                  [2, 0, 0, 0],
                  [0, 0, 0, 0]])

    print(non_kp(g, a, b))
