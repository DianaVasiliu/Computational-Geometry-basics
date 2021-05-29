import sys
import matplotlib.pyplot as plt

yPlotLim = 10
xPlotLim = 10
epsilon = 1e-5
inf = 1e10


def problem1(inputFilePath, outputFilePath):
    f = open(inputFilePath, 'r')
    g = open(outputFilePath, 'w')

    nrTests = int(f.readline())

    for i in range(nrTests):
        nrPlanes = int(f.readline())

        _, ax = plt.subplots()
        plt.xlim(-xPlotLim, xPlotLim)
        plt.ylim(-yPlotLim, yPlotLim)

        xInfLim = yInfLim = -inf
        xSupLim = ySupLim = inf

        for _ in range(nrPlanes):
            coeffs = f.readline().split()
            a, b, c = (float(coeffs[0]), float(coeffs[1]), float(coeffs[2]))
            supLim = inf
            infLim = -inf
            vertical = None

            if (abs(a) > epsilon and abs(b) > epsilon) \
                    or (abs(a) < epsilon and abs(b) < epsilon):
                sys.exit("Plane is not vertical or horizontal")

            if abs(a) <= epsilon:
                vertical = True
                if b > 0:
                    supLim = -c / b
                elif b < 0:
                    infLim = -c / b
            elif abs(b) <= epsilon:
                vertical = False
                if a > 0:
                    supLim = -c / a
                elif a < 0:
                    infLim = -c / a

            if vertical:
                yInfLim = max(yInfLim, infLim)
                ySupLim = min(ySupLim, supLim)
            else:
                xInfLim = max(xInfLim, infLim)
                xSupLim = min(xSupLim, supLim)

            # ###### plotting #####
            plt.title("Problem 1 - Test " + str(i + 1))

            if xSupLim != inf:
                plt.plot([xSupLim] * 2, [-yPlotLim, yPlotLim], color='green')
                ax.axvspan(-xPlotLim, xSupLim, alpha=0.2, color='green')
            if xInfLim != -inf:
                plt.plot([xInfLim] * 2, [-yPlotLim, yPlotLim], color='red')
                ax.axvspan(xInfLim, xPlotLim, alpha=0.2, color='red')
            if ySupLim != inf:
                plt.plot([-xPlotLim, xPlotLim], [ySupLim] * 2, color='blue')
                ax.axhspan(-yPlotLim, ySupLim, alpha=0.3, color='blue')
            if yInfLim != -inf:
                plt.plot([-xPlotLim, xPlotLim], [yInfLim] * 2, color='yellow')
                ax.axhspan(yInfLim, yPlotLim, alpha=0.2, color='yellow')
            # ###### end plotting #####
        plt.show()

        if xInfLim - epsilon > xSupLim or yInfLim - epsilon > ySupLim:
            # empty intersection
            g.write("empty intersection\n")
        elif ((yInfLim != -inf and ySupLim != inf) and yInfLim - epsilon < ySupLim) and \
                ((xInfLim != -inf and xSupLim != inf) and xInfLim - epsilon < xSupLim):
            # non-empty, finite intersection
            g.write("non-empty, finite intersection\n")
        else:
            # non-empty, infinite intersection
            g.write("non-empty, infinite intersection\n")
