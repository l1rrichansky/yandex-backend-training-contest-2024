n = int(input())
out = []
for i in range(n):
    a = input().split(',')
    c1 = len(set(a[0]).union(set(a[1]).union(set(a[2]))))
    c2 = sum([int(i) for i in a[3]]) + sum([int(i) for i in a[4]])
    c3 = ord(a[0][0].upper()) - 64
    c = c1 + c2 * 64 + c3 * 256
    chex = hex(c).upper()[2:]
    if len(chex) < 3:
        fhex = '0'*(3-len(chex)) + hex(c)[2:]
        out.append(fhex)
    else:
        out.append(chex[-3:])
print(*out)
