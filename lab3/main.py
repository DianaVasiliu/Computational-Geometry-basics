from problem1 import problem1
from problem2 import problem2
import os
import helper as hlp

if __name__ == '__main__':
    problem1('in_out/1_in.txt', 'in_out/myout/1_out.txt')
    problem2('in_out/2_in.txt', 'in_out/myout/2_out.txt')

    output_files = os.listdir('in_out')
    output_files = list(filter(lambda x: x.endswith('_out.txt'), output_files))
    my_output_files = os.listdir('in_out/myout')

    for i in range(len(my_output_files)):
        print('Problem {} checking:'.format(i + 1), end=' ')

        of = 'in_out/' + output_files[i]
        myof = 'in_out/myout/' + my_output_files[i]

        if of.endswith('_out.txt'):
            same = hlp.checkFiles(of, myof)
            print(same)
