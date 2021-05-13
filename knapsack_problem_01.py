#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def kp_01(c, a, b):
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


if __name__ == '__main__':
    # c = [1, 2, 1, 2]
    # a = [1, 3, 2, 2]
    # b = 5

    c = [1, 3, 2, 2]
    a = [1, 4, 3, 3]
    b = 7

    print(kp_01(c, a, b))
