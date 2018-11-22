import matplotlib.pyplot as plt
import numpy as np
# 存在的一些问题，使用递归完成了对单方向的简单定点求根。
# 比如该方法中我使用的函数f（x）=x^3-2x-3的根位于1.8-2.0之间，在迭代为收敛的情况下，
# 可以得出正确值，在发散的前提下只能顺利跳出，而不能扭转。


# 要求根的函数 ：目标是 f（x）=x^3-2x-3
def function_composition(x):
    """函数表示和结果求值"""
    fc = (2 * x + 3)**(1/3)
    return fc

# 待定注意
def function_composition_reverse(x):
    """函数表示和结果求值"""
    fc = (x**3 - 3)/2
    return fc


def iterations_number(nums):
    print('逐次逼近第', nums, '后求得：')


def display(output, flags):
    """打印测试结果"""
    if flags == 'estimated_value'or flags == 'ev':
        print('函数的一个根为'+str(round(output, 10)))

    if flags == 'unsolvable ' or flags == 'un':
        print("以该点递归无法获得根。")


def simple_fixed_point(x, acc):
    """简单定点迭代法"""
    global num
    num = num + 1
    fx = function_composition(x)
    lists.append(fx)
    draw_allways([[x, x], [0, fx]], [[x, fx], [fx, fx]])
    if num != 1 and lists[0] < fx:
        del lists[1]
        display(0, 'un')
        # 待定注意
        simple_fixed_point_reverse(x, acc)

    else:
        if (x-fx) < acc and function_composition(fx) < fx:
            iterations_number(num)
            display(x, 'ev')
        else:
            simple_fixed_point(function_composition(x), acc)


# 待定注意
def simple_fixed_point_reverse(x, acc):
    """简单定点迭代法"""
    global num
    num = num + 1
    fx = function_composition_reverse(x)
    print(fx)
    lists.append(fx)
    draw_allways([[x, x], [0, fx]], [[x, fx], [fx, fx]])
    if num != 1 and lists[0] < fx:
        del lists[1]
        display(0, 'un')
    else:
        if (x-fx) < acc and function_composition_reverse(fx) < fx:
            iterations_number(num)
            display(x, 'ev')

        else:
            simple_fixed_point_reverse(function_composition_reverse(x), acc)


def input_limit():
    """输入定点"""
    a = float(input("请输入定点的值："))
    acc = float(input("请输入误差限的值："))
    result = [a, acc]
    return result


def main():
    """主驱动"""
    print("简单定点迭代法：f（x）=x^3-2x-3（根在1.8-2.0左右，唯一。）")
    result = input_limit()
    flag = result[0]
    simple_fixed_point(result[0],result[1])


def draw():
    """绘制函数和寻找的路径"""
    plt.title("fixed point iteration method")
    x = np.linspace(0, 10)
    y = np.linspace(0, 10)
    plt.plot(x, x)
    plt.plot(x, (2 * x + 3) ** (1 / 3), "r-")
    plt.grid(True)  # 设置网格线
    plt.show()


def draw_allways(dot1,dot2):
    """负责完成函数变换路径"""
    plt.plot(dot1[0], dot1[1])
    plt.plot(dot2[0], dot2[1])


# 开始
num = 0
flag = 0
lists = []
main()
draw()


