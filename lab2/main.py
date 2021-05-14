from problem1 import problem1
from problem2 import problem2
from problem3 import problem3
from problem4 import problem4
import os
import helper as hlp

if __name__ == '__main__':

    problem1()
    problem2()
    problem3()
    problem4()

    output_files = os.listdir('in_out')
    output_files = list(filter(lambda x: x.endswith('_out.txt'), output_files))
    my_output_files = os.listdir('in_out/my_out')

    for i in range(len(my_output_files)):
        print('Problem {} checking:'.format(i + 1), end=' ')

        of = 'in_out/' + output_files[i]
        myof = 'in_out/my_out/' + my_output_files[i]

        if of.endswith('_out.txt'):
            same = hlp.checkFiles(of, myof)
            print(same)
