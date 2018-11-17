def Bisectionmethod(a,b):
    """二分法"""
    sa = int(a) ** 2 + int(a) + 20
    sb = int(b) ** 2 + int(b) + 20

    print()
    print(int(b) ** 2 + int(b) + 20)
    if int(a)*int(b)<=0:
        print("exit")

    print("Bisection method")

def FalsePosition(a,b):
    """试位法"""
    print("False Position")


print()
choose = int(input("请输入执行二分法还适位法，1选择二分法 2选择试位法"+'\n 输入：'))
if int(choose)==1:
    print("二分法")

    Bisectionmethod(0,5)
else:
    print("试位法")
    FalsePosition(0,5)




