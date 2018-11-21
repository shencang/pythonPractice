# from matplotlib import pyplot as plot
import numpy
import matplotlib.pyplot as plt
from matplotlib import animation  #动画包

print("题目：用定点迭代法求x^3-x-1=0在x=1.5附近的一个根")
i = 0
def result(x):
    y = (x+1)**(1/3)
    return y

def Y(x):
    global i #global关键字全局变量修改必须声明
    i = i+1
   # updata(x)
    plt.plot([x, x], [0, result(x)])
    plt.plot([x,result(x)],[result(x),result(x)])# 1.5,result(1.5)   1.5,1.5
    if((x-result(x))<0.000001):
        print('逐次逼近第', i, '后求得：')
        print('函数在x=1.5附近的一个根为',round(x,5))# 输出字符方式
    else:
        Y(result(x))

Y(1.5)

x = 0
# plt.plot([0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0],[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0])
plt.title("fixed point iteration method")
x = numpy.linspace(1.3,1.6)
y = numpy.linspace(1.3,1.6)
plt.xlim(1.3,1.6)# 固定坐标
plt.ylim(1.3,1.6)
plt.plot(x,x)
plt.plot(x,(x+1)**(1/3),"r-")
plt.grid(True)# 设置网格线
x = 1.5
# plt.plot([x,x],[0,result(x)])
##plt.vlines(0,1,result(1.5),linestyles = "dashed")
# fig1 = plt.figure()# 建立子图
# def updata(data):
   # plt.plot([x, x], [0, result(x)])
    #plt.plot([x, result(x)], [result(x), result(x)])  # 1.5,result(1.5)   1.5,1.5
    #fig_points.set_data(data[:, 0:num])
   # return line
#fig_points, = plt.plot([], [])#'ro'是画点 不加是连线
#anim = animation.FuncAnimation(fig1, updata)#结束条件
plt.show()
