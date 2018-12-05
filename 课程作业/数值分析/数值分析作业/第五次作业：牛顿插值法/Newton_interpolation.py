import matplotlib.pyplot as plt
from pylab import mpl


def getparameters(choose):
    """
        选择课本的三组数据中的一组。
        4.12 二次牛顿插值多项式，参数见下。求f（1.5）
        4.13 三次牛顿插值多项式，参数见下。求f（0.5）
        4.14 四次牛顿插值多项式，参数见下。求f（5.96）
    """
    if choose == 1:
        x_c = 1.5
        x = [1, 3, 2]
        y = [1, 2, -1]

    if choose == 2:
        x_c = 0.5
        x = [0, 1, 2, 4]
        y = [3, 6, 11, 51]
    if choose == 3:
        x = [0.4, 0.55, 0.65, 0.80, 0.90, 1.05]
        y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
        x_c = 0.596
    return x, y, x_c


quotient = []
for i in range(len(x) + 1):
    quotient.append(0)


def n_difference_quotient(x, y):
    # i记录计算差商的次数，这里循环5次，计算5次差商。
    i = 0
    print(quotient)
    # quotient = [0, 0, 0, 0,0,0]
    while i < len(x) - 1:
        j = len(x) - 1
        while j > i:
            if i == 0:
                quotient[j] = ((y[j] - y[j - 1]) / (x[j] - x[j - 1]))
            else:
                quotient[j] = (quotient[j] - quotient[j - 1]) / (x[j] - x[j - 1 - i])
            j -= 1
        i += 1
    return quotient


def function(parameters, data, order):
    return (y[0] +
            parameters[1] * (data - x[0]) +
            parameters[2] * (data - x[0]) * (data - x[1]) +
            parameters[3] * (data - x[0]) * (data - x[1]) * (data - x[2]) +
            parameters[4] * (data - x[0]) * (data - x[1]) * (data - x[2]) * (data - x[3]) +
            parameters[5] * (data - x[0]) * (data - x[1]) * (data - x[2]) * (data - x[3]) * (data - x[4]))
    # return  (y[0] +
    #          parameters[1]*(data-x[0])+
    #          parameters[2]*(data-x[0])*(data-x[1])+
    #          parameters[3]*(data-x[0])*(data-x[1])*(data-x[2])+
    #          parameters[4]*(data-x[0])*(data-x[1])*(data-x[2])*(data-x[3]))


# x = [0, 1, 2, 4]
# y = [3,6,11,51]
# x = [0.4, 0.55, 0.65, 0.80, 0.90, 1.05]
# y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]

"""计算插值多项式的值和相应的误差"""


def calculate_data(x, parameters):
    returnData = []
    for data in x:
        returnData.append(function(parameters, data, len(x) - 1))
    return returnData


"""画函数的图像
newData为曲线拟合后的曲线
"""


def draw(parameters, newData):
    plt.scatter(x, y, label="离散数据", color="red")
    plt.plot(x, newData, label="牛顿插值拟合曲线", color="black")
    plt.scatter(x_c, function(parameters, x_c, len(x) - 1), label="预测函数点", color="blue")
    plt.title("牛顿插值法")
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
    global x, y, x_c
    # 获得x y 的取值和要计算的值
    x, y, x_c = getparameters(input_estimation_and_conditions())
    # 计算差商
    parameters = n_difference_quotient(x, y)
    # 以差商算出的公式计算大致对应点，用于绘图
    predictive_value = calculate_data(x, parameters)
    # 绘图
    draw(parameters, predictive_value)
    print(function(parameters, x_c, len(x) - 1))


if __name__ == '__main__':
    x = []
    y = []
    x_c = 0
    newton_interpolation()
