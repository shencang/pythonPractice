import sys

import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

sys.setrecursionlimit(10000)
def error_analysis():
    """误差分析"""
    r = (save_b[0] * save_c[3] - save_b[1] * save_c[2]) / (save_c[2] * save_c[2] - save_c[1] * save_c[3]) + r_s[0]
    s = (save_b[0] * save_c[2] - save_b[1] * save_c[1]) / (save_c[3] * save_c[1] - save_c[2] * save_c[2]) + r_s[1]
    r_s[2] = round(r, 4)
    r_s[3] = round(s, 4)


def error_analysis_for_rse():
    """误差分析"""
    r_s_error_analysis[0] = round((r_s[2] - r_s[0]) / r_s[2], 5)
    r_s_error_analysis[1] = round((r_s[3] - r_s[1]) / r_s[3], 5)
    r_s[0] = r_s[2]
    r_s[1] = r_s[3]


def result_b(r, s):
    """求b的值"""
    num = 3
    save_b[5] = round(save_coeff[5], 5)
    save_b[4] = round(save_coeff[4] + r * save_b[5], 5)
    while num != -1:
        save_b[num] = round(save_coeff[num] + r * save_b[num + 1] + s * save_b[num + 2], 5)
        num = num - 1



def result_c(r, s):
    """求c的值"""
    num = 3
    save_c[5] = round(save_b[5], 4)
    save_c[4] = round(save_b[4] + r * save_c[5], 4)
    while num != -1:
        save_c[num] = round(save_b[num] + r * save_c[num + 1] + s * save_c[num + 2], 5)
        num = num - 1


# 题设题解的下标
w = 0
# 存放答案的下标
j = 0
# 标记迭代次数
count = 0
n_0 = [3, 1]
def result_bairstow(r, s):
    """贝尔斯托法求解"""
    global n, w, j, count
    count = count + 1
    result_b(r, s)
    result_c(r, s)
    error_analysis()
    error_analysis_for_rse()
    if (abs(r_s_error_analysis[0]) < 0.01) | (abs(r_s_error_analysis[1]) < 0.01):  # 误差满足条件
        print('经过', count, '次迭代得')
        save_x[j] = (r_s[2] + (r_s[2] ** 2 + 4 * r_s[3]) ** (1 / 2)) / 2  # 4
        print('x', j, '=', save_x[j])
        j = j + 1
        save_x[j] = (r_s[2] - (r_s[2] ** 2 + 4 * r_s[3]) ** (1 / 2)) / 2  # 3
        print('x', j, '=', save_x[j])
        j = j + 1
        n = n_0[w]  # n代表当前计算多项式项数
        w = w + 1
        if n == 1:
            save_x[4] = round((-r_s[2]) / r_s[3], 0)  # 单项式求解
            print('x', 4, '=', save_x[4])
            print('多项式的根:', save_x)
        elif (n == 2):
            print('二次项求实根：此题目不需计算')
        elif (n > 2):  # 传入修正的r,s值  商作为因式迭代
            count = 0
            save_coeff[0] = save_b[2]
            save_coeff[1] = save_b[3]
            save_coeff[2] = save_b[4]
            save_coeff[3] = save_b[5]
            save_coeff[4] = 0
            save_coeff[5] = 0
            result_bairstow(r_s[2], r_s[3])
    else:  # 不满足近似条件
        result_bairstow(r_s[2], r_s[3])  # 用修正的值继续迭代


def display(output, flags):
    """打印测试结果"""
    if flags == 'estimated_value' or flags == 'ev':
        print('函数的一个根为' + str(round(output, 10)))

    if flags == 'unsolvable ' or flags == 'un':
        print("以该点递归无法获得根。")


def input_estimation_and_conditions():
    """输入初始估计"""
    a = float(input("请输入估计r的值："))
    b = float(input("请输入估计s的值："))
    acc = float(input("请输入迭代满足条件的值：（小数表示的百分数）"))
    result = [a, b, acc]
    return result


def main():
    """主驱动"""
    print("贝尔斯托迭代法：f（x）=x^5-3.5*x^4+2.75*x^3+2.125*x^2-3.875*x+1.25")


    result_bairstow(result[0], result[1])


def draw(lists_x, lists_new, lists_fc):
    """绘制函数和寻找过程的路径"""


# 开始
num = 0
result = input_estimation_and_conditions()
# 存放系数，正序a0到a5
save_coeff = [1.25, -3.875, 2.125, 2.75, -3.5, 1]
save_b = ['b0', 'b1', 'b2', 'b3', 'b4', 'b5']
save_c = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5']
# 存放rs和误差
r_s = [result[0], result[1], 'r', 's']
r_s_error_analysis = ['%r', '%s']
coeff_num = len(save_coeff)
save_x = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5']
main()


