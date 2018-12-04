import matplotlib.pyplot as plots

VALUE = [([0] * 100) for i in range(100)]

# 用来正常显示负号
plots.rcParams['axes.unicode_minus'] = False
# 用来正常显示中文标签
plots.rcParams['font.sans-serif'] = ['SimHei']

def knapsack(value, weght, capacity, n, choose):
    for i in range(n + 1):
        VALUE[i][0] = 0
    for j in range(capacity + 1):
        VALUE[0][j] = 0
    for i in range(n):
        for j in range(capacity + 1):
            if (j < weght[i]):
                VALUE[i][j] = VALUE[i - 1][j]
            else:
                VALUE[i][j] = max(VALUE[i - 1][j], (VALUE[i - 1][j - weght[i]] + value[i]))
    j = capacity
    i = n - 1
    while i >= 0:
        if VALUE[i][j] > VALUE[i - 1][j]:
            choose[i] = 1
            j = j - weght[i]
        else:
            choose[i] = 0
        i = i - 1

    for i in range(n):
        print(choose[i], ' ', end='')
    print()
    for i in range(n):
        for j in range(capacity + 1):
            print(VALUE[i][j], '\t', end='')
            if j == capacity:
                print()

    return VALUE[n - 1][capacity]


def display(flag, a, b):
    if flag == 'result' or flag == 're':
        print("拟合的直线为", 'y=', a, '+', b, 'x')


if __name__ == '__main__':
    weight = [2, 2, 6, 5, 4, 3, 5, 6]
    valve = [6, 3, 5, 4, 6, 4, 5, 7]
    choose = [0, 0, 0, 0, 0, 0, 0, 0]
    n = len(weight)
    capacity = 10
    sums = knapsack(valve, weight, capacity, n, choose)
    print(sums)
