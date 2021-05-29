import sys
import matplotlib.pyplot as plt
import numpy as np

epsilon = 1e-5
inf = 1e10
yPlotLim = 10
xPlotLim = 10


def plot(limit, vertical, a, x, y, color):
    if vertical:
        plt.plot([-xPlotLim, xPlotLim], [limit, limit], color=color)
        if a > 0:
            plt.axhspan(-yPlotLim, limit, alpha=0.2, color=color)
        else:
            plt.axhspan(limit, yPlotLim, alpha=0.2, color=color)
    else:
        plt.plot([limit, limit], [-yPlotLim, yPlotLim], color=color)
        if a > 0:
            plt.axvspan(-xPlotLim, limit, alpha=0.2, color=color)
        else:
            plt.axvspan(limit, xPlotLim, alpha=0.2, color=color)
    plt.scatter(x, y, zorder=100, color='white', edgecolors='black')


def pointInPlane(plane, x, y):
    vertical = plane[2]
    if vertical:
        return plane[0] * y + plane[1] <= 0
    else:
        return plane[0] * x + plane[1] <= 0


def problem2(inputFilePath, outputFilePath):
    f = open(inputFilePath, 'r')
    g = open(outputFilePath, 'w')

    nrTests = int(f.readline())

    for i in range(nrTests):
        g.write('example ' + str(i + 1) + ':\n')

        pointCoords = f.readline().split()
        xq = float(pointCoords[0])
        yq = float(pointCoords[1])
        nrPlanes = int(f.readline())

        _, ax = plt.subplots()
        plt.xlim(-xPlotLim, xPlotLim)
        plt.ylim(-yPlotLim, yPlotLim)
        plt.xticks(np.arange(-xPlotLim, xPlotLim, 1))
        plt.yticks(np.arange(-yPlotLim, yPlotLim, 1))

        planes = []
        for _ in range(nrPlanes):
            coeffs = f.readline().split()
            a, b, c = (float(coeffs[0]), float(coeffs[1]), float(coeffs[2]))

            if (abs(a) > epsilon and abs(b) > epsilon) \
                    or (abs(a) < epsilon and abs(b) < epsilon):
                sys.exit("Plane is not vertical or horizontal")

            if abs(a) <= epsilon:
                planes.append((b, c, True))
            elif abs(b) <= epsilon:
                planes.append((a, c, False))

        xInfLim = yInfLim = -inf
        xSupLim = ySupLim = inf

        plt.title("Problem 2 - Test " + str(i + 1))
        colors = ['blue', 'green', 'red', 'cyan', 'yellow']

        for j in range(len(planes)):
            plane = planes[j]

            limit = -plane[1] / plane[0]
            vertical = plane[2]

            # ##### plotting #####
            plot(limit, vertical, plane[0], xq, yq, colors[j % len(colors)])
            # ##### end plotting #####

            if not pointInPlane(plane, xq, yq):
                continue

            if vertical:
                if limit < yq:
                    yInfLim = max(yInfLim, limit)
                if limit > yq:
                    ySupLim = min(ySupLim, limit)

            else:
                if limit < xq:
                    xInfLim = max(xInfLim, limit)
                if limit > xq:
                    xSupLim = min(xSupLim, limit)

        plt.show()

        if ((yInfLim != -inf and ySupLim != inf) and yInfLim - epsilon < ySupLim) and \
                ((xInfLim != -inf and xSupLim != inf) and xInfLim - epsilon < xSupLim):
            # non-empty, finite intersection
            area = (xSupLim - xInfLim) * (ySupLim - yInfLim)

            if abs(float(area) - epsilon) <= int(area):
                area = int(area)

            g.write('(a) there is a rectangle with the required property\n')
            g.write('(b) minimum area is ' + str(area) + '\n\n')

        else:
            # non-empty, infinite intersection or empty intersection
            g.write('(a) there is NOT a rectangle with the required property\n\n')
