def exact_solution(x):
    """
    求函数的精确值
    """
    fc = 0.5 * pow(x, 4) + 4 * pow(x, 3) - 10 * pow(x, 2) + 8.5 * x + 1
    return fc


def estimated_results(x):
    """
    求函数的导数值
    :param x:
    :return:
    """
    fc = -2 * pow(x, 3) + 12 * pow(x, 2) - 20 * pow(x, 2) + 8.5
    return fc


def input_estimation_and_conditions():
    print("步进输入-1或者0退出系统")
    x_begin = int(input("==============================\n请输入起始点"))
    x_end = int(input("==============================\n请输入终点"))
    h = int(input("==============================\n请输入步进"))
    return max(x_begin, x_end), min(x_begin, x_end), h


def swap(cha, chb):
    """
    交换两个数的值
    :param cha: 系数矩阵
    :param chb: 结果矩阵
    :return:两个交换的值
    """
    return chb, cha


def euler_method(x_begin, x_end, h):
    x_length = abs(x_begin - x_end)
    print(h)
    result = []
    result.append(exact_solution(x_begin))
    for i in range(x_begin, x_end, 1):
        print(i)
    # result.append(result[-1]+exact_solution(i))


def draw(lr, ur):
    """
    画图画图
    :param a:
    :param b:
    :return:
    """
    # 不会画·····
    # image = Image.fromarray(lr)
    # img = imread(image)


def student():
    """
    显示学号= =
    :return: 1607094239 金浩
    """
    print('made by 1607094239 金浩')


def result(x):
    """
    输出结果
    :param x:
    :return:
    """
    print("解集为：")
    for i in range(len(x)):
        print('x', i, '=', x[i])


def begin():
    """
    启动方法
    :return: 没有
    """
    # 得到系数和结果矩阵
    x_begin, x_end, h = input_estimation_and_conditions()
    # 错误输入时推出
    if h == 0 or h == -1:
        exit(0)

    euler_method(x_begin, x_end, h)
    # 画图
    # draw(l_r, u_r)
    # 学号输出
    student()
    # 结果输出
    result([1])


if __name__ == '__main__':
    begin()
