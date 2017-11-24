count = {}
t = []
try:
    fhandle = open('/Users/Suha/romeo.txt')
except:
    print('Not able to open the file')
    exit()
for line in fhandle:
    line = line.lower()
    words = line.split()
    for word in words:
        count[word] = count.get(word,0)+1

for (k,v) in count.items():
    t.append((v,k))
t.sort(reverse=True)
print(t[:11])
print(sorted ((v,k) for (k,v) in count.items()))
