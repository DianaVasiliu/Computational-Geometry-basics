import helper
import helper as hlp
from sympy import *
import random


def findOrientation(p1, p2, p3):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]

    value = (x2 * y3 + x1 * y2 + x3 * y1) - \
            (x2 * y1 + x3 * y2 + x1 * y3)

    return value


def isbetween(between, p1, p2):
    if p1[0] < between[0] < p2[0]:
        return True
    if p2[0] < between[0] < p1[0]:
        return True
    if p1[1] < between[1] < p2[1]:
        return True
    if p2[1] < between[1] < p1[1]:
        return True
    return False


def checkPosition(point, polygon, M):
    intersections = 0

    n = len(polygon.vertices)
    for i in range(n):
        point1 = polygon.vertices[i % n]
        point2 = polygon.vertices[(i + 1) % n]

        if findOrientation(point1, point2, point) == 0 and isbetween(point, point1, point2):
            return 'on edge'

        edge = Segment(point1, point2)
        line = Segment(M, point)
        inter = line.intersection(edge)
        if inter:
            intersections += 1

    if intersections % 2:
        return 'inside'
    else:
        return 'outside'


def problem1():
    f = open('in_out/1_in.txt', 'r')
    g = open('in_out/my_out/my_1_out.txt', 'w')

    polygon, points = hlp.readPolygonsAndPoints(f)

    helper.plotPolygon(polygon.vertices, 1, points=points)

    x = max([point[0] for point in points])
    y = max([point[1] for point in points])
    M = Point(x + random.randint(10000, 20000), y + random.randint(10000, 20000))

    for point in points:
        where = checkPosition(point, polygon, M)

        px = point[0]
        py = point[1]
        if type(px) == Rational:
            px = float(px)
        g.write('({}, {}) - {}\n'.format(px, py, where))
