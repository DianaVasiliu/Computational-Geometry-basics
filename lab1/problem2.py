import matplotlib.pyplot as plt
import helper as hlp


def problem2():
    f = open('in_out/2.in', 'r')
    g = open('in_out/my_output/2.out', 'w')

    pointList = hlp.readPoints(f)
    convex_hull = hlp.convexHull(pointList)

    hlp.plot(pointList)
    hlp.plot(convex_hull, False)
    plt.title('Problem 2 - Convex Hull')
    plt.show()

    for pt in convex_hull:
        g.write(str(pt[0]) + ' ' + str(pt[1]) + '\n')
