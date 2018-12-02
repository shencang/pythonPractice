import matplotlib.pyplot as plots
import numpy as np
from numpy.linalg import *

# 用来正常显示负号
plots.rcParams['axes.unicode_minus'] = False
# 用来正常显示中文标签
plots.rcParams['font.sans-serif'] = ['SimHei']

lists_x = [0.0, 0.2, 0.4, 0.6, 0.8]
lists_y = [0.9, 1.9, 2.8, 3.3, 4.2]


def result():
    """例题5.1的求解"""
    resultxx = 0
    resultyx = 0
    resultx = 0
    resulty = 0
    num = 0
    for x in lists_x:
        resultyx = resultyx + x * lists_y[num]
        num = num + 1

    for x in lists_x:
        resultxx = resultxx + x * x

    for x in lists_x:
        resultx = resultx + x

    for y in lists_y:
        resulty = resulty + y

    print(resultx)
    print(resultyx)
    print(resultxx)
    print(resulty)
    print(num)

    a = np.array([[num, resultx], [resultx, resultxx]])
    b = np.array([[resulty], [resultyx]])
    print(solve(a, b))


result()
