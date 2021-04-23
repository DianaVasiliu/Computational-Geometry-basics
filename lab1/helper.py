import matplotlib.pyplot as plt


def checkFiles(file1, file2):
    f = open(file1, 'r')
    g = open(file2, 'r')

    file1 = f.readlines()
    file2 = g.readlines()

    file1 = [x.replace('\n', '').replace('.0', '') for x in file1]
    file2 = [x.replace('\n', '').replace('.0', '') for x in file2]

    print(file1 == file2)


def plot(toPlot, points=True):
    xes = [p[0] for p in toPlot]
    yes = [p[1] for p in toPlot]

    if points:
        plt.scatter(xes, yes)
    else:
        poly = plt.Polygon(list(zip(xes, yes)), fill=None)
        plt.gca().add_patch(poly)
        plt.axis('equal')


def readPoints(file):
    nrPoints = int(file.readline())

    pointList = []
    for i in range(nrPoints):
        point = tuple([int(x) for x in file.readline().split()])
        pointList.append(point)

    return pointList


def findOrientation(p1, p2, p3):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]

    value = (x2 * y3 + x1 * y2 + x3 * y1) - \
            (x2 * y1 + x3 * y2 + x1 * y3)

    return value


def removeDuplicates(l):
    newList = []
    for element in l:
        if element not in newList:
            newList.append(element)
    return newList


def grahamScanInf(points):
    path = [points[0], points[1]]
    for i in range(2, len(points)):
        path.append(points[i])
        while len(path) > 2 and findOrientation(path[-3], path[-2], path[-1]) <= 0:
            path.pop(-2)
    return path


def grahamScanSup(points):
    path = [points[0], points[1]]
    for i in range(2, len(points)):
        path.append(points[i])
        while len(path) > 2 and findOrientation(path[-3], path[-2], path[-1]) > 0:
            path.pop(-2)
    return path


def convexHull(points):
    points.sort(key=lambda p: p[1])
    points.sort(key=lambda p: p[0])
    inferior_hull = grahamScanInf(points)
    superior_hull = grahamScanSup(points)

    inferior_hull.extend(superior_hull)
    convex_hull = removeDuplicates(inferior_hull)

    return convex_hull
