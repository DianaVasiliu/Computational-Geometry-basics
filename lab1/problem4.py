import math
import sys
import math
import matplotlib.pyplot as plt
import helper as hlp


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def computedSum(r, i, j):
    dist1 = distance(i, r)
    dist2 = distance(r, j)
    dist3 = distance(i, j)
    return dist1 + dist2 - dist3


def ratio(r, i, j):
    dist1 = distance(i, r)
    dist2 = distance(r, j)
    dist3 = distance(i, j)
    return (dist1 + dist2) / dist3


def TSP(points):
    contour = hlp.convexHull(points)

    pointsLeft = set()
    for point in points:
        if point not in contour:
            pointsLeft.add(point)

    while pointsLeft:
        bestRatio = sys.maxsize
        pointToAdd = 0
        bestId = 0

        for r in pointsLeft:
            idx = 0
            bestDist = sys.maxsize

            for pos in range(len(contour)):
                currentDist = computedSum(r, contour[pos], contour[(pos + 1) % len(contour)])
                if currentDist < bestDist:
                    bestDist = currentDist
                    idx = pos

            currentRatio = ratio(r, contour[idx], contour[(idx + 1) % len(contour)])
            if currentRatio < bestRatio:
                bestRatio = currentRatio
                pointToAdd = r
                bestId = idx

        pointsLeft.remove(pointToAdd)
        contour.insert(bestId + 1, pointToAdd)

    return contour


def problem4():
    f = open('in_out/4.in', 'r')
    g = open('in_out/my_output/4.out', 'w')

    pointList = hlp.readPoints(f)

    tspPath = TSP(pointList)

    hlp.plot(pointList)
    hlp.plot(tspPath, False)
    plt.title('Problem 4 - TSP')
    plt.show()

    for point in tspPath:
        g.write(str(point[0]) + ' ' + str(point[1]) + '\n')
    g.write(str(tspPath[0][0]) + ' ' + str(tspPath[0][1]))
