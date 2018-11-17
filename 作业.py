import math
import matplotlib.pyplot as plt
import numpy as np
import time


def function_composition(x):
    fc = math.pow(x, 2) - x - 20
    return fc


def display(output, flag):
    if flag == 'true_value'or flag == 'tv':
        print("零点的准确坐标为：" + str(output))

    if flag == 'estimated_value'or flag == 'ev':
        print("零点的估计坐标为：" + str(output))


def bisection_method(a, b, acc):
    """二分法"""
    tag = True
    while tag:
        if function_composition(a)*function_composition(b) > 0:
            print("该区间内无解。")
        else:
            while tag:
                if function_composition(a)*function_composition(b) == 0.0:
                    if function_composition(a) == 0.0:
                        display(a, 'tv')
                        tag = False
                    else:
                        display(b, 'tv')
                        tag = False
                    break
                else:
                    mid = (a+b)/2
                    if abs(b-a) < acc:
                        display(mid, 'ev')
                        tag = False
                        break
                    else:
                        if function_composition(a)*function_composition(mid)>0:
                            a = mid
                        else:
                            b = mid
    print("Bisection method")


def false_position(a,b,acc):
    """试位法"""
    print("False Position")


def input_limit():
    """输入左右端点"""
    a = float(input("请输入左端点的值："))
    b = float(input("请输入右端点的值："))
    acc = float(input("请输入精确度："))
    back = [a, b, acc]
    return back


def main():
    """驱动与选择"""
    choose = int(input("请输入执行二分法还适位法，1选择二分法 2选择试位法,0退出"+'\n 输入：'))
    if int(choose)==1:
        print("二分法")
        limit=input_limit()
        bisection_method(limit[0], limit[1], limit[2])
    if int(choose)==0:
        exit()
    else:
        print("试位法")
        limit = input_limit()
        false_position(limit[0], limit[1], limit[2])




while(True):
    # 开始的入口
    main()


