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
