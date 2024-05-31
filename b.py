n = int(input())
d = {}
for i in range(n):
    a = input().split()
    if int(a[3]) not in d:
        d[int(a[3])] = []
    d[int(a[3])].append([int(a[0])*24*60+int(a[1])*60+int(a[2]), a[-1]])
for i in d:
    d[i].sort(key=lambda x: x[0])
sorted_d = dict(sorted(d.items()))
out = []
s = 0
#print(d)
for i in sorted_d:
    for j in range(len(d[i])):
        if d[i][j][1] == 'A':
            continue
        else:
            s += d[i][j][0] - d[i][j-1][0]
    out.append(s)
    s = 0
  
print(*out)
