import matplotlib.pyplot as plt
from pylab import mpl


def get_parameters(choose):
    """
        选择课本的三组数据中的一组。
        4.12 二次牛顿插值多项式，参数见下。求f（1.5）
        4.13 三次牛顿插值多项式，参数见下。求f（0.5）
        4.14 五次牛顿插值多项式，参数见下。求f（0.596）（求得是四阶可以取前五个节点，在这里取6个，效果类似，取最优）
    """
    global x, y, x_c
    if choose == 1:
        x_c = 1.5
        x = [1, 3, 2]
        y = [1, 2, -1]

    elif choose == 2:
        x_c = 0.5
        x = [0, 1, 2, 4]
        y = [3, 6, 11, 51]

    elif choose == 3:
        x = [0.4, 0.55, 0.65, 0.80, 0.90, 1.05]
        y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
        x_c = 0.596
    else:
        print("输入有误。请重新输入")
        newton_interpolation()
        # 可以直接计算n阶
        # 但是没有数据，不保留键入入口。 保留程序入口


def secondary_spline_method():
    """
    二次样条插值法
    :return:
    """
    global x, y
    # num_height表示未知数和方程数量
    num_weight = 3 * (len(x) - 1)
    parameter = []
    i = 1
    # 计算方程内点两边相邻节点处函数值相等的方程 方程数量2n-2
    while i < len(x) - 1:
        coefficient = init(num_weight)
        # 计算a b c放入系数coefficient列表里，原计划打算直接填充矩阵，遇到点问题。
        coefficient[(i - 1) * 3] = x[i] * x[i]
        coefficient[(i - 1) * 3 + 1] = x[i]
        coefficient[(i - 1) * 3 + 2] = 1
        # coefficient 里的数据取出后后移
        movement_coefficient = init(num_weight)
        movement_coefficient[i * 3] = x[i] * x[i]
        movement_coefficient[i * 3 + 1] = x[i]
        movement_coefficient[i * 3 + 2] = 1
        # 因为a1(a0)= 0,去除矩阵中a0对应的行列
        parameter.append(coefficient[1:])
        parameter.append(movement_coefficient[1:])
        i = i + 1
    # 输入端点处两个方程的函数值 方程数量2
    coefficient = init(num_weight - 1)
    coefficient[0] = x[0]
    coefficient[1] = 1
    parameter.append(coefficient)
    coefficient = init(num_weight)
    coefficient[((len(x) - 1) - 1) * 3 + 0] = x[-1] * x[-1]
    coefficient[((len(x) - 1) - 1) * 3 + 1] = x[-1]
    coefficient[((len(x) - 1) - 1) * 3 + 2] = 1
    temp = coefficient[1:]
    parameter.append(temp)
    # 导数内点相等列出的方程。方程数量n-1
    # 人为规定a1=0  方程数量1
    i = 1
    while i < len(x) - 1:
        coefficient = init(num_weight)
        coefficient[(i - 1) * 3] = 2 * x[i]
        coefficient[(i - 1) * 3 + 1] = 1
        coefficient[i * 3] = -2 * x[i]
        coefficient[i * 3 + 1] = -1
        temp = coefficient[1:]
        parameter.append(temp)
        i += 1
    return parameter


def init(size):
    j = 0
    data = []
    while j < size:
        data.append(0)
        j += 1
    return data


def cubic_spline_method():
    """
    三次样条插值法
    :return:
    """


def draw(parameters, new_data):
    """画通过差商计算出来的函数的图像
       new_data是曲线拟合后的曲线
       （二阶情况下比较失准····）
    """
    plt.scatter(x, y, label="离散数据", color="red")
    plt.plot(x, new_data, label="牛顿插值拟合曲线", color="black")
    # plt.scatter(x_c, functions(parameters, x_c, len(x) - 1), label="预测函数点", color="blue")
    plt.title("牛顿插值法（newton interpolation）")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.legend(loc="upper left")
    plt.show()


def input_estimation_and_conditions():
    """输入初始选择"""
    print('请选择数据:1,为课本例题4-12的数据\n 2,为课本例题4-13的数据\n 3,为课本例题4-14的数据')
    result = int(input("请输入选择"))
    return result


def newton_interpolation():
    """
    启动整个计算过程
    """
    # 获得x y 的取值和要计算的值
    get_parameters(input_estimation_and_conditions())
    # 计算差商
    # 绘图
    #    draw(parameters, predictive_value)
    # 输出估计值
    student()


# print('计算得在x=', x_c, '时，函数值近似为：', functions(parameters, x_c, len(x) - 1))


def student():
    """
    显示学号= =
    :return: 1607094239 金浩
    """
    print('made by 1607094239 金浩')


if __name__ == '__main__':
    x = [2, 4.5, 7, 9]
    y = [2.5, 1, 2.5, 0.5]
    quotient = []
    x_c = 0
    # newton_interpolation()
    ss = secondary_spline_method()

    for i in range(len(ss)):
        print(ss[i])
