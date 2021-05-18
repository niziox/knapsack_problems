#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def kp_01_decisions(c, a, b):
    decisions = np.zeros((b + 1, 2 * len(c) + 1))
    decisions[:, 0] = np.arange(b + 1)

    for iter, col in zip(range(len(a)-1, -1, -1), range(1, 2 * len(c) + 2, 2)):
        if iter == len(a)-1:
            for y in range(b + 1):
                if y / a[iter] < 1:
                    decisions[y, col], decisions[y, col+1] = 0, 0
                else:
                    decisions[y, col], decisions[y, col+1] = 1, c[iter]
        else:
            for y in range(b + 1):
                if iter == 0 and y != b:
                    pass
                elif y / a[iter] < 1:
                    decisions[y, col], decisions[y, col+1] = 0, decisions[y, col-1]
                else:
                    decisions[y, col+1] = max(decisions[y, col-1], c[iter] + decisions[y - a[iter], col-1])
                    if decisions[y, col-1] == c[iter] + decisions[y - a[iter], col-1]:
                        decisions[y, col] = 10
                    elif decisions[y, col+1] == decisions[y, col-1]:
                        decisions[y, col] = 0
                    elif decisions[y, col+1] == c[iter] + decisions[y - a[iter], col-1]:
                        decisions[y, col] = 1

    return decisions


def kp_01(c, a, b):
    decisions = kp_01_decisions(c, a, b)
    objective_function = [[]]

    def _kp_01(row, col, objective_function, decisions, object, branch):
        if row == 0:
            return
        else:
            if decisions[row, col] == 10:
                if len(objective_function[0]) != 0:
                    objective_function.append(objective_function[branch].copy())
                else:
                    objective_function.append([])

                branch_zero = len(objective_function) - 1

                y = row - a[object]
                objective_function[branch].append(object + 1)
                _kp_01(y, col - 2, objective_function, decisions, object + 1, branch)

                _kp_01(row, col - 2, objective_function, decisions, object + 1, branch_zero)

            elif decisions[row, col] == 1:
                y = row - a[object]
                objective_function[branch].append(object+1)
                _kp_01(y, col-2, objective_function, decisions, object+1, branch)

            elif decisions[row, col] == 0:
                _kp_01(row, col-2, objective_function, decisions, object+1, branch)

    _kp_01(b, 2 * len(c) - 1, objective_function, decisions, 0, 0)

    return objective_function



if __name__ == '__main__':
    # c = [1, 2, 1, 2]
    # a = [1, 3, 2, 2]
    # b = 5

    # c = [1, 3, 2, 2]
    # a = [1, 4, 3, 3]
    # b = 7

    c = [1, 2, 1, 2, 5, 3, 2, 7, 4, 2]
    a = [1, 3, 2, 2, 4, 3, 5, 7, 1, 2]
    b = 21

    print(kp_01(c, a, b))
