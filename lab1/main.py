import os
import helper as hlp
import problem1 as p1
import problem2 as p2
import problem3 as p3
import problem4 as p4

if __name__ == '__main__':

    p1.problem1()
    p2.problem2()
    p3.problem3()
    p4.problem4()

    output_files = os.listdir('in_out')
    output_files = list(filter(lambda x: x.endswith('.out'), output_files))
    my_output_files = os.listdir('in_out/my_output')

    for i in range(len(my_output_files)):
        print('Problem {} checking:'.format(i + 1), end=' ')

        of = 'in_out/' + output_files[i]
        myof = 'in_out/my_output/' + my_output_files[i]

        if of.endswith('.out', len(of) - 4, len(of)):
            hlp.checkFiles(of, myof)
