#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import math

def non_kp_decisions(g, a, b):
    pass

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

    print(non_kp_decisions(g, a, b))
