from sympy import *
import matplotlib.pyplot as plt
import random


def checkFiles(filename1, filename2):
    f = open(filename1, 'r')
    g = open(filename2, 'r')

    file1 = f.readlines()
    file2 = g.readlines()

    file1 = [x.replace('\n', '') for x in file1]
    file2 = [x.replace('\n', '') for x in file2]

    while '' in file1:
        file1.remove('')
    while '' in file2:
        file2.remove('')

    return file1 == file2


def plotPolygon(polygonPoints, number, axes=False, points=None):
    x = [point[0] for point in polygonPoints]
    y = [point[1] for point in polygonPoints]

    plt.fill(x, y, zorder=0)
    plt.title("Problem {}".format(number))

    if axes:
        xlines = []
        ylines = []
        for i in range(5):
            xlines.append(random.randrange(min(x), max(x), 1))
            ylines.append(random.randrange(min(y), max(y), 1))

        for i in range(5):
            plt.axvline(xlines[i], color='r')
            plt.axhline(ylines[i], color='y')

    if points is not None:
        px = [point[0] for point in points]
        py = [point[1] for point in points]
        plt.scatter(px, py, color='r', zorder=1)

    plt.show()


def readPoints(file, nrPoints):
    pointList = []
    for j in range(nrPoints):
        point = tuple([float(x) for x in file.readline().split()])
        point = Point(point)
        pointList.append(point)
    return pointList


def readPolygons(file):
    nrPolygons = int(file.readline())

    polygonList = []
    for i in range(nrPolygons):
        nrPoints = int(file.readline())
        pointList = readPoints(file, nrPoints)
        pointList = tuple(pointList)
        polygon = Polygon(*pointList)
        polygonList.append(polygon)

    return polygonList


def readPolygonsAndPoints(file):
    nrPoints = int(file.readline())
    polygonPoints = readPoints(file, nrPoints)

    nrPoints = int(file.readline())
    pointList = readPoints(file, nrPoints)

    polygon = Polygon(*polygonPoints)

    return polygon, pointList


def plotTriangleCircle(trianglePoints, points, problemNumber):
    triangle = Polygon(*(trianglePoints[0], trianglePoints[1], trianglePoints[2]))
    circle = triangle.circumcircle
    circle = plt.Circle((circle.center[0], circle.center[1]), circle.radius, fill=False)

    ax = plt.gca()
    ax.add_patch(circle)
    plotPolygon(triangle.vertices, problemNumber, points=points)


def pointPositionCircle(circle, point):
    radius = circle.radius
    center = Point(circle.center)
    distance = float(center.distance(point))

    if distance == radius:
        return 'on the circle'
    elif distance < radius:
        return 'inside'
    else:
        return 'outside'
