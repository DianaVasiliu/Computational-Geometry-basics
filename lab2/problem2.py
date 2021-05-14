import helper


def monotony(polygon, axis):
    if axis == 'x':
        axis = 0
    elif axis == 'y':
        axis = 1

    n = len(polygon.vertices)
    minimumPoint = polygon.vertices[0]
    idx = 0
    for i in range(1, n):
        point = polygon.vertices[i]
        if point[axis] < minimumPoint[axis]:
            minimumPoint = point
            idx = i

    increasing = True
    currentPoint = polygon.vertices[idx]
    for i in range(1, n):
        otherPoint = polygon.vertices[(i + idx) % n]
        if otherPoint[axis] < currentPoint[axis]:
            increasing = False
        elif otherPoint[axis] > currentPoint[axis] and not increasing:
            return False

        currentPoint = otherPoint
    return True


def problem2():
    f = open('in_out/2_in.txt', 'r')
    g = open('in_out/my_out/my_2_out.txt', 'w')

    polygons = helper.readPolygons(f)

    for i in range(len(polygons)):
        g.write("Polygon {}:\n".format(i + 1))

        polygon = polygons[i]

        helper.plotPolygon(polygon.vertices, number=2, axes=True)

        x_monotony = monotony(polygon, 'x')
        y_monotony = monotony(polygon, 'y')

        if x_monotony:
            is_x = ''
        else:
            is_x = 'not '
        g.write('is {}x-monotone\n'.format(is_x))

        if y_monotony:
            is_y = ''
        else:
            is_y = 'not '
        g.write('is {}y-monotone\n'.format(is_y))
        g.write('\n')
