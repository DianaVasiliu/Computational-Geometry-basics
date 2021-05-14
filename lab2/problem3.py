import helper
from sympy import *


def problem3():
    f = open('in_out/3_in.txt', 'r')
    g = open('in_out/my_out/my_3_out.txt', 'w')

    A, B, C = helper.readPoints(f, 3)

    nrPoints = int(f.readline())
    points = helper.readPoints(f, nrPoints)

    for point in points:
        triangle = Polygon(*(A, B, C))
        circle = triangle.circumcircle
        where = helper.pointPositionCircle(circle, point)

        g.write('({}, {}) - {}\n'.format(point[0], point[1], where))
