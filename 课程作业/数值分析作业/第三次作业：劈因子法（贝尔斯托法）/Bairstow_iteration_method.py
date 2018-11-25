import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def error_analysis():
    """误差分析"""


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


def result_bairstow(r, s):
    """贝尔斯托法求解"""


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


