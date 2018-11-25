import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 要求根的函数 ：目标是 f（x）=x^3-2x-3
def function_composition(x):
    """函数结果求值"""
    fc = pow(x, 3) - 2 * x - 3
    return fc


# 要求根的导数 ：3x^2-2
def derivative_solution(x):
    """导数结果求值"""
    ds = 3 * pow(x, 2) - 2
    return ds


def iterations_number(nums):
    print('逐次逼近第', nums, '后求得：')


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
    result = input_estimation_and_conditions()

    # 存放系数，正序a0到a5
    save_coeff = [1.25, -3.875, 2.125, 2.75, -3.5, 1]
    save_b = ['b0', 'b1', 'b2', 'b3', 'b4', 'b5']
    save_c = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5']
    r_s = [result[0], result[1], 'r', 's']
    r_s_error_analysis = ['%r', '%s']
    




def draw(lists_x, lists_new, lists_fc):
    """绘制函数和寻找过程的路径"""
    plt.title("tangential_method")
    plt.plot([lists_x[1],lists_x[1]],[0,function_composition(lists_x[1])],c='r')
    x = np.arange(0, max(lists_x), 0.01)
    y = np.power(x, 3) - 2 * x - 3
    plt.plot(x, y)
    plt.axis([0, max(lists_x), 0, max(lists_fc)])
    plt.plot([lists_x[0], lists_x[0]], [[lists_x[0]], [lists_fc[0]]])
    for i in range(len(lists_x)):
        plt.scatter(lists_x[i], 0, c='r')
    for i in range(len(lists_new)):
        plt.plot([lists_x[i], lists_new[i], lists_new[i]], [lists_fc[i], 0, lists_fc[i+2]], c='r')
    # 设置网格线
    plt.grid(True)
    plt.show()


# 开始
num = 0
flag = 0
main()


