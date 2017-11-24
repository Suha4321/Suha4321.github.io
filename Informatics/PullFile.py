## write a program to read a file

try:
    fhandle = open('/Users/Suha/PyFile.txt')
except:
    print('Not able to open the file')
    exit()
count = 0
total = 0
print('python shout.py')
# for line in fhandle:
#     if count <5:
#         line = line.rstrip()
#         print(line.upper())
#         count = count +1

## to detect the filename begining with something : Exxcersise 7.2
for line in fhandle:
    if  line.startswith('X-DSPAM-Confidence:'):
        print(line)
        float_str = line.find(':') +1
        req_float = float(line[float_str:])
        total = req_float + total
        count = count+1
print('Total = ' + str(total))
print('Count = '+ str(count))
print('Average =' + ' '+ str(total/count))
