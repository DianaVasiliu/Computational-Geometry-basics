import helper as hlp


def problem1():
    f = open('in_out/1.in', 'r')
    g = open('in_out/my_output/1.out', 'w')

    nrPairs = int(f.readline())

    for i in range(nrPairs):
        P = [int(x) for x in f.readline().split()]
        Q = [int(x) for x in f.readline().split()]
        R = [int(x) for x in f.readline().split()]

        orientation = hlp.findOrientation(P, Q, R)
        if orientation == 0:
            g.write('coliniare')
        elif orientation < 0:
            g.write('dreapta')
        else:
            g.write('stanga')
        g.write('\n')
