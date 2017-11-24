try:
    fhandle = open('/Users/Suha/PyFile.txt')
except:
    print('Not able to open the file')
    exit()
for line in fhandle:
    line = line.split()
    if 'From' in line:
        x = line[1]
        x = x.split('@')
        print(x[0])
