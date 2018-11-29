class Point:
    def __init__(self, x, y, flag):
        self.x = x
        self.y = y
        self.flag = flag


def convexhull(n):
    i = 0
    for i in range(n):
        j = i + 1
        for j in range(n):
            a = point[j].y - point[i].y
            b = point[j].x - point[i].x
            c = (point[i].x * point[j].y) - (point[i].y * point[j].x)
            sign1 = 0
            sign2 = 0
            k = 0
            for k in range(n):
                if k == j and k == i:
                    continue
                if a * point[k].x + b * point[k].y == c:
                    sign1 = sign1 + 1
                    sign2 = sign2 + 1
                if a * point[k].x + b * point[k].y > c:
                    sign1 = sign1 + 1
                if a * point[k].x + b * point[k].y < c:
                    sign2 = sign2 + 1
            if sign1 == (n - 2) and sign2 == (n - 2):
                point[i].flag = 1
                point[j].flag = 1


point = [Point(1, 2, 0), Point(2, 3, 1)]
n = len(point)
