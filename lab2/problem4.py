import helper
from sympy import *


def illegalEdge(p1, p2, p3, p4):
    triangle = Polygon(*(p1, p2, p3))
    circle = triangle.circumcircle
    where = helper.pointPositionCircle(circle, p4)
    if where == 'inside':
        return 'illegal'
    else:
        return 'legal'


def problem4():
    f = open('in_out/4_in.txt', 'r')
    g = open('in_out/my_out/my_4_out.txt', 'w')

    A, B, C = helper.readPoints(f, 3)

    nrPoints = int(f.readline())
    points = helper.readPoints(f, nrPoints)

    helper.plotTriangleCircle([A, B, C], points, 4)
    for D in points:
        helper.plotTriangleCircle([A, B, C], [D], 4)
        helper.plotTriangleCircle([A, B, D], [C], 4)

        legal = illegalEdge(A, B, C, D)
        g.write('AC edge is {}\n'.format(legal))

        legal = illegalEdge(A, B, D, C)
        g.write('BD edge is {}\n'.format(legal))
        g.write('\n')
