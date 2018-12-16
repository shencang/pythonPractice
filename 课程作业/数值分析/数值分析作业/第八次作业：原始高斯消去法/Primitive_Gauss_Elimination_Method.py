import numpy as np

# inp = [[6,   15,  55,  152.6],
#       [15,  55, 225,  585.6],
#       [55, 225, 979, 2488.8]]
inp = [[6, 15, 55],
       [15, 55, 225],
       [55, 225, 979]]
bs = [152.6, 585.6, 2488.8]
bs.insert(0, 0)
b = np.array([bs])
b = b.T
b = b.astype('float')
print(b)

ins = np.array([[0, 0, 0]])
d = [[0], [0], [0], [0]]
# A = np.hstack((a,b))
inp = np.r_[ins, inp]
inp = np.hstack((d, inp))
inp = inp.astype('float')
print(inp)


def fs(inp, b):
    i = 0
    n = len(inp) - 1
    x = []
    sums = 0
    k = 1
    # while k<(n):
    for k in range(1, n):
        # i= k+1
        # while i<n+1:
        for i in range(k + 1, n + 1):
            factor = inp[i][k] / inp[k][k]
            # j=k+1
            # while j<n+1:
            for j in range(k + 1, n + 1):
                inp[i][j] = inp[i][j] - factor * inp[k][j]
                j = j + 1
            b[i] = b[i] - factor * b[k]
            i = i + 1
        k = k + 1
    # for i in range(n):
    #    x.append(b[i]/inp[i][i])
    for ns in range(n + 1):
        x.append(0)
    x[n] = (b[n] / inp[n][n])
    i = n - 1
    while i > 0:
        sums = b[i]
        j = i + 1
        while j < n + 1:
            sums = sums - inp[i][j] * x[j]
            j = j + 1
        x[i] = sums / inp[i][i]
        i = i - 1
    print(inp)
    print(b)
    print(x)


fs(inp, b)
