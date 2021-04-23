import matplotlib.pyplot as plt
import helper as hlp


def position(point, polygon):
    n = len(polygon)
    for i in range(n):
        if i <= n - 2:
            p1 = polygon[i]
            p2 = polygon[i + 1]
        else:
            p1 = polygon[i]
            p2 = polygon[0]
        orientation = hlp.findOrientation(p1, p2, point)
        if orientation < 0:
            return -1
        elif orientation == 0:
            return 0
    return 1


def problem3():
    f = open('in_out/3.in', 'r')
    g = open('in_out/my_output/3.out', 'w')

    polygonPoints = hlp.readPoints(f)
    pointList = hlp.readPoints(f)

    hlp.plot(polygonPoints, False)
    hlp.plot(pointList)
    plt.title('Problem 3 - Point Position Relative to a Polygon')
    plt.show()

    for p in pointList:
        pos = position(p, polygonPoints)

        if pos < 0:
            g.write('outside\n')
        elif pos > 0:
            g.write('inside\n')
        else:
            g.write('on edge\n')
